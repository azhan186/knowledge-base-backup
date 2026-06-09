# LLM Wiki - Karpathy

> 来源：https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
> 作者：Andrej Karpathy

## 核心思想

LLM 不是每次查询时从原始文档重新发现知识，而是**增量构建和维护一个持久的 Wiki**——一个结构化的、相互链接的 Markdown 文件集合，介于你和原始资料之间。

关键区别：**Wiki 是一个持久的、累积的产物。** 交叉引用已经在那里了。矛盾已经被标记了。综合已经反映了你所读的一切。

## 三层架构（与本知识库相同）

1. **Raw Sources**：原始资料库，只读，Immutable
2. **Wiki**：LLM 生成和维护的 Markdown 文件集合
3. **Schema**：配置文件，告诉 LLM Wiki 的结构、约定和工作流程

## 三种操作

1. **Ingest**：将新资料加入 Raw，LLM 读取、提取、整合到 Wiki
2. **Query**：基于 Wiki 回答问题
3. **Lint**：定期检查 Wiki 健康度（矛盾、过时、孤立页面）

## 特殊文件

- **index.md**：内容导向，Wiki 的目录
- **log.md**：时间导向，添加-only 的操作记录

---
*存入时间：2026-05-12*