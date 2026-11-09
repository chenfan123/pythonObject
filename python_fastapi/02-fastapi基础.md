##### 启动服务

1. 通过命令：`uvicorn file_name:app_name --reload`
2. 通过代码：`uvicorn.run(app, host="0.0.0.0", port=8000)`
3. 通过调试：`fastapi dev filename`

### 传参方式

- 路径参数
- 查询参数
- 请求体
- 表单数据

### 参数校验

1. 原生类型注解
2. 查询参数使用 Query 类
3. 路径参数使用 Path 类
4. Field 方式
5. 表单数据使用 Form 类

## 异步与非异步

### 异步

##### 事件循环

异步代码运行在 python 的异步事件循环（如 asyncio）中，事件循环负责协调多个协程,在某个协程等待 I/O 操作时，事件循环可以切换到其他协程执行，

##### 非阻塞

当一个异步函数调用 await，他回暂停执行将控制权交回事件循环，允许其他任务运行，直到等待的操作完成。

##### 并发性

异步模式允许单个线程处理大量并发请求，特别适合高并发场景

### 非异步

##### 阻塞式执行

同步函数在调用时会完全占用线程，直到函数执行完成才会释放线程

##### 线程池

同步函数由工作线程处理，Uvicorn 会将同步函数放入线程池运行

##### 并发限制

线程池的大小限制了同步函数的并发能力，如果线程池耗尽，新的请求会排队等待，可能导致响应延迟

## 文件上传

### 基础文件上传

#### bytes 类型（适合小文件）

- 文件以二进制形式读取，适合小于 10MB 的文件
- 内存占用高，大文件可能导致崩溃

#### uploadFile 类型（推荐）

- 自动处理内存和磁盘存储（超过阈值存磁盘）
- 支持文件元数据（filename、content-type）
- 提供异步文件操作方法（read()、write())

## 请求对象 Request

- 获取客户端信息
- 获取请求头
- 获取请求体
- 获取请求查询参数
- 获取请求表单数据
- 获取请求 cookies
- 获取请求状态码
- 获取请求协议
- 获取请求主机
- 获取请求路径
- 获取请求全路径
- 获取请求引用 URL
- 获取请求 User-Agent

  ## 响应对象 Response

- JSON 响应：用于 RESTful API 的数据交互，占主导地位
- 列表响应：用于分页查询或批量数据返回
- 文件响应：用于文件下载或上传
- 字符串响应：用于健康检查或简单状态反馈
- HTML 响应：用于渲染网页内容
- 重定向响应：用于认证流程或 URL 前一
- 流式响应：用于实时数据传输或大文件处理

### JSON 响应

1. 通过`response_model`实现相应数据结构校验
2. 使用`response_model_exclude_unset=True`过滤未设置的默认值字段
3. 组合模型：`response_model=Union[SuccessResponse[User], ErrorResponse[User]]`

### 文件格式

#### 关键特点

内容类型：通过 Content-Type 头信息指定文件 MIME 类型，如 application/pdf、text/csv、application/vnd.ms-excel
文件内容：body 包含文件的实际数据，可能是二进制或文本

#### 大文件的处理

先读取文件拆分成 chunks，然后通过 StreamingResponse 返回

### 其他响应的格式

#### 字符串响应

直接返回字符串，格式为 text/plain

#### html 响应

直接返回 html 字符串，格式为 text/html

#### 重定向响应

通过 RedirectResponse 返回重定向响应，格式为 302 Found

## ORM

对象关系映射，用于在面向对象编程语言和关系型数据库之间建立映射。

工作原理：

- 定义了一个映射层，将类和数据库表关联起来
- 开发者通过 ORM 的 API 操作对象，ORM 自动将操作翻译成 SQL 语句，并执行

SQLAlchemy\Tortoise\Gino

### Aerich 迁移工具

是 Tortoise-ORM 的迁移工具，用于管理数据库结构的变更。

#### 初始化：

`aerich init -t main.TORTOISE_ORM`
这回生成

- pyproject.toml:Aerich 的配置文件,指定迁移配置
- migrations:迁移文件目录，存放生成的.sql 文件
  `aerich init-db`:初始化数据库
- 生成迁移文件：当模型发生变更时，运行以下命令生成迁移文件
  `aerich migrate --name 'info_table'`
- 应用迁移：运行以下命令将迁移应用到数据库
  `aerich upgrade`
- 验证迁移：检查迁移历史
  `aerich history`
- 回滚迁移：回退到制定版本
  `aerich downgrade`

#### 说明

- 继承 Model 类:所有模型必须继承 tortoise.models.Model
- 字段定义：每个字段对应数据库表中的一列，使用 Tortoise-ORM 的字段类（如 CharField、BooleanField）
- Meta 类：定义模型元数据，如表名、排序规则等

#### 核心字段类型详解

| Python 字段类型            | 数据库类型           | 描述           | 常用参数                                                     |
| -------------------------- | -------------------- | -------------- | ------------------------------------------------------------ |
| `CharField`                | VARCHAR              | 字符串         | `max_length`（必填）、`unique=True`、`index=True`            |
| `TextField`                | TEXT                 | 长文本         | `null=True`（允许为空）                                      |
| `IntField` / `BigIntField` | INTEGER / BIGINT     | 整数           | `pk=True`（主键）、`default=0`                               |
| `FloatField`               | DOUBLE / REAL        | 浮点数         | `gt=0`（值必须大于 0）                                       |
| `DecimalField`             | DECIMAL              | 高精度小数     | `max_digits=10`、`decimal_places=2`（最多 10 位，小数 2 位） |
| `BooleanField`             | BOOLEAN              | 布尔值         | `default=True`                                               |
| `DateField`                | DATE                 | 日期           | `auto_now=True`（保存时更新）                                |
| `DatetimeField`            | DATETIME / TIMESTAMP | 日期时间       | `auto_now_add=True`（仅首次保存记录时间）                    |
| `JSONField`                | JSON / JSONB         | 存储字典或列表 | `encoder`（自定义编码器）、`decoder`（自定义解码器）         |
| `UUIDField`                | UUID / CHAR(36)      | 唯一标识符     | 作为主键时默认生成 UUID4                                     |
| `BinaryField`              | BLOB                 | 二进制数据     | 不支持过滤和更新操作                                         |

#### 字段参数详解

- `max_length`：字符串字段的最大长度（`CharField` 必填）
- `null`：是否允许字段为空（`null=True` 允许数据库中为 NULL）
- `default`：字段的默认值（如 `default=0`、`default=True`）
- `unique`：值是否必须唯一（`unique=True` 确保表中唯一）
- `index`：是否创建索引（`index=True` 提升查询性能）

#### 模型元数据（Meta 类）

Meta 类用于定义模型的元数据，控制表结构和查询行为。常用属性包括：

- `table`：自定义数据库表名（如 `table="users"`）
- `unique_together`：定义联合唯一约束（如 `unique_together=[("field1", "field2")]`）
- `indexes`：定义索引（如 `indexes=[("field1", "field2")]`）
- `ordering`：默认排序规则（如 `ordering=["-created_at", "username"]`）
