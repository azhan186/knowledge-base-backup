# Wiki 目录统一迁移计划（P2-a，待办）

## 现状

```
知识库/
├── 图书馆/Wiki/
│   ├── concepts/   (~80)
│   ├── entities/   (~20)
│   ├── sources/    (~180)
│   ├── syntheses/  (~30)
│   └── 客房部/      (子聚合)
└── 新闻/Wiki/
    └── sources/    (~25)
```

**问题**：
1. 脚本（如 wiki-conflict-scanner.sh）必须处理两个 Wiki 根
2. 跨领域页面（"AI 应用"既属科技又属新闻）归属不清
3. 备份/迁移脚本必须双查双扫
4. 索引页分散（`图书馆/Wiki/index.md` + `新闻/Wiki/index.md`）

## 目标

```
知识库/wiki/
├── concepts/      # 所有概念
├── entities/      # 所有实体
├── sources/       # 所有原始资料摘要
├── syntheses/     # 所有综合
├── index.md       # 统一索引
└── _templates/    # 模板
```

## 迁移步骤（建议分 5 批）

### 第 1 批：仅迁移 sources/（新闻 → 图书馆合并）
- 风险：低（sources/ 是输出，不需要保持原链接）
- 工作量：~25 个 .md + 修 frontmatter 路径
- 命令：
  ```bash
  mv 知识库/新闻/Wiki/sources/*.md 知识库/图书馆/Wiki/sources/
  # 然后修每个文件的 frontmatter sources 路径
  ```

### 第 2 批：建立 `wiki/` 顶层
- 复制 `图书馆/Wiki/concepts/` + `entities/` + `syntheses/` → `wiki/`
- 用 `rsync` 或 `cp -r`

### 第 3 批：所有脚本路径改
- `wiki-deep-check.sh`
- `wiki-conflict-scanner.py`
- `wiki-auto-update.sh`
- `wiki-monthly-raw-scan.sh`
- 全部从 `图书馆/Wiki` + `新闻/Wiki` 改为 `wiki/`

### 第 4 批：删 `图书馆/Wiki` + `新闻/Wiki`（保留一个月兜底）
- 用 git tag 标记
- 一个月后没出问题再彻底删

### 第 5 批：检查 wiki/ 内部断链
- 跑 `wiki-conflict-scanner.sh` 看断链
- 修复

## 不迁移的内容

- `图书馆/Wiki/客房部/`——这是**子聚合**，跨多个 SOP——保留在原位
- `图书馆/Raw Sources/` 和 `新闻/Raw Sources/`——**不动**（snapshot 机制依赖这两个根）
- `_templates/`、`_taxonomy/`——已在正确位置

## 工作量估计

- 第 1 批：30 分钟
- 第 2 批：1 小时（复制 + 验证）
- 第 3 批：1 小时（修脚本）
- 第 4 批：5 分钟
- 第 5 批：1 小时

**总计 ~3.5 小时**——**建议**下一个空闲时段做。

## 风险

- 断链：迁移后**所有** `[[xxx]]` 双链需要重新解析——但 wiki-conflict-scanner 会捕获
- Git 历史：移动文件保留历史（git 会自动识别）
- 飞书消息里的链接：可能失效（链接是绝对路径）

## 不做的话

- 脚本继续双根扫描——**功能不受影响**——只是维护成本高
- 跨领域页面继续模糊——**实际使用不受影响**——只是分类学不完美

---

*创建于 2026-06-08*  
*状态：待定（主人有空再做）*
