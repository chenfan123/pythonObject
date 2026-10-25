"""Redis Hash 任务状态实验：独立于缓存与限流示例。"""

import asyncio
from contextlib import asynccontextmanager
from typing import Literal
from uuid import uuid4

import redis.asyncio as redis
from fastapi import FastAPI, HTTPException, Request, status
from pydantic import BaseModel, Field


REDIS_URL = "redis://localhost:6380/0"
JOB_TTL_SECONDS = 3600


class JobCreateDTO(BaseModel):
    input_file: str = Field(min_length=1, max_length=200)
    duration_seconds: int = Field(default=3, ge=1, le=10)
    should_fail: bool = False


class JobCreatedDTO(BaseModel):
    job_id: str
    status: Literal["queued"]


class JobStatusDTO(BaseModel):
    job_id: str
    status: Literal["queued", "running", "succeeded", "failed"]
    progress: int = Field(ge=0, le=100)
    input_file: str
    result_url: str | None = None
    error_code: str | None = None
    error_message: str | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = redis.from_url(REDIS_URL, decode_responses=True)
    await client.ping()
    app.state.redis = client
    try:
        yield
    finally:
        await client.aclose()


app = FastAPI(title="Redis Task Status Lab", lifespan=lifespan)


def job_key(job_id: str) -> str:
    return f"task:job:{job_id}"


async def run_demo_job(
    client: redis.Redis,
    job_id: str,
    duration_seconds: int,
    should_fail: bool,
) -> None:
    """仅用于教学；生产中由独立 Worker/任务队列执行。"""
    redis_key = job_key(job_id)
    await client.hset(redis_key, mapping={"status": "running", "progress": "0"})
    for progress in (25, 50, 75, 100):
        await asyncio.sleep(duration_seconds / 4)
        await client.hset(redis_key, "progress", progress)

    if should_fail:
        await client.hset(
            redis_key,
            mapping={
                "status": "failed",
                "error_code": "PARSE_FAILED",
                "error_message": "The demo parser could not read this file.",
            },
        )
        return

    await client.hset(
        redis_key,
        mapping={
            "status": "succeeded",
            "result_url": f"/downloads/{job_id}.json",
        },
    )


@app.post("/lab/jobs", status_code=status.HTTP_202_ACCEPTED, response_model=JobCreatedDTO)
async def create_demo_job(payload: JobCreateDTO, request: Request) -> JobCreatedDTO:
    job_id = str(uuid4())
    client: redis.Redis = request.app.state.redis
    redis_key = job_key(job_id)
    await client.hset(
        redis_key,
        mapping={
            "status": "queued",
            "progress": "0",
            "input_file": payload.input_file,
        },
    )
    await client.expire(redis_key, JOB_TTL_SECONDS)

    # 演示用途：应用重启会中断它，生产中应用投递任务给独立 Worker。
    asyncio.create_task(
        run_demo_job(client, job_id, payload.duration_seconds, payload.should_fail)
    )
    return JobCreatedDTO(job_id=job_id, status="queued")


@app.get("/lab/jobs/{job_id}", response_model=JobStatusDTO)
async def get_demo_job(job_id: str, request: Request) -> JobStatusDTO:
    data = await request.app.state.redis.hgetall(job_key(job_id))
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"code": "JOB_NOT_FOUND", "message": "Job was not found"},
        )
    return JobStatusDTO(job_id=job_id, **data)
