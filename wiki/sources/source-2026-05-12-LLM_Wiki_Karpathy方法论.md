---
title: "LLM Wiki Karpathy方法论：增量构建持久知识库"
type: source
subject: "870 图书情报"
tags: [LLM, 知识库, Wiki, Karpathy, 三层架构, Ingest, Query, Lint]
sources: [../../图书馆/Raw Sources/AI与科技/AI基础/2026-05-12_LLM_Wiki_Karpathy.md]
last_updated: 2026-06-11
date: 2026-05-12
---

# LLM Wiki Karpathy方法论：增量构建持久知识库

> 视角：Andrej Karpathy 提出的"LLM Wiki"理念核心——把 LLM 从"查询时重新发现知识"升级为"增量维护持久 Wiki"。

## 核心定义

**LLM Wiki**：介于你和原始资料之间的**持久的、累积的**结构化 Markdown 文件集合，由 LLM 持续增量构建和维护。

**关键区别**：
- 传统 RAG：每次查询时从原始文档重新发现知识
- LLM Wiki：交叉引用已经在那里、矛盾已经被标记、综合已经反映你所读的一切

> 本知识库（`/home/azhan186/open claw/知识库/`）就是 LLM Wiki 理念的具体实现。

## 三层架构

```
┌─────────────────────────────────┐
│ Layer 1: Raw Sources（原始资料）   │ ← 只读 Immutable
│   - 论文 PDF、网页剪藏、MD 笔记     │
├─────────────────────────────────┤
│ Layer 2: Wiki（知识库）           │ ← 可读写 LLM 维护
│   - concepts/entities/sources/     │
│   - syntheses（综合）            │
├─────────────────────────────────┤
│ Layer 3: Schema（规则文件）       │ ← 用户+LLM 共同维护
│   - 结构规范、命名约定、工作流程    │
└─────────────────────────────────┘
```

## 三种核心操作

| 操作 | 触发 | 产出 |
|------|------|------|
| **Ingest**（摄取）| Raw Sources 加入新资料 | LLM 读 → 提取 → 整合到 Wiki |
| **Query**（查询）| 用户提问 | 基于 Wiki 回答（带 [[双向链接]]）|
| **Lint**（健康度检查）| 定期 | 检查矛盾、过时、孤立页面 |

## 强制知识编译流水线

```
1. 增量扫描 → 识别新文件
2. 开始编译：
   a) 生成摘要 → wiki/sources/source-YYYY-MM-DD-主题.md
   b) 提取概念 → wiki/concepts/概念.md
   c) 提取实体 → wiki/entities/实体.md
   d) 建立 [[双向链接]] 关联
3. 更新索引：wiki/index.md
```

## 关键设计原则

### 1. 增量维护 vs 重新发现
- **优势**：知识积累、链接丰富、矛盾标记
- **代价**：需要持续维护、可能产生过时内容

### 2. 矛盾标注（[!warning]）
- 发现与已有知识冲突时显式标记
- 维护"知识妥协态"而非追求完美一致

### 3. 主动关联
- 编译新资料时主动思考：它和已有知识的关系？
- 用 [[Obsidian双向链接]] 建立网络

## 与传统 RAG 的对比

| 维度 | RAG | LLM Wiki |
|------|-----|---------|
| 知识存储 | 原始文档 | 结构化 Wiki |
| 检索时机 | 每次查询 | 已建立索引 |
| 知识更新 | 增删文档 | LLM 增量编译 |
| 矛盾处理 | 无 | 显式标注 |
| 跨资料综合 | 无 | 已综合 |

## 相关概念

- [[私人知识库对AI-Agent的影响]]（本知识库具体实现）
- [[三层架构]]（Raw Sources / Wiki / Schema）
- [[个人知识库对AI-Agent的影响]]
- [[知识库规范]]（本知识库的实施规范）

## 特殊文件约定

- `wiki/index.md`：内容导向目录
- `wiki/log.md`：添加-only 操作记录
- `_taxonomy/`：主题索引与迁移历史
- `_trash/`：删除文件备份（30 天清理）

---

*来源：[Karpathy Gist #442a6bf555914893e9891c11519de94f](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | 编译：2026-06-11*