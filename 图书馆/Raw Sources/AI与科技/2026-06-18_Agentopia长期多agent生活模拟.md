# Agentopia: Long-Term Life Simulation and Learning in Agent Societies

**日期：** 2026年6月18日
**分类：** AI与科技 / 人工智能 / 多智能体仿真
**来源：** arXiv:2606.07513（Xintao Wang 等，复旦大学，2026-06-05 提交，79 页）
**代码：** https://github.com/Neph0s/Agentopia
**本地 PDF：** `2026-06-18_Agentopia长期多agent生活模拟.pdf`（2.2 MB）
**全文文本：** `2026-06-18_Agentopia长期多agent生活模拟_全文.md`

---

## 一句话总结

让 100 个 LLM agent 在 3 个不同世界观里自主生活 **10 个模拟年**，用"life reward（人生奖励）"作为优化目标，用 rejection sampling 反向训练出更像人的 LLM（CoSER Test 提升 +15.6%）。

---

## 摘要（原文翻译）

人类通过社会生活学习。用 LLM agent 模拟这一过程是一个有前景的方向，自然引出一个问题：LLM 能否从模拟的社会经验中学习，更好地理解和复现人类行为？

然而，以往的 agent 社会仿真通常只能跑几天，限制了社交互动的深度和长期成长。本文研究 agent 社会中的长期人生仿真与 LLM 学习，目标是：
1. 探究终生仿真中涌现的社交行为
2. 通过多年模拟社会经验，发展 LLM 的人格化能力，特别是社交生活中的智能

我们提出 **Agentopia**——一个长期人生仿真的多 agent 社会框架，100 个 agent 在 **10 个模拟年**内自主追求个人成长、发展社交关系、满足需求和目标。我们定义 **life reward** 来镜像人类福祉，并用 rejection sampling 训练 LLM。

大量实验表明 agent 展现出丰富的涌现社交行为。life reward 训练有效增强底层 LLM，提升了仿真中的 agent 福祉，并在下游角色扮演 benchmark 上泛化提升 **+15.6%**。

---

## 核心贡献

1. **Agentopia 系统**：把人生仿真规模从"天"扩展到"年"，首次实现长期社交动态（个人成长、关系建立、人生规划）
2. **Life Reward 训练**：基于 life reward 在高优势 agent 经验上微调 LLM，**不依赖人类数据**
3. **广泛实验**：社交行为综合分析与案例研究；验证 life reward 训练提升仿真福祉和下游角色扮演能力

---

## 关键设计：Life Reward（三维）

| 维度 | 来源 | 计算方式 |
|------|------|----------|
| **Social Reward** | Warmth-Competence 模型（affection + respect） | 加权有向图 + Weighted PageRank + Mutual Affection Bonus |
| **Subjective Reward** | Maslow 需求层次（mood/material/social/esteem 四维 fulfillment） | 每周 fulfillment 加权 + 低于 25 百分位惩罚 |
| **Economy Reward** | 年度财务净增 | `deposit_end - deposit_start` |

总奖励 = `λ_social·z_social + λ_subj·z_subj + λ_econ·z_econ`（z-score 归一化后加权）

---

## 关键设计：Life Reward Training（rejection sampling）

挑战：长期 horizon 让 PPO/GRPO 不可行（单 agent 单年就要几百次 LLM 调用）。

**做法**：
1. **优势估计**：以 agent 自身上一年的归一化回报为基线 → `A_i,t = G^norm_i,t - G^norm_i,t-1`
   - **关键设计**：和自己比，不和别人比（避免偏向初始条件好的 agent）
2. **轨迹选择**：每周期选 top 25% advantage 的 agent，其所有轨迹进训练集
3. **质量过滤**：用 16 条 roleplay 原则过滤响应（anthropomorphism / character fidelity / reasonableness）
4. **防遗忘**：与 Tulu 3 自蒸馏数据 50:50 混合

---

## 三个仿真世界（100 agent × 10 年 / 世界）

| 世界 | 设置 | 强调 |
|------|------|------|
| **The Apartment** | 纽约合租公寓，年轻人/学生/艺术家 | 陌生人在共享空间自然形成社群 |
| **Arcane Academy** | 魔法学院，学生+教职工 | 结构化学术机构中的复杂关系 |
| **The Campus** | 中国高中（中文运行） | 校园社交网络形成与个人成长轨迹 |

---

## 主要实验结果

### 1. 仿真中涌现的社交行为
- 个人成长、关系建立、人生选择、社交网络分化
- 涌现类别：婚姻、友情、竞争、师徒、社交圈分化
- 三个世界展现**显著的跨世界分化**：制度性环境（The Campus）推动广泛人格成长；自主环境（The Apartment）产生多样个人策略；结构转变（Arcane Academy）破坏社交连续性

### 2. 训练后 agent 表现（Qwen3.5-397B-Agentopia vs Qwen3.5-397B）

| 维度 | 变化 | 含义 |
|------|------|------|
| Economy Reward | +2.5% | 理财更好 |
| Subjective Reward | +1.8% | 主观福祉更高 |
| **Respected By** | **+24.2%** | 被尊重的人数大幅上升 |
| **Liked By** | **+15.9%** | 被喜爱的人数上升 |
| Social Fulfillment | +9.7% | 社交满足感显著提升 |
| Mood / Esteem Fulfillment | +1.9% / +4.8% | 心情/自尊小幅提升 |
| Material Fulfillment | **−14.8%** | 因经济奖励激励储蓄而非消费 |
| Public Activity | +7.1% | 公共活动参与增多 |
| Solo Activity | −19.8% | 独处活动减少 |
| Skill Advances | **−29.6%** | 技能进步减少（被未被奖励的行为 deprioritize） |

### 3. 下游角色扮演 benchmark（CoSER Test）

| 模型 | Avg | Anthropomorphism | Character Fidelity |
|------|-----|------------------|---------------------|
| Claude 4.5-Opus | 62.43 | 64.28 | 58.45 |
| Gemini 3-Pro | 61.80 | 60.42 | 58.34 |
| **Qwen3.5-397B-Agentopia** | **49.16** | **49.67** | **46.93** |
| Claude 4.5-Sonnet | 45.21 | 36.02 | 47.55 |
| Qwen3.5-397B (baseline) | 42.51 | 40.16 | 40.32 |
| CoSER 70B | 35.95 | 31.16 | 32.28 |
| GPT-5 Mini | 32.97 | 24.60 | 27.20 |

- 相对 baseline **+15.6% overall**
- Anthropomorphism **+23.7%**（最大提升）
- Character Fidelity **+16.4%**
- **超过 Claude 4.5-Sonnet**

### 4. 计算成本（每世界 100 agent × 10 年）

| 世界 | 输入(M) | 输出(M) | 总 token(M) | LLM 调用(K) | 耗时(h) |
|------|---------|---------|-------------|-------------|---------|
| The Campus | 19,041 | 425 | 19,466 | 544 | 201.3 |
| Arcane Academy | 11,302 | 315 | 11,617 | 572 | 174.2 |
| The Apartment | 9,699 | 317 | 10,016 | 584 | 183.2 |
| **平均** | **13,347** | **352** | **13,700** | **567** | **186.2** |

- 3 个 FP8 Qwen3.5-397B 实例 / 仿真
- 输入远多于输出（每 agent context 重）
- 内存增长是主要瓶颈：每周期耗时 80→140 分钟（10 年累计）

---

## 训练硬件

- **30 节点 × 8 H100 80GB** GPU
- 1 epoch
- 学习率 `1×10^-5`
- 训练数据：3 世界前 4 年的仿真数据

---

## 限制（论文自陈）

1. **Turn-based 设计**：LLM 轮次生成 ≠ 人类实时感知；实时感知会消耗过多算力在底层操作上
2. **幻觉**：agent 可能捏造不存在的角色/地点（用上下文管理 + 位置系统 + 16 原则过滤缓解）
3. **环境与数值系统**：完全对齐真实人类社会极难
4. **对齐缺口**：
   - life reward 不一定完全对齐人类福祉
   - agent 社会 ≠ 人类社会：所有反馈来自其他 AI 模型，不是人类
5. **计算约束**：没跑更多世界/agent/时间；没尝试不同模型族；没做精细 credit assignment

---

## 核心创新点（主人视角提炼）

1. **规模跳跃**：从"几天"到"10 年"，让成长/规划/长期关系真正涌现
2. **奖励设计哲学**：life reward = Maslow + Warmth-Competence + PageRank，把心理学理论量化进奖励函数
3. **自基线优势**：不用 critic 也不用多次 rollout 估计基线，用 agent 自身去年表现做 baseline —— **这是面对长 horizon 仿真时 PPO/GRPO 不可行的工程化绕行**
4. **不依赖人类数据**：纯模拟自举训练，回应"人类数据耗尽"的未来担忧（silver2025era 引用）
5. **下游泛化**：在 Agentopia 内部优化的策略，能迁移到 CoSER 这种独立角色扮演 benchmark，**说明社会经验训练具有跨任务的可迁移性**

---

## 与主人知识库已有内容的关联

- **AI Agent 百科**（2026-05-27）：Agentopia 是 agent 系统的"学习型"代表
- **AI幻觉系列**：论文 §Limitations 显式承认 agent 幻觉问题
- **维度黎明 San 值体系**：本论文的 vitality / fulfillment 机制可作为科幻项目中"状态指标"的现实参考
- **基础常识优先规则**：论文的"不依赖人类数据"思路与个人知识库维护哲学相通 —— 都是用经验/上下文代替人工标注