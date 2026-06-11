# 知识库模板与规范

## 页面类型

| 类型 | 用途 | 目录 | frontmatter 必备 |
|------|------|------|------------------|
| source | 单个原始资料的提炼 | `wiki/sources/` 或 `wiki/sources/` | `sources` |
| concept | 概念/方法论/思想 | `wiki/concepts/` | `sources`, `claims` |
| entity | 实体（人物/工具/产品）| `wiki/entities/` | `sources`, `claims` |
| synthesis | 综合多源的笔记 | `wiki/syntheses/` | `sources`, `claims` |

## 模板

- **`factual-page.md`** — 事实类页面（D 方案结构化模板，含 `claims` 数组）
- 创作/叙事类页面（克苏鲁、维度黎明等）继续用宽松散文格式

## 矛盾检测机制

D 方案（2026-06-08 落地）：

1. **事实层**（新闻/医学/科技/投资）—— 用 `claims` 数组结构化
2. **创作层**（《维度黎明》等）—— 不强制结构化，主人随时问主代理
3. **验证器**：`scripts/wiki-conflict-scanner.sh` —— 扫 `claims`，找：
   - 同一 source 被不同页面引用但说不同
   - 引用了已不存在的 source
   - 页面缺少 `last_conflict_check` 字段
4. **跑时**：`wiki-monthly-raw-scan.sh` 之后自动调用

## 写新页面流程

1. 复制 `_templates/factual-page.md` 到目标目录
2. 填 frontmatter（**`sources` 和 `claims` 必填**）
3. 写正文
4. 跑 `validate-snapshot.sh` 确认没破坏

## 老页面迁移

**不主动迁移**。每次更新老页面时**顺手**补 `claims` 数组——慢慢覆盖。

## 验证器命令

```bash
# 干跑
bash /home/azhan186/open\ claw/scripts/wiki-conflict-scanner.sh

# 看报告
cat /home/azhan186/open\ claw/知识库/data/wiki-conflict-report-YYYY-MM-DD.txt
```
