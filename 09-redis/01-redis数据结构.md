# Redis 数据结构

## String 与 TTL

```
SET：写 Key
GET：读 Key
EX：设置秒级 TTL
TTL：查看剩余过期时间
过期后 GET 返回 nil
```

```
GET 有值      → Key 存在
GET 返回 nil  → Key 不存在或已过期
TTL = -2      → Key 不存在
```

## Hash 与局部更新

- Hash：一个 Redis Key 下保存多个 field-value
  - `HSET user:1001 name "Alice" city "Shanghai" level "vip"`
- HSET：设置字段
  - `HSET user:1001 city "Beijing"`
- HGET：读取单个字段
  - `HGET user:1001 name`
- HGETALL：读取整个对象
  - `HGETALL user:1001`
- Hash 的 TTL 默认仍是整个 Key 的 TTL

> user:1001 是 redis 的一个 key,也就是存放数据的名字。user 表示业务前缀，1001 表示用户 id。

## List、Set、Sorted Set 选型

- List → 队列，关注进出顺序
- Set → 去重集合，关注是否存在
- Sorted Set → 去重 + score 排序

### List

简单待处理任务队列

```
- RPUSH queue:email task:1 task:2 task:3 → 添加任务 1、2、3 到队列
- LRANGE queue:email 0 -1 → 获取队列中的所有任务
- LPOP queue:email → 从队列中取出第一个任务
- LRANGE queue:email 0 -1 → 获取队列中的所有任务
```

### Set

文章点赞用户，自动去重

- SADD post:100:likes user:1 user:2 user:1 → 添加用户 1、2 到文章 100 的点赞集合
- SMEMBERS post:100:likes → 获取文章 100 的点赞用户集合
- SISMEMBER post:100:likes user:1 → 判断用户 1 是否点赞了文章 100
- SCARD post:100:likes → 获取文章 100 的点赞用户数量

### Sorted Set

文章热度排行榜

- ZADD leaderboard 90 Alice 80 Bob 100 Carol → 添加用户 Alice、Bob、Carol 到排行榜，分数分别为 90、80、100
- ZREVRANGE leaderboard 0 -1 WITHSCORES → 获取排行榜前 3 名
- ZINCRBY leaderboard 15 Bob → 将用户 Bob 的分数增加 15
- ZREVRANGE leaderboard 0 -1 WITHSCORES → 获取排行榜前 3 名
