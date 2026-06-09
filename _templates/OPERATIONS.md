# 知识库运维手册

> 创建于 2026-06-08  
> 维护者：主代理 + OpenClaw cron + isolated session

---

## 1. OpenClaw 定时任务（cron）

| 时间 | 任务 | 用途 | 产物 |
|------|------|------|------|
| 0:30 | 图书馆和新闻增量检查-凌晨 | 跑 wiki-auto-update.sh，编译昨天新 Raw Sources | `wiki/sources/` + `wiki/concepts/` + `wiki/index.md` |
| 2:00 | 每日记忆汇总 | 跑 isolated session 总结昨天变更，**有变更时飞书通知** | `知识库/记忆/YYYY-MM-DD.md` |
| 8:00 (1日) | 图书馆和新闻月度整理与矛盾检测 | 月度跑：wiki-monthly-raw-scan + wiki-conflict-scanner + wiki-deep-check | `data/wiki-monthly-new-sources-*.txt` + `data/wiki-conflict-report-*.txt` |
| 8:30 | 每日新闻收集 | 跑 news-collect.sh 采集百度热搜 | `data/news-YYYY-MM-DD.json` + 飞书 |
| 9:00 | 每日新闻发送 | 读 news.json，发送"今日天气 + 5 条新闻" | 飞书 |
| 12:30 | 图书馆和新闻增量检查-中午 | 同 0:30 任务（处理中午前新文件） | 同上 |
| 16:30 | 财经新闻采集 | 跑 finance-collect.sh | `data/finance-YYYY-MM-DD.json` |
| 16:45 | 财经新闻发送 | 读 finance.json，发送"明日天气 + 3 条财经" | 飞书 |
| **已禁用** | ~~处理99个SOP docx文件~~ | ~~一次性 6/8 任务完成~~ | ~~无~~ |

配置文件：`/root/.openclaw/cron/jobs.json`

---

## 2. scripts 目录清单

位置：`/home/azhan186/open claw/scripts/`

### 核心（每天/每小时跑）

| 脚本 | 用途 | 触发者 |
|------|------|--------|
| `heartbeat-raw-check.sh` | 30 分钟一次的轻量增量检测，写 `.raw_sources_snapshot.md` | OpenClaw cron |
| `wiki-auto-update.sh` | 完整增量更新，写 `.raw_sources_snapshot.{md,all}` + 生成报告 | OpenClaw cron (0:30 + 12:30) |
| `mark-compiled.sh` | 标记文件为已编译（避免入 queue） | 主代理/子代理手动 |

### 月度任务

| 脚本 | 用途 | 触发者 |
|------|------|--------|
| `wiki-monthly-raw-scan.sh` | 扫描上月新增 Raw Sources（sort -u + 相对路径） | OpenClaw cron (1日 8:00) |
| `wiki-conflict-scanner.sh` / `.py` | 矛盾检测（结构化字段对比） | OpenClaw cron + 主代理手动 |
| `wiki-deep-check.sh` | 断链检查（cumulative scan 上月 Wiki 页面） | OpenClaw cron (1日 8:00) |
| `wiki-migrate.sh` | 5 批 Wiki 目录迁移（一次性） | 手动（2026-06-08 完成） |

### 健康与索引

| 脚本 | 用途 |
|------|------|
| `validate-snapshot.sh` | 校验 snapshot 一致性 + `.compiled_files.list` 引用完整性 |
| `regenerate-topics-index.sh` | 按主题词表重生成 `_taxonomy/topics-index.md` |
| `expired-content-check.sh` | 检查 `data_date` 过期的新闻/投资类页面 |

### 库

| 文件 | 用途 |
|------|------|
| `lib/domain_classifier.py` | 按文件名判断 Raw Sources 所属领域 |

### 其他（早期遗留）

| 脚本 | 状态 |
|------|------|
| `check_raw_sources.sh` | 旧版 raw_check，被 heartbeat 取代 —— 可忽略 |
| `news-collect.sh` / `news-send.sh` / `finance-collect.sh` / `finance-send.sh` / `news-5day.sh` | 新闻+财经日报支持脚本 |
| `memory-daily.sh` | 路径 P2-a 后已更新，但实际未跑（isolated session 用 LLM 写） |

---

## 3. 运行时文件

位置：`/home/azhan186/open claw/知识库/`

| 文件 | 用途 | 由谁写 |
|------|------|--------|
| `.raw_sources_snapshot.md` | md/pdf 文件快照 | `heartbeat-raw-check.sh` + `wiki-auto-update.sh` |
| `.raw_sources_snapshot.all` | md/pdf/docx/txt 完整快照 | `wiki-auto-update.sh` |
| `.last-processed` | wiki-auto-update 时间戳 | `wiki-auto-update.sh` |
| `.compiled_files.list` | 已编译文件列表 | `mark-compiled.sh`（主代理手动） |
| `.deep-check-checkpoint.json` | 月度矛盾检测断点续传 | `wiki-deep-check.sh` |
| `.raw_sources_snapshot.bak.YYYY-MM-DD.txt` | 旧格式备份 | 手动（迁移时） |

**Git ignore**（已在 `.gitignore`）：
- `.raw_sources_snapshot*`
- `.last-processed`
- `.deep-check-checkpoint.json`
- `.compiled_files.list`
- `__pycache__/`

---

## 4. 报告输出

位置：`/home/azhan186/open claw/知识库/data/`

| 文件 | 生成者 | 用途 |
|------|--------|------|
| `wiki-conflict-report-YYYY-MM-DD.txt` | `wiki-conflict-scanner.sh` | 矛盾检测报告（同源对比候选 + 缺失 source） |
| `expired-content-report-YYYY-MM-DD.txt` | `expired-content-check.sh` | 过期内容清单 |
| `wiki-monthly-new-sources-YYYY-MM.txt` | `wiki-monthly-raw-scan.sh` | 上月新增 Raw Sources |
| `wiki-new-files-YYYY-MM-DD-HHMMSS.txt` | `wiki-auto-update.sh` | 增量检查发现的新文件报告 |

---

## 5. 日志

| 日志 | 路径 |
|------|------|
| Raw check | `/root/.openclaw/workspace/logs2/raw_check.log` |
| Auto-compile | `/root/.openclaw/workspace/logs2/auto_compile.log` |
| Wiki auto-update | `/root/.openclaw/openclaw/知识库/logs/wiki-auto-update.log` |
| Wiki conflict scan | `/root/.openclaw/workspace/logs/wiki-conflict-scanner.log` |
| Wiki deep check | `/root/.openclaw/workspace/logs/wiki-deep-check.log` |
| Memory daily | `/root/.openclaw/workspace/logs/memory-daily.log` |

---

## 6. 常见问题排查

### Q1: 12:35 之前报"50 个新 Raw Sources"是误报吗？

**A1:** 是的。**已修复**（2026-06-08）：
- 原因：两脚本共用 snapshot + sort 与 sort -u 不一致
- 修复：双 snapshot 设计（`.md` + `.all`）+ 统一 `sort -u` + 相对路径
- 验证：`validate-snapshot.sh` 跑通，353/25/44 三项指标稳定

### Q2: Raw Sources 数量对不上？

**A2:** 跑 `validate-snapshot.sh`——会报告 `.md` snapshot 行数 vs 实际文件数——不匹配就是丢了

### Q3: 矛盾检测漏了某对新页面？

**A3:** 跑 `wiki-conflict-scanner.sh` 看报告 [3] 段（"source 被多页面引用"）——这是同源对比候选——主人/主代理人工审视

### Q4: 6/4 月度任务为何说"未做矛盾检测"？

**A4:** 已修。**月度任务 payload 第一步空白**导致子代理自己想办法——6/4 那次只列了文件清单，没做实际矛盾检测。
- 修复：payload 明确指定 `wiki-monthly-raw-scan.sh` + `wiki-conflict-scanner.sh`
- 下次 7/1 8:00 自动跑新链路

### Q5: 知识库膨胀很快，能清理吗？

**A5:** 跑 `expired-content-check.sh`——标了 `data_date` + `freshness` 的页面会报告——手动决定清理哪些

### Q6: 加新 cron 任务怎么改？

**A6:** 编辑 `/root/.openclaw/cron/jobs.json`——改完保存即可，下次触发自动生效

### Q7: 知识库更新出问题怎么回滚？

**A7:** `.git` 仓库保护
- 出问题：`cd /home/azhan186/open claw/知识库 && git status` 看未提交
- 回滚某次提交：`git checkout <commit_hash> -- <path>`
- 最新 commit `9400843 "新增：NAS存储概念"` 状态稳定

---

## 7. 文档版本

| 日期 | 变更 |
|------|------|
| 2026-06-08 | 创建（C 方案落地后）|

---

*最后更新：2026-06-08*
