---
title: "Agentopia：长期多 agent 生活仿真与训练"
type: source
subject: "520 计算机科学与技术"
tags: [AI, Agent, LLM, 多智能体, 社会仿真, 角色扮演, 强化学习, rejection sampling, Maslow, PageRank, 交叉学, 智能科学与技术, 人工智能 AI]
sources:
  - "../../图书馆/Raw Sources/AI与科技/2026-06-18_Agentopia长期多agent生活模拟.pdf"
  - "../../图书馆/Raw Sources/AI与科技/2026-06-18_Agentopia长期多agent生活模拟.md"
last_updated: 2026-06-18
---
L1-交叉学/L2-智能科学与技术/L3-人工智能 AI/L4-Agentopia长期多agent生活模拟

# Agentopia：长期多 agent 生活仿真与训练

> 来源：arXiv:2606.07513（Xintao Wang 等，复旦大学，2026-06-05 提交，79 页）
> 代码：https://github.com/Neph0s/Agentopia
> 一句话：100 个 LLM agent 在 3 个世界观里自主生活 **10 个模拟年**，用 life reward + rejection sampling 反向训练出更像人的 LLM（CoSER +15.6%）。

## TL;DR（30 秒读完）

- **问题**：以往 agent 社会仿真只能跑几天，长期社交动态涌现不出来；角色扮演训练又严重依赖人类数据
- **方案**：Agentopia 框架——100 agent × 3 世界 × **10 模拟年**；引入 **life reward**（social + subjective + economy 三维）；用 rejection sampling 选 top-25% advantage 轨迹微调 LLM
- **结果**：仿真中涌现真实社交行为；训练后 agent 在内部仿真福祉提升；**CoSER Test 角色扮演 benchmark 整体 +15.6%**，超过 Claude 4.5-Sonnet

## 一、为什么这件事重要

LLM 角色扮演的天花板：现在的训练数据快耗尽（silver2025era "era of experience"），单纯靠人类数据 scaling 已经不够。

论文的核心假设：**人类从社会生活学习**——那 LLM 是否也能通过在 agent 社会里"活过十年"来学会更像人？

前提：需要能跑**长期**仿真的环境 + 能量化"人生过得好不好"的奖励。

## 二、Agentopia 系统架构

### 2.1 时间结构

- **周** = 基本时间单位（每周末做 review）
- **年** = 大周期（年末：更新 profile / 申请新职业 / 计算 life reward）
- **十年** = 单次仿真长度

### 2.2 一周四阶段

| 阶段 | 做什么 |
|------|--------|
| **Plan** | agent 制定下周计划 + 选择生活水平 |
| **Contact** | 多轮配对通信，安排共同活动日程 |
| **Activity** | 执行活动（4 类：joint / solo / encounter / public） |
| **Review** | 反思并写入 weekly diary + 更新 memory files |

### 2.3 Agent 三层状态

1. **Profile**：背景、性格、天赋、初始职业/资产（每年更新一次）
2. **Social Relationships**：用 character 间互写的 memory file 表达关系（朋友/恋人/对手/陌生人统一表示，不预设类型）
3. **Dynamic States**：vitality（能量）+ fulfillment（Maslow 四维）+ skills + position + assets

### 2.4 长期记忆：File System Memory

每个 agent 维护三类文件：
- `general.txt` —— 个人笔记/计划
- `characters/<who>.txt` —— 对具体人的认知与关系
- `others/<name>.txt` —— 任意主题

通过 `read_file` / `update_file` / `list_files` 三个函数自主管理。
**关键约束**：写之前必须先读（read-before-write），避免覆盖式瞎写。

### 2.5 Environment Model（关键创新）

不是硬编码规则，而是用一个**无状态的 LLM**当"环境生成器"：
- 给 agent 反馈（活动是否可行、结果如何）
- 选下一个说话人（joint activity 中）
- 生成 public/encounter 活动
- 排名职业申请候选人
- 年度 profile 更新
- 过滤低质量响应

> 类比：environment model ≈ 游戏里的"GM"，但完全用 LLM 即兴演。

## 三、Life Reward（三维）⭐ 核心创新

### 3.1 Social Reward —— 社交地位

基于 **Warmth-Competence 模型**（Fiske 2007）：
- 让每个 agent 给社交圈里所有人评 **affection** 和 **respect**（0-100，告知评分私秘以避免迎合）
- 排序后 rescale 到 0-100
- 构建两个加权有向图
- 用 **Weighted PageRank** 计算每个 agent 的地位分数
- 加 **Mutual Affection Bonus**：被"我也在乎的人"在乎 → 权重放大

```python
S_i' = Σ w_ji · (1 + α · w_ij) · S_j  # 公式 1
r_social = ½ · S_aff' + ½ · S_resp'
```

### 3.2 Subjective Reward —— 主观福祉

基于 **Maslow 需求层次**，4 维 fulfillment：
- mood（情绪）
- material（物质）
- social（社交）
- esteem（自尊）

按 **hedonic adaptation**（享乐适应）理论，每周边际衰减。

**惩罚机制**：任何维度低于当周 25 百分位 → 扣分；vitality 低也独立扣分。

```python
r_subj = (Σ f_{w,d} - n_p · λ_p) / (n_w · D)  # 公式 2
```

### 3.3 Economy Reward —— 经济

```python
r_econ = deposit_end - deposit_start
```

### 3.4 总奖励

```python
r = λ_social · z_social + λ_subj · z_subj + λ_econ · z_econ  # 公式 3
```
三个维度独立 z-score 归一化后再加权。

## 四、Life Reward Training（rejection sampling）

### 4.1 为什么不用 PPO/GRPO？

- 长期 horizon：单 agent 单年几百次 LLM 调用 → PPO 不可行
- 单轨迹：每个 agent 只产生一条人生轨迹 → GRPO 无法多次 rollout 求基线

### 4.2 关键设计：自基线

```python
A_i,t = G^norm_i,t - G^norm_i,t-1  # 与自己去年比
```

**为什么这样设计**：
- 避免偏向初始条件好的 agent
- 衡量"进步"而非"绝对水平"
- 选出的高优势轨迹 → 多元人格都能受益，不会塌缩成单一行为模式

### 4.3 训练数据流

1. 在每个奖励周期内选 top 25% advantage 的 agent
2. 该 agent 在该周期内的**所有**轨迹进训练集
3. 16 条 roleplay 原则过滤低质量响应
4. 与 Tulu 3 自蒸馏数据 50:50 混合（防灾难性遗忘）

### 4.4 训练规模

- 30 节点 × 8 H100 80GB
- 1 epoch，lr = 1e-5
- 训练数据：3 世界前 4 年的仿真
- 评估：4 年仿真（The Campus + The Apartment）+ CoSER Test

## 五、关键实验结果

### 5.1 涌现行为（3 世界 10 年）

涌现类别：婚姻、友情、竞争、师徒、社交圈分化、人生规划。

**跨世界分化**：
- **The Campus（制度环境）**：广泛人格成长
- **The Apartment（自主环境）**：多样个人策略
- **Arcane Academy（结构转变）**：破坏社交连续性

### 5.2 训练后 agent 内部表现（vs baseline）

| 指标 | Δ | 解读 |
|------|---|------|
| Economy Reward | +2.5% | 理财更好 |
| Subjective Reward | +1.8% | 主观福祉略升 |
| **Respected By** | **+24.2%** | 显著受尊重 |
| **Liked By** | **+15.9%** | 显著受欢迎 |
| Mood Fulfillment | +1.9% | 心情微升 |
| Social Fulfillment | +9.7% | 社交满足显著升 |
| Esteem Fulfillment | +4.8% | 自尊微升 |
| **Material Fulfillment** | **−14.8%** | 因奖励激励储蓄而非消费 |
| Public Activity | +7.1% | 公共活动增 |
| Solo Activity | −19.8% | 独处减 |
| Skill Advances | **−29.6%** | 技能进步大幅减（未被奖励的行为被 deprioritize） |

> **关键洞察**：reward shaping 真实地重塑了行为分布。被奖励的行为增，未被奖励的行为减（即使是"好"的技能学习也被 deprioritize，因为 skill 进步没直接进 reward）。这暴露了 reward shaping 的局限。

### 5.3 下游 benchmark：CoSER Test

| 模型 | Avg | Anthropomorphism | Character Fidelity |
|------|-----|------------------|---------------------|
| Claude 4.5-Opus | 62.43 | 64.28 | 58.45 |
| Gemini 3-Pro | 61.80 | 60.42 | 58.34 |
| **Qwen3.5-397B-Agentopia** | **49.16** | **49.67** | **46.93** |
| Claude 4.5-Sonnet | 45.21 | 36.02 | 47.55 |
| Qwen3.5-397B baseline | 42.51 | 40.16 | 40.32 |
| CoSER 70B | 35.95 | 31.16 | 32.28 |
| GPT-5 Mini | 32.97 | 24.60 | 27.20 |

- 整体 **+15.6%** over baseline
- Anthropomorphism **+23.7%**（最大提升）
- Character Fidelity **+16.4%**
- **超过 Claude 4.5-Sonnet**

### 5.4 计算成本（每世界 100 agent × 10 年）

| 世界 | 输入(M) | 输出(M) | 总 token(M) | 调用(K) | 耗时(h) |
|------|---------|---------|-------------|---------|---------|
| The Campus | 19,041 | 425 | 19,466 | 544 | 201.3 |
| Arcane Academy | 11,302 | 315 | 11,617 | 572 | 174.2 |
| The Apartment | 9,699 | 317 | 10,016 | 584 | 183.2 |
| **平均** | **13,347** | **352** | **13,700** | **567** | **186.2** |

- 3 个 FP8 Qwen3.5-397B 实例
- 输入 ≫ 输出（每个 agent context 很重）
- **每周期耗时 80→140 分钟**（10 年内）：记忆增长是主要瓶颈

## 六、局限性（论文自陈）

1. **Turn-based ≠ 实时人类感知**；实时感知会消耗过多算力在底层操作
2. **幻觉**：agent 可能捏造不存在的角色/地点（context 管理 + location 系统 + 16 原则过滤缓解）
3. **环境/数值系统对齐真实社会极难**
4. **对齐缺口**：
   - life reward 不完全对齐真实人类福祉
   - agent 社会 ≠ 人类社会：所有反馈来自其他 AI
5. **计算约束**：没跑更多世界/agent/时长/模型族；没尝试 fine-grained credit assignment

## 七、对主人的意义

### 7.1 与知识库已有内容的关联

- [[AI Agent百科]]（2026-05-27）：Agentopia 是 agent 系统的"学习型/长期自主"代表
- [[AI幻觉]]：论文 §Limitations 显式承认 agent 幻觉问题
- [[维度黎明 San 值体系]]：本论文的 vitality + 4 维 fulfillment 机制可作为科幻项目"状态指标"的设计参考（San 值也是 Maslow 式分层）

### 7.2 可借鉴的方法论

1. **量化的"人生奖励"**：Maslow + Warmth-Competence + PageRank —— 把抽象的"过得好不好"工程化为可计算的 reward
2. **自基线 advantage**：不用 critic 也不用多次 rollout，用"和自己去年比"绕过 PPO/GRPO 的不可行性
3. **不依赖人类数据**：回应 silver2025era 的 "era of experience" 论点——当人类数据耗尽，**agent 社会经验可作为新训练源**
4. **跨任务泛化**：在 Agentopia 内部优化的策略，能迁移到独立的 CoSER Test，**说明社会经验训练具有跨任务的迁移性**

### 7.3 主人潜在的应用场景

- **《维度黎明》角色系统设计**：agent 状态的量化（vitality/fulfillment/技能/资产/关系）可直接映射到角色指标
- **个人知识库维护哲学**：论文的"不依赖人类标注数据"思路，与知识库 v2.1 规范的"AI 自举编译"哲学相通

## 八、相关引用（论文内提及）

- park2023generative —— Generative Agents（25 agent × 2 天）
- wang2023humanoid —— Humanoid Agents（引入 Maslow）
- altera2024projectsid —— Project Sid（Minecraft 中 50 agent）
- fan2026aivilization —— Aivilization（生产经济仿真）
- wang2025coser —— CoSER（角色扮演 benchmark，本论文下游评估）
- silver2025era —— "Era of Experience"
- maslow1943theory —— Maslow 需求层次
- fiske2007universal —— Warmth-Competence 模型
- page1999pagerank —— PageRank

## 相关翻译

- [[../../../图书馆/Raw Sources/AI与科技/2026-06-18_Agentopia长期多agent生活模拟_中文翻译]] — 全文中文翻译（§1-6 + Appendix A-E，178KB，2026-06-18 由 5 个并行子代理完成）

## 更新记录

- 2026-06-18：初建，从 arXiv:2606.07513（v1，2026-06-05 提交）摘要 + §1-6 + §A-E 蒸馏
- 2026-06-18：补充全文中文翻译链接（5 子代理并行）