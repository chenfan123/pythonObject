# 限流、Session 与任务状态

- 限流：这个请求现在能不能进来？
- Session：这个请求是谁发起的？
- 任务状态：之前创建的任务现在做到哪了？

## 限流

为接口主动设定一个可承受的规则，每次请求到来时，服务端用 Redis 记录计数。

```shell
Key:   rate_limit:product-detail:user:42
Value: 当前窗口内第几次访问
TTL:   剩余窗口时间

计数 ≤ 3 → 放行
计数 > 3 → 返回 429 Too Many Requests
TTL 到期 → Key 自动删除，下一次从 1 重新计数
```

FastAPI 典型的位置是：

```shell
请求
→ 认证 Dependency 得到 current_user
→ 限流 Dependency 根据 current_user.id 增加 Redis 计数
→ 未超限：进入路由
→ 超限：直接抛 429，路由不执行
```

使用 Lua 把两步合成一个原子操作：

```shell
INCR key
如果结果是 1 → EXPIRE key window_seconds
```

为什么要合并？如果先 INCR，进程恰好在 EXPIRE 前崩溃，Key 会没有 TTL，用户可能被永久限流。

固定窗口的局限是边界突刺：用户能在 12:00:59 用完配额，又在 12:01:00 立即使用新窗口配额。验证码、普通搜索等保护场景通常能接受；支付风控等更敏感的场景会使用滑动窗口或令牌桶

面试讲解：

> 我会基于认证后的用户 ID 或 IP 构造 Redis 限流 Key，通过原子计数和 TTL 实现固定窗口限流；超限返回 429 和 Retry-After。对于边界突刺敏感的接口，再考虑滑动窗口或令牌桶。

## Session：从 Cookie 到 current_user

```shell
Cookie: session_id=随机 UUID
Redis:  session_id → {user_id, username, role}
```

登录时

```shell
验证用户身份
→ 生成不可预测的 UUID
→ HSET session:lab:{uuid}
→ EXPIRE 1800
→ Set-Cookie: session_id={uuid}
```

注销有两个动作，缺一不可：
DEL Redis Session + 删除浏览器 Cookie

Cookie 的安全选项：

- HttpOnly=True：浏览器 JavaScript 不能直接读取 Cookie，降低 XSS 窃取风险。
- Secure=True：生产环境仅允许 HTTPS 发送。实验是本地 HTTP，所以暂设为 False。
- SameSite="lax"：限制部分跨站携带 Cookie 的情况，降低 CSRF 风险。

## 任务状态与长任务接口

重点不是 Redis 命令，而是把 HTTP 请求和长时间工作拆开.

```shell
POST /jobs
→ 系统接收任务
→ 返回 202 + job_id

GET /jobs/{job_id}
→ 返回任务当前状态
```

## 限流进阶：滑动窗口

固定窗口的问题是：

- 12:00:59 通过 3 次
- 12:01:00 又通过 3 次

两秒不到通过 6 次。

滑动窗口不按整分钟切段，而是始终查看“现在向前推 10 秒”的真实请求数量。

例如限制“任意连续 10 秒最多 3 次”

Redis 常用 Sorted Set 实现：

```shell
Key:    rate_limit:upload:user:42
Score:  请求时间戳
Member: 每次请求唯一 ID

1. 删除 10 秒前的旧请求记录
2. 统计当前 ZSet 中还剩多少条
3. 未超过上限 → 写入当前请求时间戳，放行
4. 已超过上限 → 返回 429
5. 给整个 Key 设置 TTL，避免空 Key 长期残留
```

> 我会使用认证后的用户身份构造 Redis 限流 Key：普通接口可用固定窗口，高敏感接口采用 ZSet 加 Lua 的滑动窗口；Session 用 HttpOnly Cookie 保存随机 session_id，并在 Redis 保存用户映射与 TTL；长任务返回 202 和 job_id，由独立 Worker 更新 Redis 中的任务状态，前端按 job_id 查询进度。
