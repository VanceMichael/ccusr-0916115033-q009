# 棋书作品盲审台

Python WSGI 后端起始工程，SQLite 文件位置由 `DATABASE_PATH` 决定。使用 `python -m app.db upgrade` 迁移，`python -m unittest discover -s tests` 测试，`python -m app.server` 启动。

Dockerfile 只包含本地运行所需内容，监听端口从 `PORT` 读取。
