# 记忆路径统一清理 - 2026-06-23

## 背景

知识库历史上存在 **3 套并行的 memory 日志路径**，内容不一致：

| 路径 | 状态 |
|------|------|
| A. `/home/azhan186/open claw/memory/` | ✅ LLM cron 实际写入路径（19 个文件，最新 06-23） |
| B. `/home/azhan186/open claw/知识库/记忆/` | ⚠️ `memory-daily.sh` 配置路径（15 个文件，最新 06-22，**脚本其实没跑**） |
| C. `/home/azhan186/open claw/知识库/memory/` | ❌ 空目录，历史遗留 |

主人于 2026-06-23 23:38 决策：统一到 A（方案 1）。

## 关键发现：挂载点等价

清理过程中发现：`/home/azhan186/open claw` 和 `/root/.openclaw/workspace` **是同一个文件系统设备**（`/dev/mapper/ug_8E91A3_1778565269_pool1-volume1`）的双挂载点，inode 验证同号。所以：

- `$WORKSPACE/memory` ≡ `/home/azhan186/open claw/memory`（memory-cleanup.sh 的路径已正确）
- 路径"不一致"只是符号层面，物理上是同一份数据

但 `/home/azhan186/open claw/知识库/memory/` 是**真正独立的子目录**（不在等价路径里），所以 C 路径才是真正孤立的历史遗留。

## 移动清单（15 个文件）

| 文件 | 大小 | A 路径有同天？ |
|------|------|---------------|
| 2026-06-03.md | 3.8K | ❌ A 无 |
| 2026-06-05.md | 6.1K | ❌ A 无 |
| 2026-06-06.md | 1.8K | ❌ A 无 |
| 2026-06-07.md | 5.0K | ❌ A 无 |
| 2026-06-08.md | 5.4K | ❌ A 无 |
| 2026-06-09.md | 5.0K | ❌ A 无 |
| 2026-06-10.md | 9.3K | ✅ A 有（md5 不同） |
| 2026-06-11.md | 10.4K | ✅ A 有（md5 不同） |
| 2026-06-12.md | 14.6K | ✅ A 有（md5 不同） |
| 2026-06-18.md | 14.1K | ✅ A 有（md5 不同） |
| 2026-06-19.md | 3.9K | ✅ A 有（md5 不同） |
| 2026-06-20.md | 5.0K | ✅ A 有（md5 不同） |
| 2026-06-21.md | 4.2K | ✅ A 有（md5 不同） |
| 2026-06-22.md | 7.4K | ✅ A 有（md5 不同） |
| NAS升级SOP_4x16T_RAID6.md | 12.3K | ❌ A 无（不是日志） |

**说明**：
- 06-10 至 06-22 的 9 个文件与 A 路径内容不一致（md5 不同），主人接受以 A 为准
- 06-03 至 06-09 的 6 个文件 A 路径没有，已随本清理移到本目录
- NAS升级SOP_4x16T_RAID6.md 是参考资料，不是日志，附带清理

## 恢复方式

30 天内可恢复（AGENTS.md 软删除策略）：
```bash
mv /home/azhan186/open\ claw/知识库/_trash/2026-06-23_记忆路径统一/<文件名> \
   /home/azhan186/open\ claw/memory/
```

60 天后自动硬删除。

## 配套改动

- `/home/azhan186/open claw/scripts/memory-daily.sh`：MEMORY_DIR 改为 `/home/azhan186/open claw/memory`（统一指向 A）
- 删除了 `/home/azhan186/open claw/知识库/记忆/`（空）
- 删除了 `/home/azhan186/open claw/知识库/memory/`（空）
