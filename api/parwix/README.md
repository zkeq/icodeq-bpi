### 盘古解析逆向 `/api/parwix`

🚀 仓库地址：https://github.com/zkeq/icodeq-bpi/tree/main/api/parwix

🚀 示例地址：https://bpi.icodeq.com/api/parwix

🚀 后端由 Github Action 驱动！

🚀 本项目由两部分组成，数据库基于 `redis`。

🚀 `/api/parwix` 目录下的 `index.py` 是主要文件

🚀 它会去读取 `Redis` 上面的 `视频链接` 的值

🚀 而 `/api/parwix/get-new-url/main.py` 则负责传递 `真实视频地址` 的值。

🚀 （爬虫数据依靠 `decode.js` 解密返回的请求）

🚀 一小时执行一次 Action .

#### 使用说明

1. 替换一下 `/get-new-url/main.py` 中列表中的视频链接值

2. 添加环境变量为你的 `Redis` 密码，更改代码中的 Redis 地址

2. 运行 Github `Action` 

4. 查看 Action 日志是否成功

5. 查看 Redis 后台是否有数据

6. 测试 https://bpi.icodeq.com/api/parwix
