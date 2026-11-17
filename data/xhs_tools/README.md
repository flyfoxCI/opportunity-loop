# Xiaohongshu 小工具 rankings

The official boards (Top100 by users and 7-day activity, and the released-today board) only exist
inside the Xiaohongshu app. There is no public API, and the radar does not scrape the app.
Drop each day's board here and the daily job imports it.

- `YYYY-MM-DD.csv` is the Top100 board, `YYYY-MM-DD_new.csv` is the released-today board
- Columns (any order): `rank,name,users,active_7d,category,note_url,author`
  - Chinese headers work too: 排名, 名称, 使用人数, 7天活跃, 分类, 链接, 作者
  - Numbers like `1.2万` or `3k` are converted
- Missing columns are fine; `name` is the only required one (rank defaults to row order)

Fastest way: screenshot the board in the app, give the screenshots to Claude Code and ask it to
"transcribe these into data/xhs_tools/<today>.csv". Then `python -m radar collect --only xhs && python -m radar build`,
or just commit the file and the daily job picks it up.

`TEMPLATE.csv` is ignored by the importer.
