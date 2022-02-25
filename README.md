## 自用 BPI 地址 ( 第二个 `API` 仓库 ) 
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fzkeq%2Ficodeq-api.svg?type=small)](https://app.fossa.com/projects/git%2Bgithub.com%2Fzkeq%2Ficodeq-api?ref=badge_small)


### 盘古解析逆向 `/api/parwix`

🚀 仓库地址：https://github.com/zkeq/icodeq-bpi/tree/main/api/parwix

🚀 示例地址：https://bpi.icodeq.com/api/parwix

🚀 后端由 Github Action 驱动！

🚀 本项目由两部分组成，数据库基于 `redis`。

🚀 `/api/parwix` 目录下的 `index.py` 是主要文件

🚀 它会去读取 `Redis` 上面的 `视频链接` 的值

🚀 而 `/api/parwix/get-new-url/main.py` 则负责传递 `真实视频地址` 的值。

🚀 （依靠 `decode.js` 解密返回的请求）

🚀 一小时执行一次 Action .

> 🚀 推荐项目: [拒绝外链播放器！直接把 B 站 1080P 视频嵌入 Notion](https://www.notion.so/B-1080P-Notion-88315db1b76f4e72a610e4e692cd8f96) [可惜不开源]

## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fzkeq%2Ficodeq-api.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fzkeq%2Ficodeq-api?ref=badge_large)