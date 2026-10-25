- Router 处理 HTTP 边界；
- Service 表达业务用例；
- Repository 隔离 SQLAlchemy / 数据库访问；

三种常用选择如下。
方法 0 条结果 1 条结果 多条结果 适用场景
scalar_one_or_none() None 返回对象 抛异常 查询有唯一约束的字段，如 email、主键
scalar_one() 抛异常 返回对象 抛异常 业务已保证必须存在且唯一
scalars().first() None 返回第一条 返回第一条 查询列表时只想拿一条，例如“最新一条记录”
