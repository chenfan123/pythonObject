import re
from pathlib import Path

from dotenv import load_dotenv

from llm.llm import QwenClient
from promptTemplate.travel_prompt import AGENT_SYSTEM_PROMPT
from tools import available_tools

# 加载 python_agent/.env（DASHSCOPE_* / TAVILY_API_KEY）
load_dotenv(Path(__file__).resolve().parent / ".env", override=True)


def run_agent(user_prompt: str, max_steps: int = 5) -> str | None:
    """ReAct 风格主循环：Thought -> Action -> Observation。"""
    # --- 1. 配置 LLM 客户端（通义千问） ---
    llm = QwenClient()

    # --- 2. 初始化对话历史 ---
    prompt_history = [f"用户请求: {user_prompt}"]
    print(f"用户输入: {user_prompt}\n" + "=" * 40)

    # --- 3. 运行主循环 ---
    for i in range(max_steps):
        print(f"--- 循环 {i + 1} ---\n")

        # 3.1. 构建 Prompt
        full_prompt = "\n".join(prompt_history)

        # 3.2. 调用 LLM 进行思考
        llm_output = llm.generate(full_prompt, system_prompt=AGENT_SYSTEM_PROMPT)
        # 模型可能会输出多余的 Thought-Action，需要截断
        match = re.search(
            r"(Thought:.*?Action:.*?)(?=\n\s*(?:Thought:|Action:|Observation:)|\Z)",
            llm_output,
            re.DOTALL,
        )
        if match:
            truncated = match.group(1).strip()
            if truncated != llm_output.strip():
                llm_output = truncated
                print("已截断多余的 Thought-Action 对")
        print(f"模型输出:\n{llm_output}\n")
        prompt_history.append(llm_output)

        # 3.3. 解析并执行行动
        action_match = re.search(r"Action:\s*(.*)", llm_output, re.DOTALL)
        if not action_match:
            observation = (
                "错误: 未能解析到 Action 字段。"
                "请确保你的回复严格遵循 'Thought: ... Action: ...' 的格式。"
            )
            observation_str = f"Observation: {observation}"
            print(f"{observation_str}\n" + "=" * 40)
            prompt_history.append(observation_str)
            continue

        action_str = action_match.group(1).strip().splitlines()[0].strip()

        if action_str.startswith("Finish"):
            finish_match = re.match(r"Finish\[(.*)\]", action_str, re.DOTALL)
            if not finish_match:
                observation = "错误: Finish 格式应为 Finish[最终答案]"
                observation_str = f"Observation: {observation}"
                print(f"{observation_str}\n" + "=" * 40)
                prompt_history.append(observation_str)
                continue
            final_answer = finish_match.group(1)
            print(f"任务完成，最终答案: {final_answer}")
            return final_answer

        tool_match = re.search(r"(\w+)\(", action_str)
        args_match = re.search(r"\((.*)\)", action_str)
        if not tool_match or not args_match:
            observation = f"错误:无法解析工具调用格式: {action_str}"
            observation_str = f"Observation: {observation}"
            print(f"{observation_str}\n" + "=" * 40)
            prompt_history.append(observation_str)
            continue

        tool_name = tool_match.group(1)
        args_str = args_match.group(1)
        kwargs = dict(re.findall(r'(\w+)="([^"]*)"', args_str))

        if tool_name in available_tools:
            observation = available_tools[tool_name](**kwargs)
        else:
            observation = f"错误:未定义的工具 '{tool_name}'"

        # 3.4. 记录观察结果
        observation_str = f"Observation: {observation}"
        print(f"{observation_str}\n" + "=" * 40)
        prompt_history.append(observation_str)

    print("已达到最大循环次数，任务未完成。")
    return None


if __name__ == "__main__":
    run_agent("你好，请帮我查询一下今天北京的天气，然后根据天气推荐一个合适的旅游景点。")
