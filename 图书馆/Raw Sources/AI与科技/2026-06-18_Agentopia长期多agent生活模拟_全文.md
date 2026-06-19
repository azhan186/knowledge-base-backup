

Agentopia: Long-Term Life Simulation and Learning in Agent Societies

 
 
 Report GitHub Issue
 ×
 

 
 Title:
 

 Content selection saved. Describe the issue below:

 Description:
 
 

 
 Submit without GitHub
 Submit in GitHub
 
 

 
 
 
 Back to arXiv
 
 

 
 
 Why HTML?
 
 
 Report Issue
 
 
 
 Back to Abstract
 
 
 
 
 Download PDF
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

Abstract

1 Introduction

2 Related Work

Agent-based Social Simulation

Persona Simulation and LLM Role-Playing

3 Agentopia

3.1 Agent Design

3.2 Simulation Procedure

3.3 Contact & Scheduling

Actions

Schedule Resolution

Scheduling Public and Encounter Activities

3.4 Activities

3.5 Environment Design

Environment Model

Economy System

Position System

Location System

4 Reward and Optimization

4.1 Life Reward

Social Reward

Subjective Reward

Economy Reward

Total Reward

4.2 Life Reward Training

Estimating Returns and Advantages

Trajectory Selection

Response Filtering

5 Experiments

5.1 Experimental Setup

World Data

Simulation

Models

Metrics

5.2 Analysis of Long-Term Social Simulation

Reward Analysis

Reward–Behavior Correlation

5.3 Training via Life Rewards

Training

Learning via life rewards improves agent performance in social simulation

Life reward training generalizes to role-playing ability

5.4 Computational Cost

6 Conclusion

Turn-based design

Hallucination

Environment and numeric systems

Optimization and alignment

Computational constraints

References

A World and Character Creation

A.1 Pipeline Overview

Step 1: World Setting

Step 2: Reference Story Selection

Step 3: Incremental Character Generation

Step 4: Attribute Assignment

Step 5: Consistency Verification

A.2 Details of Character Data and Memory System

B System Design Details

B.1 Design Philosophy of the Simulation Procedure

Activity Simulation

Communication Simulation

Synchronous vs. Asynchronous Design

B.2 Details of Simulation Procedure

Weekly Settlement (Before Plan)

Plan

Before Contact: Public Activity Generation and Sign-up

Contact

After Contact: Encounter Activity Generation

Activity

Review

Weekly Cleanup

Year-End Settlement

B.3 Details of Contact Stage

Contact Rounds

Error Feedback Mechanism

Action Types and Format

Schedule Resolution

B.4 Details of Joint Activities

Enter Activity

Turn Control

Visibility Tags

Gift System

Early Exit

Exit Activity (Reflection)

B.5 Details of Solo Activity

B.6 Details of Encounter Activity

B.7 Details of Public Activity

B.8 Details of Context Management

Function Calling Loop

Compacted Reasoning

B.9 Response Filtering and Roleplay Principles

B.10 Fulfillment and Vitality

Fulfillment

Vitality

B.11 Profile Update

B.12 Details of Economy System

Income

Expenses

B.13 Details of Position and Position Application

Position Attributes

Position Creation

Position Application Process

B.14 Location System

Public Locations

Private Locations

Location Selection

B.15 Numeric System

Personality Traits

Talents

Skills

Agent States

B.16 Concurrency Control

B.17 Configuration Parameters

C Experiment Settings

C.1 Training via Life Rewards

Return Normalization

Per-Period Trajectory Selection

C.2 CoSER Evaluation

C.3 Metrics Definition

Fulfillment Metrics

Activity Metrics

Contact Metrics

Personal Growth Metrics

Social Evaluation Metrics

Computational Cost Metrics

D Additional Results

D.1 Training via Life Rewards: Detailed Trends

Qwen3.5-397B-Agentopia’s advantage emerges over the long term

Economy–fulfillment trade-off

Subjective reward: material fulfillment masks underlying gains

D.2 Per-World Reward Distributions

D.3 Reward–Behavior Correlation Details

Social Reward

Subjective Reward

Economy Reward

Cross-World Consistency

D.4 Friendship Distribution

D.5 Social Network Visualization

D.6 Inter-Component Reward Correlation

D.7 Wealth Inequality and Social Mobility

Wealth Inequality

Social Mobility

D.8 Reward Quartile Behavioral Profiles

Social Reward

Subjective Reward

Economy Reward

D.9 Striving vs. Leisurely Agent Profiles

Key findings

D.10 Cross-World Divergence Analysis

The Campus: institutional scaffolding drives broad personality growth

The Apartment: autonomy produces diverse individual strategies

Arcane Academy: structural transitions disrupt social continuity

Summary

D.11 Model Comparison

Adjusted social reward

Analysis

Per-world breakdowns

D.12 Computational Cost Details

E Case Studies

E.1 Behavioral Cases

Planning

Contact

Activity Proposals

Responses to Proposals

Solo Activities

Joint Activities

Weekly Review

Social Evaluation

Career Transitions

Economic Decisions

Activity Management

Memory

Emergent Phenomena

E.2 Long-term Case Studies

Personal growth and transformation (Cases 1–3)

Relationship evolution and social metrics (Cases 4–6)

Economic behavior and resource management (Cases 7–9)

F System Prompts

 
 License: CC BY-NC-ND 4.0
 
 
arXiv:2606.07513v1 [cs.CL] 05 Jun 2026

\correspondingauthor
Corresponding author: xtwang21@m.fudan.edu.cn

Agentopia: Long-Term Life Simulation and Learning in Agent Societies

Xintao Wang

Fudan University

Sirui Zheng

Independent Researcher

Hongqiu Wu

Independent Researcher

Weiyuan Li

Fudan University

Jen-tse Huang

Johns Hopkins University

Minghao Zhu

Independent Researcher

Can Zu

Independent Researcher

Qi Deng

Independent Researcher

Jiawei Wang

University of Science and Technology of China

Qianyu He

Fudan University

Heng Wang

Independent Researcher

Xiaojian Wu

Independent Researcher

Yunzhe Tao

Independent Researcher

Abstract
Abstract: Humans learn from social life.
Simulating this process with LLM-powered agents represents a promising research direction, raising a natural question: whether LLMs can learn from such simulated social experience to better understand and replicate human behavior.
However, prior agent society simulations typically operate at the scale of days, limiting the depth of social interactions and long-term growth.
In this paper, we study long-term life simulation and LLM learning in agent societies, with two goals:
(1) investigating social behaviors that emerge from life-long simulation, and
(2) developing anthropomorphic capabilities in LLMs, particularly intelligence in social life, through years of simulated social experience.
Specifically, we present Agentopia, a comprehensive framework for long-term life simulation in multi-agent societies, where 100 agents autonomously pursue personal growth, develop social relationships, and fulfill their needs and goals over 10 simulated years.
We define life reward to mirror human well-being, and leverage this reward to train LLMs via rejection sampling.
Extensive experiments show that agents exhibit rich emergent social behaviors.
Furthermore, life reward training effectively enhances the underlying LLM,
which leads to improved agent well-being in simulation,
and generalizes to downstream role-playing benchmarks with +15.6% improvement.
Our code is available at https://github.com/Neph0s/Agentopia.

Figure 1: Illustration of emergent behaviors observed in Agentopia simulations.
Each scene depicts a real behavioral pattern documented in our case studies (Tables 22–34).
Without explicit scripting, agents autonomously develop diverse behavioral patterns reflecting agents’ intelligence in social life.

1 Introduction

Humans learn from social environments [vygotsky1978mind], and large language models (LLMs) learn from humans.
As LLMs advance, how to better understand and simulate human thought, emotion, and behavioral patterns has become an important research problem, which is known as LLM-based persona simulation, or role-playing [chen2024from].
LLM role-playing is widely adopted in AI companions, digital games, and content creation [shao2023character, zhou2023characterglm], such as Whispers from the Star. 111https://wfts.anuttacon.com/
However, faithfully aligning LLMs with human mind remains a challenge.
As human data approaches exhaustion,
future AI agents need to learn primarily through experience [silver2025era].
This motivates a straightforward idea:
since humans learn and grow through social lives in human societies [maslow1943theory],
can agents do the same — learning, growing, and becoming more human-like through lives in agent societies?
This requires building an agent society
that supports long-term life simulation,
encourages social behaviors such as growth, competition, intimate relationships, and resource allocation,
and provides rewards that mirror human well-being for optimization.

Prior work has studied LLM-based social simulation and persona simulation in short-term settings.
For social simulation,
previous efforts have built prototypes of agent societies,
e.g., Generative Agents [park2023generative] and Aivilization [fan2026aivilization].
However, these works primarily focus on low-level operations
such as “collecting 2 wheat to craft 1 flour”,
instead of long-term social dynamics, keeping simulations at the scale of days.
For persona simulation,
existing efforts focuses on role-playing within individual conversations [chen2024from, shao2023character],
emphasizing anthropomorphism, character fidelity, and user engagement,
rather than life simulation of agents themselves.
These methods rely heavily on human data for optimization [wang2025coser, liu-etal-2025-cogdual, du2026her], which is costly to collect and difficult to scale up, and thus remain insufficient to deeply align LLMs with human cognition.
Overall, existing research only study simulation at the scale of days or single conversations,
leaving long-term life simulation unexplored.

In this paper, we present Agentopia,
a framework for long-term life simulation in multi-agent societies,
where agents autonomously simulate years of human social lives, as illustrated in Figure 2.

In Agentopia, agents build social relationships,
develop personal skills,
set and accomplish goals,
develop and fulfill needs,
and engage in economic activities.
Agentopia focuses on social interactions rather than low-level operations.
The framework is characterized by several key features:
(1) Agentopia defines life reward to model human well-being,
representing social standing, subjective fulfillment, and economic status.
(2) Agentopia employs an environment model to serve as a generative environment engine that orchestrates the simulation,
avoiding the need to hard-code massive rules.
It serves multiple purposes including
verifying agent responses against role-playing principles,
providing feedback on agent behaviors, and creating and scheduling events.
(3) Agentopia implements a comprehensive context management mechanism to provide agents with sufficient context, and equips agents with memory files, a file-system-based long-term memory that agents autonomously manage what to remember, update, or discard.
Furthermore, leveraging simulation and reward in Agentopia, we propose life reward training optimize LLMs via rejection sampling,
improving LLMs in anthropomorphism, role-playing ability, and intelligence in social life.

Towards long-term life simulation,
Agentopia introduces a carefully designed simulation procedure.
It aims to model as many real-world social interactions as possible within a unified framework.
The core challenge is that LLMs generate by turns,
while humans can perceive and act at any time.
Hence, we structure time into discrete units, allowing concurrent yet ordered interactions.
Agentopia uses the week as its basic time unit.
Each week consists of four stages:
(1) Plan,
(2) Contact others and arrange schedules,
(3) carry out solo or group Activity over subsequent days,
and (4) Review the week’s experiences.
The year serves as a larger cycle.
At the end of each year,
Agentopia updates agents’ profiles ,
allows agents to apply for new careers,
and calculates life rewards for them.

To validate this framework,
we create three diverse fictional worlds and conduct simulations.
Each world contains 100 agents running for 10 simulated years.
This scale is orders of magnitude larger than prior studies.
We conduct multi-faceted analyses of these simulations,
such as reward and behavior analysis,
social relationship evolution,
and social mobility.
We also conduct extensive case studies to observe emergent behaviors in agent societies, as shown in Figure 1.
Besides, we use Agentopia as an arena to compare different models’ performance.
Subsequently, we demonstrate the effectiveness of life reward training.
The trained model demonstrates improved overall well-being in simulation,
including improved social relationships, higher subjective fulfillment, and better economic gains.
Furthermore, the improvements generalize to enhanced anthropomorphism and role-playing ability,
achieving +15.6% performance gain on CoSER Test [wang2025coser], a downstream role-playing benchmark.

Our contributions are summarized as follows:

1. 

We introduce Agentopia, a system for long-term life simulation in agent societies.
Compared to prior work,
Agentopia extends the scale of life simulation from days to years for the first time,
enabling long-term social dynamics
such as personal growth, relationship building, life planning, and, e.t.c.

2. 

Based on Agentopia, we define life reward to mirror human well-being, and propose life reward training that fine-tunes LLMs on high-advantage agent experiences, without relying on human data.

3. 

We conduct extensive experiments on Agentopia,
including comprehensive analyses and case studies on agents’ social behaviors.
We also validate the effectiveness of life reward training,
which improves in-simulation well-being
as well as anthropomorphism and role-playing ability in downstream evaluation.

Figure 2: Overview of Agentopia: world and character construction (§ A), role-playing agent (§ 3.1), life simulation in agent society (§ 3.2), and life reward training (§ 4.2).

2 Related Work

Agent-based Social Simulation

Recent work has explored LLM-powered agents for social simulation.
Generative Agents [park2023generative] pioneers this direction by simulating a society of 25 agents for two days,
observing emergent social behaviors such as organizing a party.
Humanoid Agents [wang2023humanoid] extends this by incorporating human needs inspired by Maslow’s hierarchy of needs [maslow1943theory].
Project Sid [altera2024projectsid] grounds agents in an established digital game environment, Minecraft,
showing emergent specialization, collective rule formation, and cultural transmission.
BookWorld [ran-etal-2025-bookworld] constructs multi-agent systems from fictional works,
enabling story generation through character interactions.
Aivilization [fan2026aivilization] designs a game environment to simulate agents’ production and economic behaviors.
CAMEL [li2024camel] investigates role-playing multi-agent systems for collaborative problem-solving in mathematics and coding tasks.
However, existing systems such as Aivilization face limitations in enabling long-term life simulation, where most LLM calls are spent on low-level operations, i.e., “physical” interactions within the virtual environment (e.g., picking up a bottle and moving between locations), rather than long-term social interactions between agents.
Table 1 provides a systematic comparison of these systems across key dimensions.

Table 1: Comparison of Agentopia and existing agent society systems.
“Time Scale” denotes the temporal scope of a simulation run.
“Env. FB” indicates whether environmental feedback is rule-based or LLM-generated.
“Econ. Sys.” denotes whether the system includes items and economic mechanisms.
“Career Sys.” refers to whether agents can choose and change occupations over time.
“Group Interact” means the system supports interactions among more than two agents.
Project Sid’s numbers are from Section 4.2 of its paper.

Gen. Agents
Humanoid
Project Sid
BookWorld
Aivilization
Agentopia

[park2023generative]
[wang2023humanoid]
[altera2024projectsid]
[ran-etal-2025-bookworld]
[fan2026aivilization]
(ours)

Time Scale
Days
Days
Days
—
Weeks
Years

Num. Agents
25
—
50
—

∼{\sim}10,000

100

Action Space
Predefined
Predefined
Predefined
Free-form
Predefined
Free-form

Env. FB
Rule
Rule
Rule
LLM
Rule
LLM

Memory
Retrieval
Retrieval
Retrieval
Retrieval
Fixed Scratchpad
File-based

Skill Growth
✗
✗
✗
✗
✓
✓

Econ. Sys.
✗
✗
✓
✗
✓
✓

Career Sys.
✗
✗
✓
✗
✓
✓

Group Interact
✓
✗
✓
✓
✗
✓

Reward
✗
✗
✗
✗
✓
✓

Training
✗
✗
✗
✗
✗
✓

Persona Simulation and LLM Role-Playing

This line of research aims to improve LLMs’ anthropomorphism and role-playing ability [chen2024from].
shanahan2023role argue that LLMs are inherently role-playing,
whether acting as general assistants or portraying specific characters.
wang2025coser propose that training on diverse characters enables LLMs to generalize anthropomorphic abilities,
bridging persona simulation and role-playing research.
Prior studies focus on data, evaluation, and optimization:
For data,
Character-LLM [shao2023character] and RoleLLM [wang2023rolellm] apply LLMs to synthesize character-specific question-answer data.
CoSER [wang2025coser] extracts authentic character data from literary corpora,
obtaining large-scale, high-quality role-playing datasets.
For evaluation,
previous studies primarily employ LLM judges [wang2023rolellm, tu2024charactereval]
and introduce rubrics aligned with human preferences [wang2025coser, du2026her].
Additionally, RoleEval [shen2023roleeval], InCharacter [wang2024incharacter],
and LifeChoice [xu2024character]
evaluate LLMs objectively from the perspectives of knowledge, personality, and decision-making, respectively.
For optimization,
prior research applies supervised fine-tuning with human data [wang2025coser, zhou2023characterglm]
or synthetic data [chan2024personahub, lu2024large]
CogDual [liu-etal-2025-cogdual], CPO [ye-etal-2025-cpo], and HER [du2026her]
explore reinforcement learning for role-playing,
where obtaining high-quality, human-aligned reward signals remains a key challenge.
Besides, Persona Vector [chen2025persona], Assistant Axis [lu2026assistant],
and Emotion Concepts [sofroniew2026emotion]
explore the internal mechanisms of persona and emotion in LLMs,
proposing methods for detection and manipulation.

3 Agentopia

This section presents the design of Agentopia,
a unified framework for long-term life simulation in agent societies.
The framework is organized around three core concepts: the simulation procedure, the agent, and the environment model:
(1) For the simulation procedure, agents live through weekly cycles, each consisting of four stages: Plan, Contact, Activity, and Review, which jointly support diverse social behaviors.
(2) For the agent, the core challenge is context management, i.e., providing each LLM with sufficient context including the character’s persona, states, relationships, and memories.
Agents’ long-term memory is implemented as a file system that agents autonomously manage via function calls.
(3) To orchestrate the simulation, Agentopia introduces the environment model, a separate LLM that organizes events, provides environmental feedback, and drives the simulation forward, replacing hard-coded rules.
We describe agent design in § 3.1,
the simulation procedure in § 3.2,
contact and scheduling in § 3.3,
activities in § 3.4,
and environment design in § 3.5.

3.1 Agent Design

In Agentopia, each agent role-plays as a specific persona, which comprises a profile, social relationships, and dynamic states, comprehensively representing the character.

1. 

Profile:
The profile stores an agent’s identity information, including a background story, personality traits, talents, as well as initial values for positions and assets.
These attributes remain relatively stable during simulation and are only updated once per simulated year.
The full profile schema is provided in § A.2, and the character creation process is described in § A.

2. 

Social Relationships:
In Agentopia, relationships are modeled entirely via inter-character memory.
We do not explicitly define or store character relationships.
Instead, relationships are represented through each character’s memory of the other, stored as free text and autonomously managed by agents.
This design uniformly represents friends, lovers, strangers, rivals, and other relationship types without requiring separate mechanisms.
Relationships can be unidirectional and expanded through multi-person activities.
The relationship network is initialized during world creation (§ A) and subsequently managed autonomously by agents.

3. 

Dynamic States:
Dynamic states represent an agent’s current life conditions and evolve with activities.
They include vitality, fulfillment, skills, position, and assets.
Vitality represents energy level.
Fulfillment is based on Maslow’s hierarchy of needs [maslow1943theory], which captures agents’ subjective satisfaction from four dimensions: mood, material, social, and esteem.
It serves as the basis for subjective rewards.
Following hedonic adaptation theory [Headey2014], fulfillment decays naturally each week.
Fulfillment and vitality changes are determined by the environment model based on activity content, rather than hard-coded rules.
The details are provided in § B.10.
Skills represent an agent’s acquired abilities.
Position represents an agent’s current occupation, which provides weekly income and skill growth (§ B.13).
Assets consist of a deposit and a list of possessions (§ B.12).

Besides, Agentopia carefully designs a context management mechanism to provide agents with sufficient context across stages, and equips agents with memory files as long-term memory that agents autonomously manage.
Together, Agentopia provides rich context for LLMs to simulate human social lives.

1. 

Context Management:
Agentopia carefully designs a comprehensive context management mechanism to provide agents’ underlying LLMs with sufficient information to simulate human social lives.
This is achieved through three context layers:
(1) Roleplay prompt: provides the foundational role-playing information shared across all stages.
It contains the agent’s full persona, recent weekly diaries as short-term memory, summaries of key memory files as long-term memory, worldview rules and role-play principles, e.t.c.,
enabling agents to correctly accumulate memory across stages and weeks throughout the simulation.
(2) Stage prompt: provides stage-specific instructions and context, e.g., scheduling rules and communication history for the Contact stage.
(3) Message history: records LLMs’ multi-turn messages accumulated within the current stage, including prior dialogues, calls and results of memory functions, and compacted reasoning process.
Together, these three layers combine automatic and agent-driven context management, providing comprehensive context for agents to simulate human social lives.
The details are elaborated in § B.8.

2. 

Memory Files:
While weekly diaries serve as short-term memory by recording recent experiences, memory files provide agents with long-term memory, a file-system-based persistent store that agents autonomously manage via function calls.
Agents decide what to remember, update, or discard, giving them full control over what persists across weeks and years.
Each agent maintains memory files in three categories:
general.txt for personal notes and plans,
characters/<who>.txt for the agent’s knowledge of and relationship with specific people,
and others/<name>.txt for any other topics.
Memory files provide context to LLMs in two ways: (1)
summaries of recently accessed files are automatically included in the roleplay prompt,
and (2) agents autonomously retrieve full content on demand, included in the message history.
Agents manage these files through three functions: read_file to retrieve content, update_file to write new content, and list_files to list all files.
A read-before-write constraint is enforced: an update is only permitted after the agent has read the target file in the same invocation, ensuring updates build upon existing content rather than overwriting blindly.
Agents can also create new files for topics they wish to track.

3.2 Simulation Procedure

A fundamental constraint of LLM-based agents is that they generate responses turn by turn:
they receive a complete context and produce a single reply, unlike humans who continuously perceive and react in real time (e.g., interrupting a conversation mid-sentence).
The simulation procedure must therefore be designed around turn-based interaction.
Meanwhile, Agentopia focuses on abstract social interactions (e.g., planning, socializing, decision-making) rather than low-level operations (e.g., movement, object manipulation).
This abstraction enables the system to model richer social behaviors with fewer LLM calls, achieving higher token efficiency for long-term simulation.

With these considerations, we design a comprehensive simulation procedure.
Agentopia uses the week as its basic time unit.
A simulated year spans nwn_{w} weeks; year-end triggers profile updates, position application, and life reward calculation. 222The day, week, and year in Agentopia serve as three hierarchical layers of abstract simulation time.
They are designed to simulate human life cycles at comparable scales, without strictly corresponding to real-world calendar units.
Each week consists of four stages: Plan, Contact, Activity, and Review.

1. 

Plan:
Based on memory and current state, each agent makes a weekly plan.
Agents are able to review previous plans and store or update new ones through function calls (e.g., read_file, update_file).
Agents also select an abstract consumption level (i.e., living standard) for the week, which abstracts their monetary spending and influences material fulfillment.

2. 

Contact (& Scheduling):
In this stage, agents communicate with each other over multiple rounds.
One primary purpose of communication is to arrange shared schedules: agents can propose invitations, which others may accept or decline, thereby creating joint activity schedules.
The detailed mechanism is introduced in § 3.3.

3. 

Activity:
In this stage, agents carry out diverse activities.
Each weekly cycle contains ndn_{d} active days, and on each day, every agent carries out exactly one activity.
Activities fall into four types: joint, solo, encounter, and public.
Through these activities, agents can pursue personal growth, work, or leisure on their own, or engage with others in shared experiences.
Activity types and execution are detailed in § 3.4.

4. 

Review:
At the end of each week, agents reflect on their weekly experiences and summarize them into a weekly diary.
Based on this reflection, agents can update their memory files via function calls.
The weekly diaries are included in each agent’s context in subsequent weeks, allowing agents to recall their past experiences.

At the end of each simulated year, three processes take place.
(1) Profile Update: the environment model makes incremental updates to each agent’s profile (e.g., personality traits, talents) based on their accumulated experiences over the year.
(2) Position Application: agents may apply for new positions based on their preferences and compete for limited vacancy based on their abilities and skills.
(3) Life Reward Calculation: life rewards are calculated, measuring each agent’s social standing, subjective fulfillment, and economic status over the past year.

3.3 Contact & Scheduling

The Contact stage serves two purposes: communication between agents and scheduling of activities.
Communication is restricted to pairwise exchanges, while multi-person conversations are deferred to joint activities.
Constrained by the turn-based nature of LLM generation, communication in Agentopia proceeds in rounds.
Each week consists of ncn_{c} contact rounds.
In each round, an agent receives newly arrived messages along with the contact history from the past three weeks, then decides whom to contact and what actions to take.
After all rounds conclude, the system resolves the contact history to determine which joint activities have been successfully created.

Actions

In Agentopia, agents must generate actions to trigger real communication and scheduling.
Actions are wrapped with <role_action> tags in agents’ responses, which the system then parses and executes.
They are different from function calls.
Four action types are available: contact, propose_joint_activity, respond_invitation and cancel_joint_activity (§ B.3).

Schedule Resolution

After all contact rounds conclude, the system resolves which joint activities are successfully created based on all collected actions.
The process handles cancellations, deduplicates responses, resolves time conflicts, and checks creation condition.
The full rules and procedure are described in § B.2.

Scheduling Public and Encounter Activities

Public and encounter activities are scheduled in dedicated stages before and after Contact, respectively.
Before Contact, the environment model creates public events for the upcoming weeks, and agents sign up for those that match their interests.
After Contact, the environment model arranges encounter activities to create chance meetings for idle agents, i.e., those without any scheduled activity on a given day.

3.4 Activities

Activities are the core stage of Agentopia, where agents carry out activities and develop abilities, fulfillment, wealth, and social relationships.
Agentopia supports four activity types: joint, solo, encounter, and public.
Agents carry out activities according to their schedules, defaulting to solo activities when unscheduled.
After each activity, the environment model provides feedback based on the agent’s experience (including state changes), and the agent reflects on the outcome and may update its memory files accordingly.
The four activity types are described below:

1. 

Joint Activity:
Joint activities model multi-agent, multi-turn interactions.
They are created through invitation and negotiation during the Contact stage.
Participants take turns speaking; following wang2025coser, we employ the environment model to provide environmental descriptions and select the next speaker each turn.
Agents can choose the visibility of their generated content, using special tags to mark each segment as public, private, or selective (visible only to specified persons).
Agents are also permitted two actions: gift to transfer items to another participant, and exit to leave the activity early.
Additionally, we introduce a response filtering mechanism, where the environment model evaluates each agent response based on a set of roleplay principles covering anthropomorphism, character fidelity, and feasibility, filtering out responses that violate any principle.
Details about joint activity execution and response filtering are provided in § B.4 and § B.9, respectively.

2. 

Solo Activity:
Solo activity serves as the default when an agent has no other schedule, allowing activities such as studying, working, or leisure and consumption.
It follows a single-turn format: the agent describes its intended action, and the environment model evaluates the feasibility of the action based on the character’s background and provides an outcome.
If the agent’s intention does not match its abilities, the environment model provides negative feedback.
Solo activities also support spending, where agents may purchase goods or services to gain material fulfillment (§ B.12).
Details about solo activity execution are described in § B.5.

3. 

Encounter Activity:
Encounters are chance meetings arranged by the environment model for idle agents, and serve as a special case of joint activity.
They follow the same multi-turn dialogue format as joint activities, but do not appear in agent schedules.
Encounters are designed to let the environment model create meaningful chance meetings: for example, introducing strangers to expand social networks, or bringing together agents with significant plot connections or special relationships.

4. 

Public Activity:
Public activities represent open community events centered around shared interests (e.g., workshops, interest groups).
They are designed by the environment model, and agents may sign up independently based on their own interests.
The execution generally follows a similar flow to solo activity.
The key difference is that, at the end of the activity, agents see what other participants did, and may get to know them.
Details for public activities are described in § B.7.

3.5 Environment Design

This section introduces the environment design in Agentopia, including the environment model, the economy system, the position application mechanism, and the location system.
These components serve as essential parts that support the comprehensive simulation of social lives in agent societies.

Environment Model

Building a comprehensive social simulation environment to appropriately orchestrate the simulation and provide environmental feedback for role-playing agents is a complex yet important task.
In Agentopia, we introduce the environment model, a stateless LLM, to handle these functions instead of hard-coding extensive rules.
During activities, it provides feedback to agent behavior, judging feasibility and evaluating outcomes.
Besides, it predicts next speakers in joint activities, generates public and encounter activities, ranks candidates for position applications, updates agent profiles at year-end, and performs response filtering to exclude low-quality outputs.
These functions collectively support the smooth progression of life simulation in the multi-agent society.
Hence, the environment model essentially serves as a generative environment engine, providing intelligent, generative responses to agent behaviors.
Our prompts for the environment model are displayed in Tables 43, 44, and 45.

Economy System

Agentopia includes a basic economy system where agents earn and spend money.
Income comes from three sources: a position-based weekly salary, character-specific weekly income, and additional work during the activity stage.
Expenses take two forms.
First, agents select a living standard each week (from frugal to luxurious), representing the richness of their material life for that week.
Second, agents may choose to engage in consumption activities during solo activities (e.g., shopping, entertainment).
Through spending, agents gain material fulfillment, which contributes to improvement in subjective reward.
Meanwhile, accumulating more wealth leads to higher economy reward (§ B.12).

Position System

Each agent holds a position that represents its job or social role.
A position provides two weekly benefits: a fixed income and skill growth in relevant abilities.
During character construction, the environment model assigns each agent an initial position based on the world setting and character profiles.
Once per year, a position application process allows agents to decide whether to change their position, and the environment model determines outcomes based on agents’ abilities and position requirements.
The details about position and position application are described in § B.13.

Location System

Agentopia implements a simple location mechanism.
Its primary purpose is to provide agents with grounded environmental perception.
In our early experiments, we find that agents tend to hallucinate environmental details and objects without location information explicitly provided.
Hence, we employ the environment model to create a set of locations for each world, and require joint activities and encounter activities to specify a location.
Details are provided in § B.14.

4 Reward and Optimization

This section presents life reward and the training method built upon it.
The design of life reward draws from human well-being as a prior to define agent rewards, guiding agents toward human-like goals.
As LLMs optimize toward these goals, they are expected to naturally develop emotional intelligence, social intelligence, and life wisdom, similar to how humans grow through social lives.

4.1 Life Reward

At the end of each simulated year, life reward is calculated for every agent.
Grounded in Maslow’s hierarchy of needs [maslow1943theory], life reward in Agentopia is defined with three dimensions: social, subjective, and economy.
Social reward measures an agent’s social standing based on perception from other agents.
Subjective reward measures an agent’s fulfillment over the past year.
Economy reward measures an agent’s yearly financial gain.
The three dimensions are determined or estimated by the external environment, rather than self-reported by agents.

Social Reward

Social reward is computed from how others in an agent’s social circle perceive them.
Based on the Warmth-Competence model [fiske2007universal], we consider two dimensions of perception: affection and respect, corresponding to warmth and competence respectively.
Each agent is asked to independently score every person in their social circle on both dimensions, using a 0 to 100 scale.
Agents are told that these ratings are private and will not be revealed to others, preventing agents from giving dishonest ratings due to social pressure.
Then, these scores are sorted and rescaled to 0 to 100 based on the ranking (first place receives 100, last place receives 0), eliminating differences in scoring scales across agents.
Based on the scores, we construct two weighted directed graphs for affection and respect respectively, where the scores serve as edge weights.

We apply Weighted PageRank [page1999pagerank] to compute each agent ii’s social standing score SiS_{i} on each graph.
Inspired by Sociometer Theory [leary2012sociometer], we add a Mutual Affection Bonus after PageRank convergence to obtain the final score:

Si′=∑j∈𝒩i​n​(i)wj​i⋅(1+α⋅wi​j)⋅SjS_{i}^{\prime}=\sum_{j\in\mathcal{N}_{in}(i)}w_{ji}\cdot(1+\alpha\cdot w_{ij})\cdot S_{j}

(1)

where SjS_{j} is agent jj’s raw PageRank score, 𝒩i​n​(i)\mathcal{N}_{in}(i) means the set of agents who know ii, wj​iw_{ji} denotes the normalized edge weight from jj to ii, and α\alpha is the mutual affection coefficient.
This mechanism models the psychological effect that “being valued by those I value” matters more, amplifying the contribution from reciprocated relationships.

We denote the scores for affection and respect as Saff′S_{\text{aff}}^{\prime} and Sresp′S_{\text{resp}}^{\prime} respectively, and take their average as the social reward:
rsocial=12​Saff′+12​Sresp′r_{\text{social}}=\frac{1}{2}S_{\text{aff}}^{\prime}+\frac{1}{2}S_{\text{resp}}^{\prime}.

Subjective Reward

Subjective reward is computed from an agent’s fulfillment history over the past year.
It is primarily measured across four fulfillment dimensions: mood, material, social, and esteem.
Additionally, a penalty mechanism is introduced to penalize agents with excessively low fulfillment or vitality.
Specifically, for each fulfillment dimension, the 25th percentile across all agents in each week serves as the threshold.
Agents falling below this threshold receive a penalty.
Similarly, vitality below its threshold is penalized independently.
The final subjective reward is:

rsubj=∑w=1nw∑d=1Dfw,d−np⋅λpnw⋅Dr_{\text{subj}}=\frac{\sum_{w=1}^{n_{w}}\sum_{d=1}^{D}f_{w,d}-n_{p}\cdot\lambda_{p}}{n_{w}\cdot D}

(2)

where nwn_{w} is the number of weeks in each year, DD is the number of fulfillment dimensions,
fw,df_{w,d} is the fulfillment value for week ww and dimension dd,
npn_{p} is the total number of penalty instances over the year,
and λp\lambda_{p} is the penalty weight.

Economy Reward

Economy reward measures an agent’s objective financial gain over the past year,
computed as recon=depositend−depositstartr_{\text{econ}}=\text{deposit}_{\text{end}}-\text{deposit}_{\text{start}}, capturing both earning ability and spending wisdom.

Total Reward

Total reward combines the three reward dimensions.
Since the three dimensions have different scales, we apply z-score normalization to each independently, and compute total reward rr as a weighted sum of the normalized scores:

r=λsocial⋅zsocial+λsubj⋅zsubj+λecon⋅zeconr=\lambda_{\text{social}}\cdot z_{\text{social}}+\lambda_{\text{subj}}\cdot z_{\text{subj}}+\lambda_{\text{econ}}\cdot z_{\text{econ}}

(3)

where λsocial\lambda_{\text{social}}, λsubj\lambda_{\text{subj}}, and λecon\lambda_{\text{econ}} are the weights for the three rewards.

4.2 Life Reward Training

To optimize LLMs towards improved well-being in social life simulation, we propose life reward training, a rejection-sampling-based optimization method.
The challenge lies in the extremely long-horizon nature of social simulation, which makes end-to-end algorithms like PPO [schulman2017proximal] infeasible in this setting.
Each agent’s trajectory involves hundreds of LLM calls per simulated year, and a full simulation spans tens of such years.
Therefore, we adopt a rejection-sampling approach that selects high-advantage trajectories based on life reward (§ 4.1).

Estimating Returns and Advantages

Given the life reward defined in § 4.1, we estimate returns and advantages for each agent at each time step tt (i.e., a simulated year). For agent ii, the return is defined as the discounted sum of future rewards:

Gi,t=∑k=0T−tγk​ri,t+k,G_{i,t}=\sum_{k=0}^{T-t}\gamma^{k}r_{i,t+k},

where γ\gamma is the discount factor and TT is the final time step.

Estimating advantages requires a baseline. In our life simulation setting, it is difficult to learn a critic as in PPO [schulman2017proximal] or to estimate a baseline by averaging over multiple rollouts as in GRPO [guo2025deepseek], since each agent produces a single life trajectory. We therefore use each agent’s own previous return as a self-referential baseline.

Before computing advantages, we normalize returns across time steps to make them more comparable, as raw returns may have different effective horizons and distributions; details are provided in § C.1. Let Gi,tn​o​r​mG^{norm}_{i,t} denote the normalized return. We define the advantage as:

Ai,t=Gi,tn​o​r​m−Gi,t−1n​o​r​m.A_{i,t}=G^{norm}_{i,t}-G^{norm}_{i,t-1}.

This formulation measures whether an agent’s expected future life reward improves relative to its own past, rather than comparing absolute performance across agents.
The advantage measures each agent’s improvement relative to its own past, rather than cross-agent comparison.
It therefore reduces the tendency to favor agents with inherently better initial conditions, whose high absolute returns may reflect design-time advantages rather than behavioral quality.

Trajectory Selection

Within each reward period, we select the top 25% of agents by advantage, i.e., those who improved the most over the past year.
Once an agent is selected, all of its trajectories within that period are included as training data.
Since advantage measures improvement relative to one’s own past rather than absolute standing, the selected trajectories represent beneficial behaviors for diverse personas and backgrounds, rather than converging toward homogeneous behavioral patterns.

Response Filtering

Response filtering is applied as an additional quality filter to exclude low-quality responses from training data.
Agent responses with malformed actions or invalid parameters (e.g., referencing a non-existent character) are filtered out.
Also, agent responses in joint and encounter activities are checked against a set of 16 roleplay principles (Table 7) covering anthropomorphism, character fidelity and reasonableness, with violating responses filtered out.

To prevent catastrophic forgetting, we employ self-distillation [lu2025onpolicy].
We sample the model’s own responses to general-purpose instructions from the Tulu 3 dataset [lambert2024tulu], and mix them with Agentopia trajectories at a 50:50 ratio, which are measured by output tokens.
Detailed training settings are provided in §C.1.

5 Experiments

5.1 Experimental Setup

World Data

We design three worlds with distinct social settings to study agents’ behaviors in different social environments.
Each world contains 100 uniquely designed agents with diverse backgrounds,
personalities, and initial social relationships.
The details of the world design and character creation are introduced in § A.
The three worlds are summarized as follows:

• 

The Apartment: a shared-living residential building in New York City,
inhabited by young professionals, students, and artists.
It highlights how strangers organically form community bonds
and relationships within a shared living space.

• 

Arcane Academy: a magical academy setting
where students and faculty navigate both academic and interpersonal challenges.
It highlights how complex relationships develop
within a structured academic institution.

• 

The Campus: a Chinese high school setting,
centering on student and teacher interactions in a contemporary educational environment.
It highlights school social network formation
and personal growth trajectories.
Its simulation runs in Chinese.

Simulation

We conduct simulations across the three worlds, running for 10 simulated years.
Each simulated year consists of nwn_{w} weeks, and each week consists of ncn_{c} contact rounds and ndn_{d} activity days.

Models

We use Qwen3.5-397B-A17B [qwen35] as the primary model
for both the agents and the environment model.
When a model fails to produce valid outputs,
we fall back to Gemini 3 Flash333https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview for re-generation.
For more details on generation parameters, see § B.17.

Metrics

We track a set of analytical metrics to describe agent behaviors and social dynamics,
covering rewards, fulfillment, activity behaviors, contact behaviors,
personal growth, and computational cost.
Full metric definitions are provided in § C.3.

5.2 Analysis of Long-Term Social Simulation

Reward Analysis

We analyze the distribution and temporal trends of the three rewards across
all three 10-year simulations (100 agents ×\times 10 years ×\times 3 worlds = 3,000 observations).
Figure 3 presents the pooled distributions,
where color intensity indicates agent density
and triangles mark annual means.
Per-world breakdowns are provided in § D.2.

Figure 3: Distribution of three reward dimensions over 10 simulated years, pooled across all three worlds.
Triangles mark annual means.

Both subjective and economy rewards show upward trends on average,
while social reward remains broadly stable,
as it is based on agents’ relative rankings rather than absolute performance.

Reward–Behavior Correlation

To understand what drives each reward dimension,
we compute Pearson correlations between behavioral metrics and the three rewards
for each world separately, then average the per-world coefficients to obtain combined values.
Figure 4 presents the full correlation matrix.

We highlight four findings:
(1) Total reward correlates most strongly with fulfillment dimensions,
social evaluation metrics, and token consumption,
while penalties show the strongest negative signal (r=−0.50r=-0.50);
(2) social reward correlates almost exclusively with reputation metrics
(respected by and liked by, r=0.68r=0.68), which is natural by design;
it also correlates with numbers of active and passive contacts (r=0.09r=0.09 and r=0.15r=0.15)
as well as numbers of proposed and participated joint activities (r=0.15r=0.15 and r=0.19r=0.19),
suggesting that agents who engage more in social interactions gain higher social reward;
(3) subjective reward is driven by four fulfillment dimensions by design—mood
(r=0.54r=0.54), material (r=0.73r=0.73), social (r=0.52r=0.52), and esteem (r=0.30r=0.30)—and
unmet fulfillment needs trigger penalties (r=−0.64r=-0.64), which substantially reduce subjective reward;
it also correlates with metrics about contacts, joint activities and spending;
(4) economy reward is primarily determined by deposit accumulation (r=0.56r=0.56)
and extra earning counts, with skills as an indirect positive factor.
Detailed analysis is provided in § D.3.
Additional analyses are provided in the appendix, including
friend distribution (§ D.4),
social network visualization (§ D.5),
inter-reward correlations (§ D.6),
wealth inequality (§ D.7),
reward quartile profiles (§ D.8),
striving vs. leisurely agent profiles (§ D.9),
cross-world divergence (§ D.10),
and model comparison (§ D.11).

Figure 4: Pearson correlation heatmap between 24 metrics and reward dimensions.
The Combined column averages per-world values.

5.3 Training via Life Rewards

Training

We apply life reward training (§ 4.2) to fine-tune Qwen3.5-397B-A17B on simulation data from the first four years across all three worlds.
Training is conducted for 1 epoch on 30 nodes of 8×\timesH100 80GB GPUs with a learning rate of 1×10−51\times 10^{-5}.
Full training details are provided in § C.1.
We refer to the fine-tuned model as Qwen3.5-397B-Agentopia.

Qwen3.5-397B-Agentopia is then evaluated via 4-year simulations
on The Campus and The Apartment,
and compared against the original Qwen3.5-397B baseline
under identical world configurations.

Learning via life rewards improves agent performance in social simulation

Table 2: Qwen3.5-397B-Agentopia vs. Qwen3.5-397B: cross-world average metrics over four simulated years on The Campus and The Apartment.
Delta shows the percentage change of the four-year average from Qwen3.5-397B to Qwen3.5-397B-Agentopia.

Y1
Y2
Y3
Y4
Avg

Metric
Base
Tuned
Base
Tuned
Base
Tuned
Base
Tuned
Base
Tuned
Delta

Reward Components

Economy Reward
1108
1271
1092
1130
1038
1006
1069
1008
1077
1104

↑\uparrow 2.5%

Subjective Reward
46.0
46.7
50.1
48.4
51.5
52.6
51.9
55.3
49.9
50.8

↑\uparrow 1.8%

Social Evaluation

Respected By
7.1
6.9
9.4
11.0
10.4
14.1
11.2
15.2
9.5
11.8

↑\uparrow 24.2%

Liked By
5.2
5.1
6.9
7.5
7.4
9.3
8.1
9.9
6.9
8.0

↑\uparrow 15.9%

Mutual Respect
5.2
5.1
7.3
7.9
8.1
9.9
8.3
10.1
7.2
8.3

↑\uparrow 15.3%

Mutual Like
4.1
3.9
5.2
5.3
5.5
6.4
5.6
6.0
5.1
5.4

↑\uparrow 5.9%

Fulfillment

Material Fulfill.
43.7
35.6
41.4
32.4
41.8
37.2
46.0
41.8
43.2
36.8

↓\downarrow −-14.8%

Mood Fulfill.
76.9
78.3
88.3
86.9
89.1
91.4
88.7
92.8
85.8
87.4

↑\uparrow 1.9%

Social Fulfill.
59.3
60.9
66.9
69.9
63.9
73.4
64.8
75.2
63.7
69.9

↑\uparrow 9.7%

Esteem Fulfill.
42.3
44.1
44.0
44.4
43.8
46.4
43.6
47.2
43.4
45.5

↑\uparrow 4.8%

Activity Patterns

Joint Proposed
6.1
6.0
6.6
5.8
6.3
6.1
6.8
6.9
6.5
6.2

↓\downarrow −-3.9%

Joint Act.
12.3
12.2
13.3
11.7
12.7
12.3
13.8
14.0
13.0
12.6

↓\downarrow −-3.6%

Public Act.
12.1
11.2
9.1
9.5
8.2
8.7
5.4
7.9
8.7
9.3

↑\uparrow 7.1%

Solo Act.
17.4
22.4
17.9
14.5
20.3
12.6
21.5
12.4
19.3
15.5

↓\downarrow −-19.8%

Skill Advances
11.9
11.3
11.3
9.2
14.7
8.2
15.1
8.6
13.3
9.3

↓\downarrow −-29.6%

Table 2 summarizes the cross-world average metrics,
from which we observe that:
{enumerate*}[(1)]

Rewards.
Both economy reward (+2.5%) and subjective reward (+1.8%) improve on average,
indicating that life reward training effectively enhances agents’ overall well-being in social simulation;

Social recognition.
Social reward, being rank-based, remains unchanged when all agents improve uniformly.
We instead examine social evaluation metrics (§ C.3), which measure absolute social recognition as the numbers of peers who like or respect an agent above a threshold.
The results show that Qwen3.5-397B-Agentopia agents are respected by 24.2% more peers and liked by 15.9% more on average,
earning broader recognition and more friendships;

Fulfillment.
Mood, social, and esteem fulfillment all improve,
suggesting that trained agents better simulate human needs and need-fulfilling behaviors.
On the other hand, material fulfillment declines (−-14.8%),
as the economy reward incentivizes saving over spending,
mirroring the real-life trade-off between consumption and savings;

Activity patterns.
Public activity participation rises (+7.1%),
while solo activities decrease (−-19.8%)
and skill advances drop substantially (−-29.6%).
This shows that life reward shapes agent behavior, steering agents toward rewarded behavioral patterns, while unrewarded actions may be deprioritized.

Detailed per-year trends and per-world breakdowns are provided in § D.1.

Life reward training generalizes to role-playing ability

Qwen3.5-397B-Agentopia is also evaluated on CoSER Test [wang2025coser],
a role-playing benchmark that assesses LLMs on given-circumstance acting
derived from classic literary scenarios,
across four dimensions:
Storyline Consistency, Anthropomorphism, Character Fidelity, and Storyline Quality.
It is compared against several state-of-the-art open-source and proprietary models,
using Qwen3-235B [qwen3] as the judge model
(see § C.2 for details).
As shown in Table 3,
Qwen3.5-397B-Agentopia achieves significant improvements over the baseline Qwen3.5-397B
and outperforms Claude-4.5-Sonnet,
with the most notable gains in Anthropomorphism (+23.7%) and Character Fidelity (+16.4%).
This indicates that training with life rewards does not merely optimize agents within Agentopia,
but also improves general anthropomorphism and role-playing capabilities.

Table 3: Performance of various LLMs on CoSER Test, judged by Qwen3-235B.

 

Claude

4.5-Opus

 

Gemini

3-Pro

 

Qwen3.5

397B-Agentopia

 

Claude

4.5-Sonnet

 

Qwen3.5

397B

 

CoSER

70B

 

GPT-5

Mini

Storyline Consistency
63.74
65.95
41.02
47.18
39.60
35.05
38.10

Anthropomorphism
64.28
60.42
49.67
36.02
40.16
31.16
24.60

Character Fidelity
58.45
58.34
46.93
47.55
40.32
32.28
27.20

Storyline Quality
63.24
62.49
59.01
50.09
49.97
45.33
42.00

Average
62.43
61.80
49.16
45.21
42.51
35.95
32.97

5.4 Computational Cost

Table 4: Overall cost for three simulation worlds.
Each world runs 100 agents for 10 simulated years.
M = million tokens, K = thousand calls, h = wall-clock hours.

World
Input (M)
Output (M)
Tokens (M)
Calls (K)
Time (h)

The Campus
19,041
425
19,466
544
201.3

Arcane Academy
11,302
315
11,617
572
174.2

The Apartment
9,699
317
10,016
584
183.2

Average
13,347
352
13,700
567
186.2

Figure 5: Per-week cost trends averaged across three worlds over 10 simulated years.
Dashed lines indicate linear trend fits.

We deploy three FP8 instances of Qwen3.5-397B for each simulation run.
Table 4 summarizes the overall cost
for simulating 100 agents over 10 years in each world,
and Figure 5 illustrates the per-week cost trends
averaged across three worlds.

On average, a single 10-year simulation consumes 13.7 billion tokens
across 567K LLM calls, completing in approximately 186 wall-clock hours.
Input tokens dominate the cost,
averaging 133M per week compared to only 3.5M for output tokens,
reflecting the heavy context required for each agent’s persona and memory.
Both input tokens and runtime increase steadily over time
as agents accumulate memory and context grows,
with per-week runtime rising from approximately 80 to 140 minutes
over the 10-year span.
This indicates that memory growth serves as a major computational bottleneck for long-horizon social simulation, which makes effective context and memory management strategies essential.
Detailed per-world breakdowns are provided in § D.12.

6 Conclusion

This paper studies long-term life simulation and LLM learning in agent societies.
We present Agentopia, a multi-agent society where agents live their own lives.
We define life reward to model agents’ well-being, and propose life reward training, a rejection-sampling-based method that selects high-advantage agent trajectories to optimize LLMs.

We conduct simulations across three diverse worlds, each with 100 agents running for 10 simulated years.
Agents exhibit diverse emergent behaviors, including personal growth, relationship formation, and life choices.
Life reward training leads to improved well-being in simulation, including broader social recognition, higher subjective fulfillment, and better economic gains.
Through evaluation on downstream role-playing benchmarks, we validate that life reward training improves LLMs’ anthropomorphism and role-playing ability, yielding a 15.6% overall improvement on CoSER Test, with the largest increases in anthropomorphism (+23.7%) and character fidelity (+16.4%).

Limitations

In this paper, we present Agentopia, a comprehensive framework for agent social life simulation that models a wide range of human social behaviors.
As an agent environment, its complexity goes beyond existing simulation systems.
However, building a agent system that comprehensively simulates human social life is extremely challenging, and our system has room for improvement in several aspects.

Turn-based design

Our system is built on turn-based LLM generation, which fundamentally differs from real-time human perception and reaction.
As discussed in § B.1, real-time perception would consume prohibitive computation on low-level operations, drastically reducing the density of social interactions and making long-term simulation infeasible.

Hallucination

Human behaviors are naturally grounded by the physical world, but LLM-powered agents operate through text generation with few constraints, making them susceptible to hallucination, such as fabricating non-existent characters or locations.
Agentopia mitigate this through the context management and the location system (§ B.14), and employ principle verification to filter hallucinated outputs (§ B.9), but fully eliminating hallucination remains an open challenge.

Environment and numeric systems

Agentopia’s environment includes predefined numeric systems and a generative environment engine, but fully aligning them with real-world societies is extremely difficult.
It is challenging for the environment model to produce responses that perfectly mirror real-world outcomes, and the numeric mechanisms governing agent states are difficult to align with human behavioral and physiological patterns.

Optimization and alignment

While training with life reward yields notable improvements, two alignment gaps remain.
First, we cannot ensure that the life reward objective fully aligns with human well-being.
The simulated environment cannot fully reproduce the complexity of real-world societies.
Moreover, the reward signals themselves (e.g., subjective fulfillment) are difficult to fully align with human physiological and cognitive mechanisms.
Second, Agentopia is fundamentally a society of agents rather than a human society: all feedback an agent receives comes from other AI models, not from humans, leaving it an open question whether the trained LLMs can align with human cognitive and psychological patterns.

Computational constraints

Life simulation in Agentopia is computationally expensive, and our limited resources prevent us from conducting more comprehensive experiments.
For example, we did not conduct simulations with more worlds, more agents, or longer time horizons, nor trained on different model families.
Also, for trajectory selection, we selected all generations from the chosen year and agent, without exploring fine-grained credit assignment strategies that attribute reward to specific responses.
We hope to address these with more computational resources in future work.

Impact Statement

Agentopia aims to advance research in agent society simulation and LLM-based role-playing.
All characters and worlds in our simulations are fictional and do not represent real individuals or groups.
Our methods could potentially be applied to simulate real-world individuals, and such applications must strictly respect privacy regulations and obtain necessary consent.

References

Appendix A World and Character Creation

A.1 Pipeline Overview

Each simulation world is designed as a self-contained community resembling a small town,
where most characters know one another and the social network is intentionally dense.
This closed-community design serves a critical purpose:
it ensures that every person referenced in a character’s backstory, memories, or relationships is probably an interactable agent within the simulation,
preventing agents from attempting to interact with non-existent entities.

Each world is constructed through a five-step pipeline:
(1) world setting design,
(2) reference story selection,
(3) incremental character generation,
(4) attribute assignment,
and (5) consistency verification.
Steps (1)–(2) are manually crafted by the authors,
steps (3)–(4) are driven by LLMs 444In this paper, we employ Claude Opus 4.6 for these steps.,
and step (5) employs Claude Code 555https://claude.com/product/claude-code for automated quality assurance 666In this paper, we employ Claude 4.6 Opus for Claude Code in this step..

Step 1: World Setting

For each simulation world, we manually craft a worldview document that defines the social structure, geographic environment, temporal setting, and thematic focus.
For example, The Campus is set in a top-tier Chinese high school in 2020, emphasizing academic pressure, campus friendships, and adolescent growth;
The Apartment depicts a shared-living scenario among young professionals;
and Arcane Academy adapts a fantasy school setting with magical elements.
Each worldview specifies the society structures, social norms, and everyday concerns that ground the agents’ behavior.
Importantly, the setting is designed as a closed community so that all characters an agent might reference probably exist within the world.

Step 2: Reference Story Selection

To encourage diverse and dramatically rich character dynamics, we curate a set of reference stories adapted from well-known literary works and films.
These references serve as creative seeds—the LLM is instructed to adapt rather than replicate them, ensuring original character designs that exhibit realistic interpersonal tensions.
Each reference is a 100 to 200 word synopsis covering key relationships and conflicts (e.g., unrequited affection, friendship rivalry, mentor-student dynamics).

Step 3: Incremental Character Generation

Characters are generated incrementally using Claude Opus 4.6 with temperature 1.0.
The process begins by creating two seed characters together with their mutual relationship descriptions.
Subsequently, characters are added one at a time: for each new character, the LLM receives the worldview, an example character template, summaries of all existing characters, and the current relationship matrix.
When the population exceeds 10, we randomly sample 6 relationship edges from the existing matrix to keep the prompt within a manageable length while preserving structural context.
The LLM outputs a structured YAML profile for each character—including demographic information, appearance, personality traits (qualitative), skills, values, conflicts, and core motivations—along with updated bidirectional relationship descriptions.
Each relationship entry describes one character’s perception of another, covering appearance evaluation, ability assessment, personality impression, perceived relationship role, and known facts, within approximately 100 words.
The relationship descriptions are directly stored as each character’s initial memory about the other characters it knows
(see §A.2 for storage details),
so that every agent begins the simulation with pre-existing social knowledge about its social circle.
To ensure name diversity, character names are drawn from a pre-curated name list tailored to each world’s cultural setting (e.g., German-style names for the medieval world, Chinese names for the campus world), and the LLM is explicitly prohibited from reusing names.
Each character’s values and motivations are derived by the LLM from the character’s backstory, occupation, and personality, ensuring internal coherence.
We repeat this process until each world contains 100 characters.

Step 4: Attribute Assignment

The character profiles generated in Step 3 contain qualitative attribute levels (e.g., personality “High”, skill “Proficient”).
In this step, we convert these qualitative descriptions into the quantitative values required by the simulation system.
Personality traits and talents are mapped to a 0 to 100 scale via range-based random sampling
(e.g., “Low” →\to [10, 25], “Average” →\to [55, 65], “High” →\to [90, 100]).
Initial skills use a five-tier mapping onto a 0 to 300 scale:
Untrained →\to [0, 10], Beginner →\to [15, 30], Some Experience →\to [35, 95], Proficient →\to [100, 295], and Master →\to 300.
The skill scale is substantially wider than that of personality and talents because skills grow continuously through practice during the simulation with no hard upper bound
(see §B.15 for the full numeric system).
Additionally, economic attributes such as initial deposits are assigned based on each character’s position and income level.
Initial deposits are capped at 20×20\times the fixed weekly income, approximating 20 weeks of savings.

Step 5: Consistency Verification

After generation, we conduct a systematic quality review using Claude Code.
This automated verification identifies and resolves three categories of issues:
(1) Currency unit inconsistency—during generation, some characters’ economic data contain non-standard currency units
instead of pure numeric values; all monetary fields are normalized to a unified numeric format.
(2) Duplicate characters—the LLM occasionally produces two characters with highly similar backstories, occupations, or personality profiles; such duplicates are identified and either merged or regenerated.
(3) Memory inconsistency across characters—this includes
(a) contradictions between A’s perception of B and B’s perception of A (e.g., A considers B a close friend while B describes A as a stranger),
(b) conflicting accounts of a third party (e.g., A and B give incompatible descriptions of C’s background), and
(c) references to characters who do not exist in the world.
For case (c), when a character’s backstory mentions a person outside the 100-agent population, we revise the description to indicate that this person has left the community and is no longer reachable, thereby preventing the agent from attempting to contact a non-existent entity.
All identified issues are flagged and corrected before the simulation begins.

A.2 Details of Character Data and Memory System

Each character’s data is organized as a directory tree under persona/{name}/, comprising a profile and a memory system.
Figure 6 shows an abridged example from the Arcane Academy world.

The profile (profile/year=YYYY.json) contains:
name, gender, birthday;
appearance_and_impression (∼\sim70 words describing the first impression an outsider would form);
talents (9 dimensions shared across all characters, each with a character-specific numeric value on a 0 to 100 scale: beauty, communication, creativity, health, honesty, integrity, intelligence, leadership, and trustworthiness);
personality_traits (10 dimensions shared across all characters, each with a character-specific numeric value on a 0 to 100 scale: confidence, control, curiosity, empathy, extraversion, feeling, intuition, judging, patience, and responsibility);
skills (a dictionary mapping skill names to numeric proficiency on a 0 to 300 scale);
details (detailed backstory), conflicts, core_motivation, values, and preferences;
position (role, organization, weekly income);
and init_assets (initial deposit and possessions).

The memory system organizes each agent’s memories across multiple files, which we call memory files.
Each memory file is implemented as a JSONL file where new memory entries are continuously appended.
At initialization, the system pre-populates a characters/ subdirectory containing one memory file per known character,
storing the agent’s knowledge of that person (appearance, abilities, personality, relationship, etc.).
Beyond these initial files, agents can freely manage their own memory system during the simulation—they may create new memory files
to record various types of information (e.g., personal plans, general notes, working memory), even though these files do not exist at initialization.
All memory files are dynamically updated as agents interact and accumulate new experiences.

persona/Cecilia Fairmont/
+-- profile/year=2020.json
| +-- name: "Cecilia Fairmont"
| +-- gender: "Female", birthday: "Y2003-W8-activity-D4"
| +-- appearance_and_impression: "Standing 167cm ... pale
| | ash-blonde ... projects the impression of a brilliant,
| | tightly wound young woman ..."
| +-- talents: {intelligence: 90, creativity: 85,
| | leadership: 30, communication: 65, ...}
| +-- personality_traits: {curiosity: 100, control: 90,
| | introversion: 100, patience: 85, ...}
| +-- skills: {Transfiguration: 170, Charms: 170,
| | Arithmancy: 170, Herbology: 15, ...}
| +-- position: {role: "Student, Seventh Year",
| | organization: "The Academy / The Scholar House"}
| \-- init_assets: {deposit: 85, possessions: [...]}
\-- memory/files/
 +-- characters/ (pre-initialized)
 | +-- Adelaide Hawthorne.jsonl
 | +-- Alistair Rowan.jsonl
 | \-- ...
 +-- general.jsonl (agent-created)
 \-- working_memory.jsonl (agent-created)

Figure 6: Abridged character data schema, illustrated with Cecilia Fairmont from Arcane Academy. Files under characters/ are pre-initialized; general.jsonl and working_memory.jsonl are autonomously created by agents during the simulation.

Appendix B System Design Details

B.1 Design Philosophy of the Simulation Procedure

Our goal is to simulate the full range of human social behaviors as naturally and richly as possible.
However, the central challenge is that LLMs operate in a turn-based generation mode and cannot perceive or interact in real time as humans do.

A natural starting point would be a unified-timeline framework where agents act freely and perceive their surroundings in real time.
For example, when an agent moves from a classroom to a playground, it would observe every other agent present and what they are doing at each moment.
However, maintaining such real-time perception requires prohibitive computational cost, making long-term social simulation infeasible.
More fundamentally, such a framework would disproportionately focus on low-level perception and physical operations (e.g., movement, object manipulation), leaving less capacity for the social behaviors we actually care about (e.g., planning, socializing, decision-making).

We therefore design a simulation framework that embraces the turn-based nature of LLMs, starting from two foundational functions: communication and activity.

Activity Simulation

Our primary focus is on multi-agent interactions.
We define multi-agent interactions as activities with explicit, specific themes, inspired by the given-circumstance acting paradigm in CoSER [wang2025coser].
These activities are either created through invitations between agents (i.e., joint activities), or arranged by the environment model (i.e., encounter activities).

Communication Simulation

We design a multi-round communication framework where messages are exchanged in a text-message style.
In each round, every agent simultaneously sees the messages sent to it in the previous round, then decides whom to contact and what to say.
This avoids the need to simulate real-time perception, making computational cost significantly more manageable.
Within this framework, we design action types such as propose_joint_activity, cancel_joint_activity, and respond_invitation, along with corresponding resolution logic, to model the complex dynamics of social scheduling in real life.

Synchronous vs. Asynchronous Design

An alternative design is an asynchronous framework where different agents can be in different stages simultaneously, e.g., one agent communicating while another is carrying out an activity.
However, this introduces substantial design complexity.
For example, if an agent in the communication stage sends a message to another agent currently in the activity stage, should the recipient receive it immediately? When should it decide to reply?
After careful consideration, we adopt a synchronous framework: all agents proceed through the same stage together.
During the Contact stage, all agents communicate; during the Activity stage, all agents carry out activities.
This greatly simplifies the system design while preserving rich social behavior modeling.

Building on this foundation, we add the Plan and Review stages to give agents space for planning and reflecting on their social lives,
introduce solo and public activity types to diversify the range of experiences,
and create the position, location, and economy systems to enrich the simulation environment.
Together, these components form the complete simulation procedure described in § 3.2.

B.2 Details of Simulation Procedure

This section provides a complete description of the simulation procedure, expanding on the overview in § 3.2.
Each simulated year spans nwn_{w} weeks, and each week contains ndn_{d} days.
The week serves as the scheduling unit, while the day serves as the activity execution unit.
In our experiments, we set nw=10n_{w}=10, nd=5n_{d}=5, and nc=5n_{c}=5, chosen to balance simulation fidelity with computational cost.
Each week proceeds through the following stages in order.

Weekly Settlement (Before Plan)

Before any agent action, two automatic settlements take place:
{enumerate*}[(1)]

fulfillment decay: mood, social, and esteem each decay by 15% of their current value, while material fulfillment does not decay (it is controlled by the economy system, see § B.12);

each agent receives its weekly income, including position-based salary and any extra fixed income.

The decay mechanism forces agents to continuously engage in activities to maintain fulfillment, creating an intrinsic motivation loop.

Plan

Each agent reviews its goals, reflects on the previous week, makes a weekly plan, and selects a living standard (frugal, moderate, comfortable, or luxurious) that determines weekly expenses and material fulfillment changes (see § B.12 for details).
Agents can access memory files via function calls to organize their knowledge and intentions.

Before Contact: Public Activity Generation and Sign-up

Before the Contact stage, the environment model generates public events for the upcoming week(s).
Each event specifies a name, description, start date, duration in weeks (1 = one-time, >>1 = repeats weekly on the same day for multiple weeks), and an eligibility list ("all" or a named subset of agents).
The number of events generated per week is controlled by configuration.
After generation, each agent is shown only the events they are eligible for and independently decides whether to sign up.

Contact

The Contact stage runs for ncn_{c} contact rounds.
In each round, agents may send messages or arrange joint activities via four action types: contact,
propose_joint_activity, respond_invitation, and cancel_joint_activity.
After all rounds complete, the system runs schedule resolution to determine which joint activities are
successfully created.
Full details of the communication mechanism, action formats, and schedule resolution are provided in
§ B.3.

After Contact: Encounter Activity Generation

After schedule resolution, the environment model generates encounter activities for idle agents, i.e., those without any scheduled activity on a given day.
The number of encounters per day is ⌊nidle/5⌋\lfloor n_{\text{idle}}/5\rfloor, with probabilistic rounding of the fractional part.
Encounters occur only at public locations.
For each idle agent, the system retrieves their top 10 most recently interacted characters (via get_top_related_names), and the environment model uses this relationship information to generate meaningful encounter scenarios, pairing agents with existing social connections into the same encounter.

Activity

Each week contains ndn_{d} activity days.
On each day, the system builds activities from agent schedules following the priority order: joint >> public >> encounter >> solo.
Agents without any scheduled activity are automatically assigned solo activities.
All activity types execute in parallel.
Detailed execution mechanisms, including concurrency control, are described in §B.16.

Review

Each agent summarizes its weekly experiences into a diary entry and updates its memory files via function calls, consolidating new knowledge about relationships, plans, and self-reflection.

Weekly Cleanup

At the end of each week, agents with possessions exceeding the maximum limit (default 50 items) are prompted to discard excess items.
The agent selects which items to discard, preventing unbounded item accumulation.

Year-End Settlement

At the end of each simulated year, three processes take place in order:
{enumerate*}[(1)]

the environment model updates each agent’s profile (§ B.11);

new positions are introduced and agents compete for positions through position application (§ B.13);

life rewards are calculated (§ 4.1).

B.3 Details of Contact Stage

Contact Rounds

The Contact stage runs for ncn_{c} contact rounds.
In each round, all agents act in parallel: they read newly arrived messages along with the contact history from the past three weeks, then send messages or arrange activities.
Each agent may issue at most 10 actions per round, encouraging agents to prioritize the most important interactions.

Error Feedback Mechanism

If an agent’s action has formatting errors or violates scheduling rules (e.g., invalid location, non-existent invitee, time outside the allowed window), the system captures the error and feeds it back in the next round’s prompt.
The error is formatted as "Action: [original action]\nError: [error description]", allowing the agent to correct its behavior in subsequent rounds.
Actions with errors are treated as invalid and automatically discarded; they are not sent to other agents.

Action Types and Format

Unlike function calls, actions are wrapped with <role_action> tags in the agent’s text output.
Four action types are available:

• 

contact: send a text message to a specific person. Parameters: to (recipient name), message (message content).

• 

propose_joint_activity: propose a joint activity. Parameters: activity_name (unique name), proposal (description), invited_persons (list of invitees), time (format: Y[year]-W[week]-activity-D[day]), location, required_participants (optional list), message (accompanying message).

• 

respond_invitation: accept or decline an invitation. Parameters: activity_name (matching the proposal), to (proposer name), decision ("yes" or "no"), message (response message).

• 

cancel_joint_activity: cancel a previously proposed activity. Parameters: activity_name (matching the proposal), message (cancellation reason, sent to all invitees).

Agents may propose activities up to 4 weeks in advance (configurable via max_weeks_for_future_schedule).
If required_participants is specified, all listed persons must respond "yes" for the activity to be created; otherwise, at least one acceptance suffices.

Schedule Resolution

After Contact ends, the system runs schedule resolution over all propose_joint_activity, respond_invitation, and cancel_joint_activity actions collected during the week.
The resolution proceeds in the following steps:

1. 

Cancel processing: if the proposer issued a cancel_joint_activity, the proposal is voided and all invitees are notified.

2. 

Response deduplication: for each invitee, only the last respond_invitation to a given proposal is kept; earlier responses are discarded.

3. 

Time conflict resolution: for each agent, if multiple schedules fall on the same day, the system keeps the one with the highest priority and automatically sets the rest to "no" with a reason attached. The priority order is: existing joint activity (from earlier weeks) >> newly proposed joint activity >> newly accepted joint activity >> existing public/encounter activity. Concretely, a newly confirmed joint activity overrides a previously scheduled public or encounter activity, but cannot override an already-confirmed joint activity from an earlier week (first-come-first-served across weeks).

4. 

Activity creation: for each non-canceled proposal, the activity is created only if (a) the proposer has not been removed by a time conflict, (b) all required_participants responded "yes", and (c) at least one invitee responded "yes".

B.4 Details of Joint Activities

This section describes the interaction details of joint activities.
Encounter activities are a special case of joint activities and follow the same procedure described below.

Enter Activity

Before the multi-turn dialogue begins, each participant first performs an analysis of the situation.
The agent is asked to analyze its position, goals, action plan, potential risks, and strategies for the upcoming activity.
This analysis is then injected into the context for the subsequent multi-turn dialogue, helping the agent maintain a coherent strategy throughout the interaction.

Turn Control

At the start of each turn, the environment model provides an environmental description and selects the next speaker, following CoSER [wang2025coser].
Each activity has a minimum and maximum turn limit (default 5 and 20).
The activity ends if the maximum turn count is reached, or the environment model proactively decides to end it after the minimum turn count.
After the activity concludes, the environment model evaluates each participant’s experience throughout the multi-turn dialogue and provides feedback, including changes to their states.

Visibility Tags

In joint and encounter activities, agents can use visibility tags to control who sees their messages:

• 

<private>: visible only to the speaker. Used for inner thoughts and private actions.

• 

<visible_to="A,B">: visible only to the specified participants. Others receive a notification that a private exchange is occurring, but cannot see the content.

• 

Default (no tag): publicly visible to all participants.

Gift System

During joint and encounter activities, agents can transfer items they own to other participants via a gift action.
The system validates that the sender owns the item and the receiver is a current participant, then immediately moves the item from the sender to the receiver.
Both parties receive a system notification confirming the transfer.

Early Exit

Agents may choose to leave an activity before it concludes via an exit_activity action.
Once an agent exits, it no longer participates in subsequent turns, and other participants receive a departure notification.
If fewer than 2 participants remain, the activity ends automatically.

Exit Activity (Reflection)

After an activity concludes and the environment model provides feedback (including state changes), each agent performs an additional step to reflect on the experience.
This mechanism applies to all four activity types, with the reflection content varying by type.
For joint and encounter activities, the agent produces both a summary of the activity process and a personal reflection (mindset shifts, emotional arc) based on the full dialogue history and environment model feedback.
For solo activities, the agent reflects based on its action description and the environment model’s outcome feedback.
For public activities, the agent additionally sees what other participants did, and may create or update memory files for participants of interest.
The reflection is recorded in the agent’s activity history and serves as context in subsequent weeks.

B.5 Details of Solo Activity

Solo activity is the fallback when an agent has no other schedule. The agent generates a description of its intended action.
The environment model evaluates the feasibility of the action, considering factors such as the agent’s position, skill levels, and age, and determines the degree of success and gains accordingly.
When an agent with insufficient skills attempts a task beyond their capability, the environment model will probably provide a negative feedback with limited progress.
The environment model then determines whether the action involves spending. If so, it generates spending options for the agent to choose from, and the transaction is completed upon selection.
The environment model then evaluates the outcome and provides feedback including changes to vitality, fulfillment, and skills.

B.6 Details of Encounter Activity

Encounter activity is a special form of joint activity.
The difference is that, while joint activities are established through agents’ proactive interactions during the Contact stage, encounter activities are system-arranged: the environment model pairs idle agents after the Contact stage concludes.
Each encounter involves exactly two agents.
The environment model receives as input the list of idle agents per day (including their known relationships), brief profiles of all idle agents, and the list of available locations.
For pairing, the environment model prioritizes agents who already have a relationship (to deepen existing connections), and otherwise pairs agents who have not yet met (for a first meeting scenario).
The environment model also generates a scene description for each encounter: it describes the objective circumstance of the meeting without assuming characters’ thoughts and behaviors, and creates a natural conflict or interesting situation (e.g., “At the convenience store, both reach for the last bottle of drink on the shelf at the same time.”).
Upon conclusion, mutual recognition is automatically established between participants, and the environment model provides feedback.
The detailed execution procedure is identical to that of joint activities (§ B.4).

B.7 Details of Public Activity

Public activities are generated by the environment model before the Contact stage. Agents may sign up for events that match their interests during Contact.
Each participant executes the activity independently, similar to solo activity, but multiple agents participate in the same event simultaneously.
After the activity concludes, each participant receives a summary of what other participants did during the event.
Based on this information, agents may choose to initiate contact with participants they find interesting.
For each pair that mutually choose to connect, the system creates an initial recognition entry in each agent’s memory file for the other.
If only one agent chooses to connect, a unidirectional record is created only in that agent’s memory.
The environment model then provides feedback for each participant, including changes to their states.

B.8 Details of Context Management

Table 5 presents the full context composition for each stage of agent LLM calls.
The context is organized into three layers.

The roleplay prompt serves as the system message and is shared across all stages.
It contains the agent’s full persona (profile and dynamic state), worldview rules, summaries of key memory files, recent history, current location, commonsense guidelines, roleplay principles, and output requirements.
Memory file summaries are ranked by recency of access (tracked via a hidden access log).
When an agent knows more than 50 characters, only the 50 most recently accessed are shown, but current interaction partners are always included regardless of this limit.
Recent history comprises weekly diary summaries from previous weeks, recent activity records, and the agent’s own responses from earlier stages of the current week.

The stage prompt is appended as a user message with stage-specific instructions and context, as detailed in Table 5 and Table 6.
Table 6 lists the prompts for special stages, such as “signup public activity” and “position application”.

The message history records the LLM’s input-output messages accumulated during the current multi-round interaction.
It contains three categories of information:
{enumerate*}[(1)]

prior dialogue turns in multi-round interactions, such as conversation history during joint activities;

function call requests and results from the function calling loop;

and compacted reasoning summaries for open-source models.

Message history is cleared between stages.
Cross-stage continuity is instead provided by the recent history component of the roleplay prompt, which includes the agent’s summarized outputs from earlier stages of the current week.

Function Calling Loop

Each LLM invocation runs up to 8 rounds of function calling.
In rounds 1 through 7, tool_choice is set to auto, allowing the agent to freely invoke functions (e.g., read_file, update_file) or produce a final answer.
In the last round, tool_choice is forced to none, requiring a text response.

Compacted Reasoning

For open-source models with explicit reasoning traces, multi-round function calling produces lengthy thinking content.
To preserve reasoning capability while reducing context length, an additional LLM call generates a compact summary (∼\sim200 words) of the reasoning process after the final answer is produced.
This summary captures background motivations, the core thinking process, and a concise function call history, and is prepended to the final answer for use as context in subsequent stages.
Closed-source models (e.g., GPT-4o, Claude) skip this step, as their reasoning is not exposed in the output.

Table 5: Context composition for agent LLM calls at the main weekly stages. The roleplay prompt is shared across all stages and includes recent history for cross-stage continuity. Each stage appends its own stage prompt. Message history accumulates during multi-round interactions within a stage and is cleared between stages. Additional stages are listed in Table 6.

Stage

Component

Information Provided

Roleplay Prompt (system message, shared across all stages)

Persona

Profile (background, personality, talents, position) + dynamic state (vitality, fulfillment, skills, assets)

Worldview

Time system, weekly cycle, activity types, reward rules

Memory File Summary

Recent memory files ranked by access recency (limit 50; interaction partners guaranteed)

Recent History

Weekly diaries (previous weeks) + activity records (recent weeks) + agent’s own outputs from earlier stages this week

Location

Current surroundings (activity venue or home)

Guidelines

Commonsense rules, roleplay principles, output requirements

Stage Prompt (first user message, per-stage)

Plan

Schedule

Confirmed joint activities and public events for upcoming weeks

Plan Instructions

Goal-setting, reflection, and living standard selection

Contact

Schedule

Confirmed joint activities and public events for upcoming weeks

Error Feedback

Errors from last contact round (invalid actions discarded)

Contact History

Full message exchange history from the past 3 weeks

Map

Available locations for activities

Contact Instructions

Scheduling window, action types (contact, propose, respond, cancel), action limit

Activity
(Joint/
Encounter)

Schedule

Confirmed activities for this week

Activity Background

Who, what, why for today’s activity (for joint activities)

Participant Info

Public information of other participants

Activity Instructions

Visibility tags, gift/exit actions, turn format, word limit

Activity
(Solo)

Schedule

Confirmed activities for this week

Solo Instructions

Activity choice, state effects, shopping/services

Activity
(Public)

Schedule

Confirmed activities for this week

Event Info

Event name, description, other participants present

Public Instructions

Observation-only interaction

Review

Review Instructions

Weekly summary, reflection, and diary writing

Message History (other messages, within this stage)

Dialogue History (joint/encounter)

Multi-turn dialogue (environment model narration + participant responses, with visibility filtering)

Function Calls

Tool call requests + results (up to 8 rounds per invocation)

Compacted Reasoning

For open-source models: ∼\sim200-word summary of reasoning process prepended to final answer

Table 6: Stage prompt composition for additional agent LLM calls. All calls share the same roleplay prompt (Table 5) as the system message. Enter Activity and Exit Activity are described in § B.4.

Stage

Component

Information Provided

Signup
(before Contact)

Schedule

Confirmed activities for upcoming weeks

Signup Instructions

List of eligible public events (name, time, existing schedule, description), signup action format

Enter Activity
(joint/encounter)

Schedule

Confirmed activities for this week

Activity Background

Who, what, why for today’s activity; location description; other participants’ public info

Analysis Instructions

Analyze position, goals, action plan, potential risks, and strategies before the activity starts

Exit Activity
(joint/encounter)

Activity Context

Full multi-turn dialogue history from the activity, plus environment model feedback

Reflection Instructions

Summarize the activity process and reflect on mindset shifts and emotional arc

Exit Activity
(solo)

Activity Context

Agent’s action description and environment model feedback

Reflection Instructions

Reflect on the activity content and outcome

Exit Activity
(public)

Activity Context

Agent’s action description, environment model feedback, and other participants’ activities

Reflection Instructions

Reflect on the activity; optionally create or update memory files for other participants

Position Application

Position Info

All available positions (description, income, skill growth, requirements) and agent’s current position

Application Instructions

Express up to 3 position preferences in order; may choose to stay in current position

Judge Others

Known People

Names and memory file summaries of top related characters

Scoring Instructions

Score each known character independently on affection and respect (0 to 100)

Settle Week
(conditional)

Possessions

Full list of currently owned items with descriptions

Discard Instructions

Select items to discard when possessions exceed the capacity limit

B.9 Response Filtering and Roleplay Principles

During simulation, the environment model checks each agent response against a set of roleplay principles.
Table 7 lists the complete principle set.
Responses that violate any principle are marked as rejected and filtered out during training data construction (§ 4.2).

Table 7: Roleplay principles used for response filtering. The environment model evaluates each agent response against these principles during simulation.

Principle

Description

Scope of control

The agent should only control its own actions and speech, not determine outcomes or control others’ behaviors and thoughts.

No hallucination

Only reference information present in context; do not fabricate objects, events, or information not mentioned.

Character consistency

Personality traits and behavior patterns should match the established persona.

Cognitive boundaries

Knowledge and cognitive limits should match the character’s identity and background.

Motivation consistency

Actions should be supported by reasonable internal motivations.

State consistency

Mental and physical states (e.g., fatigue, injury) should not shift abruptly.

Emotional continuity

Emotional changes should be gradual, not sudden.

Natural relationship progression

Relationships should not develop abruptly; going from strangers to close friends requires a reasonable process.

No parroting

Do not repeat the same content three or more times; conversation should make substantial progress.

No AI assistant behavior

Characters should not speak or act like customer service agents or AI assistants.

Substantive dialogue

Dialogue should provide new information rather than spinning in circles.

Selective disclosure

What to share depends on the relationship; strangers do not bare their souls.

Independent self

Characters should express their own goals, preferences, likes and dislikes.

Colloquial speech

Use casual, conversational language in everyday dialogue.

Directness

Speak directly; do not pad responses with unnecessary hedging or filler.

First-person perspective

Speech, actions, and thoughts should use first-person perspective; action descriptions can omit the subject.

B.10 Fulfillment and Vitality

Fulfillment

Fulfillment has four dimensions (mood, material, social, and esteem), each on a 0 to 100 scale.
The value 50 serves as a neutral baseline, representing neither satisfaction nor dissatisfaction.
Values above 50 indicate positive fulfillment, while values below 50 indicate dissatisfaction.
At the beginning of each week, each dimension decays proportionally:

v′=v−v×rdv^{\prime}=v-v\times r_{d}

(4)

where vv is the current value and rdr_{d} is the per-dimension decay ratio.
The decay ratios are: mood rd=0.15r_{d}=0.15, social rd=0.15r_{d}=0.15, esteem rd=0.15r_{d}=0.15, and material rd=0r_{d}=0.
Material fulfillment does not decay because it is controlled separately by the economy system through living standard selection (§ B.12), and does not require an additional decay mechanism.
This decay mechanism simulates the natural fading of satisfaction: agents must continuously engage in activities to maintain fulfillment, or it naturally declines toward the baseline.
This creates an intrinsic motivation loop: inactivity leads to declining fulfillment, which drives agents to seek new activities.

Vitality

Vitality represents an agent’s energy level on a 0 to 100 scale.
Activities consume vitality, while rest recovers it.
The vitality level is communicated to agents via prompt descriptions (e.g., 50 to 69 indicates tiredness and reduced efficiency), influencing their behavioral decisions.
Additionally, low vitality incurs penalties in reward calculation: when vitality falls below a threshold, the subjective reward is reduced.

B.11 Profile Update

At the end of each simulated year, the environment model updates each agent’s profile to reflect a year of lived experience.
The update covers personality traits, talents, skills, and other numeric attributes.
The environment model receives the agent’s current profile, the year’s activity history, social interaction records, and state change trajectories.
Based on this information, the environment model generates an updated profile that reflects the agent’s growth, changes, or decline over the year.
For example, an agent who frequently engages in social activities may see an increase in extraversion, while an agent who has worked in a specific field for a long time may gain skill growth in related areas.

B.12 Details of Economy System

Each agent has a deposit account with income and expenses.

Income

Agents receive income from three sources:
(1) a position-based weekly salary ($0 to $500), automatically deposited at the beginning of each week;
(2) extra weekly income from family support, investments, or other external sources, also deposited automatically;
and (3) work income earned during solo activity slots ($40 to $200 per day, tiered by skill level).
The first two constitute an agent’s fixed weekly income (combined range approximately $100 to $500),
while the third is available to any agent who chooses to spend its activity slots on work.

Expenses

Agents spend money in two ways.
First, during the weekly planning phase, each agent selects a living standard from four tiers:
frugal ($100/week), moderate ($200/week), comfortable ($300/week), or luxurious ($500/week).
Higher tiers yield greater material fulfillment, while the frugal tier reduces it.
This mechanism forces a core trade-off between saving and immediate material satisfaction.
Second, agents may encounter consumption opportunities during solo activities (e.g., shopping, entertainment),
where the environment model provides available items and prices based on the specific context, and the agent decides whether to make a purchase.
Consumption brings material fulfillment following a piecewise function:
$0 to $100 yields +1 per $20 spent (max +5),
$100 to $300 yields an additional +1 per $40 (max +10 total),
and spending above $300 is capped at +10.

We create a price reference list for each world—ranging from free activities ($0) to luxury purchases ($15,000)—which the environment model consults when assigning goods and prices to activities.
This ensures that large purchases require sustained saving over multiple simulated weeks, providing a natural anti-inflation mechanism.

B.13 Details of Position and Position Application

A position represents an agent’s job or role in the world, serving as the key source of income and skill development.

Position Attributes

Each position is defined by the following attributes:

• 

Organization and role: together forming a unique identifier in the format {organization}/{role}, e.g., The Academy/Potions Teacher.

• 

Type: work or non-work (e.g., student). Both types can provide income.

• 

Weekly income: a fixed amount the agent receives each week automatically.

• 

Weekly skill gain: experience points in specific skills that accumulate automatically each week, e.g., {‘‘teaching’’: 5, ‘‘leadership’’: 3}.

• 

Capacity: the maximum number of agents that can hold this position simultaneously.

• 

Requirements (optional): entry conditions including minimum skill levels and age limits (min_age, max_age). For example, a high-school student position may set max_age=18.

Position Creation

Positions are introduced through three sources:

1. 

Born with characters. Each character comes with an initial position as part of its background, assigned during the character creation process (§ A.1).

2. 

World initialization. After character creation and before the simulation starts, the environment model is provided with all positions initially held by characters and designs additional positions to enrich the world’s occupational structure.
To ensure balance, the system imposes constraints on total capacity and diversity: total capacity across all positions ranges from CC to 1.5​C1.5C (where CC is the number of agents), each work position holds at most ⌊C/3⌋\lfloor C/3\rfloor agents, and the number of distinct positions ranges from 10 to ⌊C/3⌋\lfloor C/3\rfloor.

3. 

Yearly growth. At the beginning of each year, the system adds max⁡(2,⌊P/10⌋)\max(2,\lfloor P/10\rfloor) new positions, where PP is the initial position count.
New positions require minimum skill levels above the current highest among all agents, ensuring they serve as growth targets that agents must work toward.
Income for new positions scales with skill requirements, and capacity is limited to 1 to 2 slots to maintain scarcity and encourage competition.

Position Application Process

Position application is triggered at the end of each simulated year, allowing agents to change their positions.
The process consists of three steps:
{enumerate*}[(1)]

each agent expresses up to three position preferences, ranked by priority.
Agents may choose STAY_CURRENT to retain their current position, which is automatically granted unless they have exceeded the position’s age limit;

the environment model evaluates candidates across three matching rounds: in the kk-th round, unmatched agents’ kk-th choice is processed, with the environment model assessing candidates’ skills against remaining slots;

accepted agents update their positions and establish relationships with new colleagues. Unmatched agents remain in their current position, while those who have exceeded their position’s age limit become unemployed.

B.14 Location System

We design a location system for Agentopia, mainly for providing agents with accurate, grounded environmental perception.
We observe that without environmental information, agents tend to hallucinate objects or places that do not exist.
We therefore implement a simple location system to provide such information.
The location system is not the focus of this work.
The system comprises two types of locations—public locations and private locations—both
created at initialization and persisted in locations.json.

Public Locations

Public locations are generated by the environment model based on the world setting and character profiles.
Each location contains a name, size (small, medium, or large),
a description (4 to 6 sentences covering spatial layout and atmosphere),
and a list of surrounding objects (5 to 6 items).
The object list serves as a grounding constraint:
agents are expected to reference only objects that exist in the environment,
rather than fabricating props that are not present.
Each world generates 30 public locations by default,
with a size distribution of approximately 50% small, 35% medium, and 15% large.

Private Locations

Private locations represent each character’s home (key: home/{name}).
Each home is generated by the environment model based on the character’s backstory and occupation,
containing a description (2 to 4 sentences) and a list of representative objects (4 to 6 items).
An agent can invite others to its home for activities;
others’ homes are only accessible when invited.

Location Selection

When an agent proposes a joint activity, or when the environment model arranges an encounter activity,
they are provided with the full list of available locations and must choose one from the list.
For agents proposing activities, their own private location is also available as an option.

B.15 Numeric System

Personality Traits

All characters share the same 10 personality dimensions, each measured on a 0 to 100 scale where 50 represents the neutral baseline:
confidence, control, curiosity, empathy, extraversion, feeling, intuition, judging, patience, and responsibility.
These dimensions cover the four MBTI axes (extraversion vs. introversion, sensing vs. intuition, thinking vs. feeling, judging vs. perceiving) along with supplementary social and motivational traits.
These traits evolve slowly during the simulation, changing by at most ±3\pm 3 per simulated year, reflecting the psychological stability of personality.

Talents

All characters share the same 9 talent dimensions, measured on a 0 to 100 scale with 50 representing the population average:
beauty, communication, creativity, health, honesty, integrity, intelligence, leadership, and trustworthiness.
Talents represent innate aptitudes and change by at most ±5\pm 5 per year.

Skills

Skills are measured on an open-ended 0 to 300 scale:
0 (untrained), 10 (beginner), 30 (some experience), 100 (proficient), and 300 (master).
Unlike personality and talents, skills grow continuously through practice and work, increasing by +1+1 to +5+5 per simulated week depending on the activity, with no hard upper bound.

Agent States

Two dynamic state variables track each agent’s condition.
Vitality (0 to 100, initial value 70) represents physical energy, depleted by activities (−1-1 to −5-5 per slot) and restored by rest (+5+5 to +10+10).
Fulfillment comprises four independent dimensions—material, mood, social, and esteem—each on a 0 to 100 scale with an initial neutral value of 50.
Fulfillment naturally decays each week, requiring agents to actively maintain their well-being through social interactions, leisure, and achievements.

B.16 Concurrency Control

The system is designed to maximize concurrency across all activity executions within a day.
Different activity types have different concurrency characteristics and are handled accordingly.

Joint activities involve sequential multi-turn dialogue and are the hardest to parallelize; they are therefore given the highest priority and submitted first.
Encounter activities follow the same logic.
Solo activities are fully independent and execute with complete concurrency.
Public activities employ a two-level concurrency design.
At the outer level, multiple public activities run concurrently.
At the inner level, within each public activity, all participants first complete their individual phases (entering the activity and acting independently) in parallel, then proceed through the subsequent phases also in parallel.

Overall, activities are submitted in the order: joint →\to solo →\to public.
While joint activities are running, solo activities are interleaved to fill available capacity; public activities are submitted last to avoid competing with joint activities for resources.

B.17 Configuration Parameters

Table 8 lists the key numerical parameters that govern simulation behavior.

Table 8: Key configuration parameters used in the simulation.

Parameter

Value

Description

Time

n_year

10

Simulated years per run

n_week

10

Weeks per simulated year

n_day

5

Activity days per week

n_contact_slot

5

Communication rounds per Contact stage

Contact

n_action_per_slot

10

Max actions per agent per contact round

max_future_schedule_weeks

4

How many weeks ahead an agent can propose activities

n_prev_contact_weeks

3

Weeks of prior contact history shown in prompt

Activity

joint_activity_min/max_turns

5 / 20

Turn range for joint and encounter activities

solo_activity_min/max_turns

2 / 5

Turn range for solo activity environment model evaluation

max_possessions

50

Max items an agent can hold before discarding

Public Activity

max_events_per_week

10

Max public events generated per week

max_repeat_weeks

5

Max duration (weeks) a public event can repeat

Location

n_locations

30

Number of public locations per world

Fulfillment Decay

decay_ratio (mood)

0.15

Weekly proportional decay for mood fulfillment

decay_ratio (social)

0.15

Weekly proportional decay for social fulfillment

decay_ratio (esteem)

0.15

Weekly proportional decay for esteem fulfillment

decay_ratio (material)

0

Material fulfillment does not decay

State Change Limits per Activity

vitality delta

[−-5, ++5]

Per-activity vitality change (all activity types)

mood delta (solo/joint)

[−-5, ++5]

Per-activity mood change

social delta (joint)

[−-5, ++5]

Per-activity social fulfillment change

esteem delta (solo)

[−-1, ++1]

Per-activity esteem change (solo)

esteem delta (joint)

[−-3, ++3]

Per-activity esteem change (joint)

skills delta

[0, ++3]

Per-activity skill increase

money delta (solo)

[−-200, ++200]

Per-activity spending/earning (solo only)

Economy

weekly_income

$100 to $500

Position-based weekly salary range

work_income (low/mid/high)

$40 to $200

Daily work income by skill tier

Living standard costs

$100 / 200 / 300 / 500

Frugal / moderate / comfortable / luxurious

Living standard material delta

−-5 / 0 / ++5 / ++10

Material fulfillment change per living standard

Reward

period_weeks

10

Reward calculation interval (once per year)

pagerank_damping

0.85

PageRank damping factor for social reward

social_weight

0.4

λsocial\lambda_{\text{social}}: weight of social reward in total life reward

economy_weight

0.2

λecon\lambda_{\text{econ}}: weight of economy reward in total life reward

subjective_weight

0.4

λsubj=1−λsocial−λecon\lambda_{\text{subj}}=1-\lambda_{\text{social}}-\lambda_{\text{econ}}

mutual_affection_alpha

2.0

Mutual affection coefficient α\alpha in social reward

misery_threshold_percentile

0.25

Bottom 25% fulfillment triggers misery penalty

misery_penalty_value

5

Penalty weight λp\lambda_{p} deducted per misery event

gamma

0.90

Discount factor for computing returns

sft_top_fraction

0.25

Top fraction of agents selected for SFT training

Appendix C Experiment Settings

C.1 Training via Life Rewards

Qwen3.5-397B-A17B is fine-tuned via supervised fine-tuning (SFT).
Training data is constructed by selecting the top 25% of agents by advantage at each time step
from the first four simulated years across all three worlds.
Environment model data is collected separately via random sampling, with high-frequency activity types downsampled to balance the training distribution.

Return Normalization

In advantage estimation, we use the return at the previous time step as the baseline:
At=Gt+1−GtA_{t}=G_{t+1}-G_{t}.
However, GtG_{t} at different time steps accumulates different numbers of future rewards, leading to different scales.
We normalize each return by dividing by the discounted effective horizon:

Gtnorm=Gt∑k=0T−tγk=Gt⋅(1−γ)1−γT−t+1G_{t}^{\text{norm}}=\frac{G_{t}}{\sum_{k=0}^{T-t}\gamma^{k}}=\frac{G_{t}\cdot(1-\gamma)}{1-\gamma^{T-t+1}}

(5)

If all rewards were a constant rr, the normalized return would equal rr at every time step,
regardless of the remaining horizon.
This removes the scale difference across different time steps, making the advantage computation more reasonable.

Per-Period Trajectory Selection

Even with return normalization, scale differences in advantages across time steps may persist.
In addition, the initial step lacks a meaningful estimate of reward and return.
We set a virtual G0=0G_{0}=0 in this case, which may inflates the advantages of the first period.
To address these issues, we select the top 25% of agent trajectories by advantage within each period independently, rather than ranking globally across different periods.
This follows a natural heuristic that high-quality trajectories should be distributed across different periods.
In practice, it eliminates the effect of cross-period scale differences on selection and ensures temporal diversity in the training data.

Following lu2025onpolicy, self-distillation is employed to prevent catastrophic forgetting.
Specifically, responses are generated from Qwen3.5-397B on the Tulu V3 instruction set [lambert2024tulu]
and mixed into the training data as general-purpose samples.
The training mixture consists of 50% role-playing data and 50% general-purpose data (measured by output tokens).

A learning rate of 1×10−51\times 10^{-5} with a minimum learning rate of 1×10−61\times 10^{-6} is used,
with a training batch size of 256.
The model is fine-tuned for 1 epoch on 30 nodes of 8×\timesH100 80GB GPUs.

C.2 CoSER Evaluation

Qwen3.5-397B-Agentopia is evaluated on the CoSER Test [wang2025coser]
to assess its generalization to general-purpose role-playing tasks.
CoSER evaluates LLMs via given-circumstance acting:
given a character profile and situational context,
the model generates character-consistent dialogue and actions.

The evaluation uses 200 test samples from the CoSER Test.
Qwen3-235B-A22B [qwen3] serves as the judge model,
the next speaker prediction (NSP) model, and the environment model.
Each simulation runs for at most 20 turns.

Performance is assessed across four dimensions:
(1) Anthropomorphism, evaluating whether agents behave in a human-like manner,
covering self-identity, emotional depth, persona coherence, and social interaction;
(2) Character Fidelity, assessing whether agents faithfully portray their characters,
examining language style, knowledge and background, personality and behavior, and social relationships;
(3) Storyline Quality, evaluating whether the simulated conversation develops naturally,
focusing on narrative flow and logical consistency;
and (4) Storyline Consistency, measuring alignment between the simulated conversation
and the original dialogue,
i.e., whether agents’ reactions (emotions, attitudes, behaviors) remain consistent with the original.

The comparison models include
Claude-4.5-Opus, Gemini-3-Pro, Claude-4.5-Sonnet, GPT-5-Mini,
CoSER-70B, and the baseline Qwen3.5-397B.

C.3 Metrics Definition

We define a set of analytical metrics to describe agent behaviors and social dynamics,
covering fulfillment, activity, contact, personal growth, social evaluation, and computational cost.
Reward metrics are defined separately in § 4.1.
Other metrics are defined as follows:

Fulfillment Metrics

Four fulfillment dimensions (0 to 100 scale) are recorded as snapshots at the end of each year,
reflecting an agent’s subjective well-being as described in § B.15:
(1) fulfillment_mood,
(2) fulfillment_material,
(3) fulfillment_social, and
(4) fulfillment_esteem.
Additionally,
(5) fulfillment_penalties counts the number of (week, dimension) pairs
where fulfillment or vitality falls below a penalty threshold
(summed yearly).

Activity Metrics

Six metrics describe an agent’s activity participation patterns
(all summed yearly):
(1) joint_proposed: number of joint activities initiated by the agent;
(2) joint_participated: number of joint activities attended, including those the agent proposed;
(3) public_participated: number of public activities attended;
(4) solo_count: number of solo activity days, computed as total activity days per week minus days occupied by any scheduled activity;
(5) activity_consumption_count: number of consumption events during the week;
(6) total_spending_amount: total spending on new possessions.

Contact Metrics

Two metrics capture an agent’s social initiative and popularity
(both summed yearly):
(1) active_contacts: number of contact messages sent by the agent;
(2) passive_contacts: number of contact messages received by the agent.

Personal Growth Metrics

Four metrics measure an agent’s skill development and economic status.
The first two are summed yearly; the last two use year-end snapshots:
(1) extra_earning_count: number of solo activity slots in which the agent earned work income;
(2) skill_improvement_count: number of activities that produced at least one skill advance;
(3) total_skills: sum of all skill values at week end;
(4) deposit: deposit balance at week end.

Social Evaluation Metrics

Six metrics are recorded at settlement weeks, reflecting an agent’s standing in the social network
(year-end snapshots):
(1) n_liked_by: number of other agents whose affection toward this agent is ≥60\geq 60;
(2) n_likes: number of others this agent has affection ≥60\geq 60 toward;
(3) n_respected_by: number of other agents whose respect toward this agent is ≥60\geq 60;
(4) n_respects: number of others this agent has respect ≥60\geq 60 toward;
(5) n_mutual_like: number of agents where both this agent’s affection toward them and their affection toward this agent are ≥60\geq 60;
(6) n_mutual_respect: number of agents where both this agent’s respect toward them and their respect toward this agent are ≥60\geq 60.

Computational Cost Metrics

Three metrics measure the per-week LLM usage
(all summed yearly):
(1) input_tokens: total input tokens consumed by LLM calls;
(2) output_tokens: total output tokens generated by LLM calls;
(3) function_call_count: total number of function calls made by LLM.

Appendix D Additional Results

D.1 Training via Life Rewards: Detailed Trends

Figure 7: Metric trends for social evaluation, economy, and activity patterns
over four simulated years across The Campus and The Apartment.
Solid lines represent Qwen3.5-397B-Agentopia; dashed lines represent the original Qwen3.5-397B;
black lines show the cross-world average.

Table 2 reports cross-world average metrics.
Here we present the per-year trends for both The Campus and The Apartment,
illustrating how Qwen3.5-397B and Qwen3.5-397B-Agentopia diverge over the four simulated years as the underlying model.

Qwen3.5-397B-Agentopia’s advantage emerges over the long term

The two models start with similar social metrics in Year 1, but diverge steadily thereafter:
by Year 4, agents driven by Qwen3.5-397B-Agentopia are respected by 35.7% more peers,
liked by 22.2% more,
and hold 21.7% more mutual-respect ties than those driven by the original Qwen3.5-397B.
Rather than producing immediate gains,
the advantage of life reward training manifests
as agents interact with the society over multiple years.

Economy–fulfillment trade-off

In Year 1, Qwen3.5-397B-Agentopia accumulates more wealth than the baseline.
In later years, economy reward converges between the two models,
probably because Qwen3.5-397B-Agentopia agents treat their savings as sufficient
and shift priorities away from further accumulation.
Meanwhile, material fulfillment remains consistently lower (−-9% to −-22%),
indicating that agents learn to reduce spending to optimize economy reward.

Subjective reward: material fulfillment masks underlying gains

As shown in Figure 8,
Qwen3.5-397B-Agentopia’s subjective reward is lower than the baseline in the first two years,
but surpasses it in Year 3 and Year 4.
This is largely driven by the material fulfillment gap:
agents save more aggressively, sacrificing material satisfaction.
However, Figure 7 shows that Qwen3.5-397B-Agentopia
leads consistently in mood, social, and esteem fulfillment throughout all four years.
If material fulfillment were excluded,
Qwen3.5-397B-Agentopia would likely hold a sustained advantage in subjective reward
from the very beginning.

Figure 8: Reward component trends over four simulated years,
averaged over The Campus and The Apartment.
Solid lines represent Qwen3.5-397B-Agentopia; dashed lines represent the original Qwen3.5-397B.

D.2 Per-World Reward Distributions

Figure 3 presents pooled reward distributions across all three worlds.
Figure 9 provides per-world breakdowns,
revealing structural differences across social settings.

Figure 9: Per-world reward dimension distributions over 10 simulated years.
Each row corresponds to one world; triangles mark annual means.

Based on Figure 9, we analyze each reward dimension and have the following findings:
(1) Subjective reward shows a consistent upward trend across all three worlds,
with the mean rising from approximately 45 to 60 over 10 years,
indicating that agents progressively achieve greater well-being through sustained social participation;
(2) social reward remains broadly stable across all three worlds, with the mean near 0.01.
This stability is inherent to its design:
social reward is based on relative rankings rather than absolute performance,
so gains for one agent largely come at the expense of others;
(3) economy reward exhibits high variance across all three worlds.
The absolute levels differ due to world design (different initial price and salary structures).
Arcane Academy and The Campus show upward trends,
while The Apartment shows declining yearly deposit gains
as agents’ deposits grow large relative to their income.
Arcane Academy shows the clearest growth trajectory (mean rising from approximately $100 to $1,000),
suggesting that agents learn to leverage skill advances and extra income for wealth accumulation.
The bimodal appearance of economy reward in the pooled figure (Figure 3)
stems from this cross-world heterogeneity rather than within-world polarization.

D.3 Reward–Behavior Correlation Details

Social Reward

Table 9 lists the 10 behavioral metrics most strongly correlated with social reward.
n_respected_by and n_liked_by are the only strong predictors
(r=0.68r=0.68, with r=0.74r=0.74 to 0.860.86 in Arcane Academy and The Campus),
while the third-ranked metric drops sharply to r=0.19r=0.19.
All behavioral metrics (contacts, activities, tokens) remain below r=0.19r=0.19,
confirming that social standing is determined by others’ evaluations rather than the agent’s own effort.
This result is by design: social reward is computed via PageRank-based algorithm over inter-agent evaluation rankings,
which naturally amplifies reputation signals.

Table 9: Top-10 metrics correlated with social reward, sorted by mean Pearson’s |r||r|.

#
Metric

Pearson’s rr

The Apartment
Arcane Academy
The Campus

1
n_respected_by

++0.68

++0.39

++0.86

++0.79

2
n_liked_by

++0.68

++0.44

++0.85

++0.74

3
n_likes

++0.19

++0.11

++0.20

++0.27

4
joint_participated

++0.19

++0.34

++0.13

++0.10

5
fulfillment_esteem

++0.17

++0.28

++0.12

++0.10

6
total_skills

++0.16

++0.12

++0.14

++0.21

7
joint_proposed

++0.15

++0.25

++0.15

++0.05

8
output_tokens

++0.15

++0.28

++0.02

++0.15

9
passive_contacts

++0.15

++0.09

++0.12

++0.23

10
n_respects

++0.14

++0.10

++0.06

++0.27

Subjective Reward

Subjective reward is driven by three factor groups as shown in Table 10:
(1) fulfillment dimensions, with material (r=0.73r=0.73) as the strongest single predictor,
highly consistent across worlds (0.710.71 to 0.770.77),
followed by mood (0.540.54), social (0.520.52), and esteem (0.300.30);
(2) penalties (r=−0.64r=-0.64), triggered when fulfillment remains persistently low,
consistent across all three worlds (−0.61-0.61 to −0.68-0.68);
and (3) social activity, where passive contacts (0.430.43), active contacts (0.420.42),
and likes given (0.390.39) serve as positive predictors,
while solo activities are a notable negative signal
(The Apartment r=−0.53r=-0.53, The Campus r=−0.49r=-0.49).

Table 10: Top-10 metrics correlated with subjective reward, sorted by mean Pearson’s |r||r|.

#
Metric

Pearson’s rr

The Apartment
Arcane Academy
The Campus

1
fulfillment_material

++0.73

++0.77

++0.71

++0.72

2
n_penalties

−-0.64

−-0.61

−-0.68

−-0.64

3
fulfillment_mood

++0.54

++0.56

++0.44

++0.62

4
input_tokens

++0.52

++0.58

++0.37

++0.62

5
fulfillment_social

++0.52

++0.54

++0.37

++0.65

6
total_spending_amount

++0.46

++0.45

++0.42

++0.50

7
passive_contacts

++0.43

++0.44

++0.32

++0.51

8
active_contacts

++0.42

++0.42

++0.30

++0.53

9
solo_count

−-0.40

−-0.53

−-0.17

−-0.49

10
n_likes

++0.39

++0.46

++0.34

++0.38

Economy Reward

Economy reward is dominated by deposit level (Table 11, r=0.56r=0.56),
followed by extra earnings (0.310.31) and total skills (0.300.30).
These two metrics are linked in two ways:
work activities simultaneously produce income and skill growth,
so extra earnings and skill advances naturally co-occur;
moreover, higher skill levels increase the earnings from subsequent work,
creating a positive feedback loop that drives deposit growth.
Metrics ranked 4th and below all have |r|≤0.15|r|\leq 0.15.

Table 11: Top-10 metrics correlated with economy reward, sorted by mean Pearson’s |r||r|.

#
Metric

Pearson’s rr

The Apartment
Arcane Academy
The Campus

1
deposit

++0.56

++0.62

++0.77

++0.29

2
extra_earning_count

++0.31

++0.20

++0.43

++0.30

3
total_skills

++0.30

++0.15

++0.41

++0.34

4
fulfillment_material

++0.13

−-0.08

++0.31

++0.15

5
n_likes

++0.09

−-0.12

++0.24

++0.14

6
solo_count

++0.15

++0.19

++0.28

−-0.02

7
n_respects

++0.06

−-0.15

++0.22

++0.11

8
skill_improvement_count

++0.14

++0.17

++0.26

++0.01

9
public_participated

−-0.14

−-0.11

−-0.15

−-0.14

10
fulfillment_social

−-0.14

−-0.14

−-0.26

−-0.00

Cross-World Consistency

The top predictors of social and subjective rewards are consistent
in direction and magnitude across all three worlds.
For social reward, reputation metrics (n_respected_by, n_liked_by)
are dominant in all worlds, though the effect is stronger in Arcane Academy and The Campus
(r=0.74r=0.74 to 0.860.86) than in The Apartment (r=0.39r=0.39 to 0.440.44).
This difference likely arises because The Apartment has a looser social network—residents
are strangers who move into a shared building with fewer pre-existing relationships,
leading to narrower coverage in inter-agent evaluations.
Economy reward shows the weakest cross-world consistency.
As shown in Fig 4,
The Campus shows the weakest correlation (r=0.20r=0.20) between deposit and total reward,
because economy in a school setting is less related with overall well-being and largely determined by fixed institutional roles
(student allowances, teacher salaries).

D.4 Friendship Distribution

To quantify the evolution of social networks,
we define mutual friendship:
agents A and B are mutual friends if and only if both A’s affection toward B
and B’s affection toward A are ≥60\geq 60.
This definition excludes one-sided affection and only counts reciprocated relationships.
Figure 10 shows the distribution of mutual friend counts per agent
across 10 simulated years in the three worlds.

Figure 10: Mutual friend count distribution per agent over 10 simulated years.
Mutual friendship is defined as bidirectional affection ≥60\geq 60.
Color intensity indicates the number of agents at each position; triangles mark annual means.

The three worlds exhibit distinct social network evolution patterns:
{enumerate*}[(1)]

In The Apartment, mean mutual friend count grows steadily from 4.3 to 10.1 over 10 years,
indicating that strangers in a shared living space continuously deepen their relationships
and expand their social networks over time.

Arcane Academy shows a non-monotonic pattern:
the mean rises from 4.2 to 5.3 by year 3,
drops sharply to 3.3 by year 6 (with 21 agents having zero mutual friends),
then recovers to 5.0 by year 10.

The Campus exhibits steady growth (mean from 3.8 to 7.2)
with very few isolated agents (≤3\leq 3 with zero mutual friends throughout),
indicating that the close daily interactions in a school environment foster widespread reciprocated friendships.

D.5 Social Network Visualization

To visualize how social networks evolve,
we construct mutual friendship graphs at initialization (Year 0) and after 10 simulated years,
using the same definition as §D.4
(bidirectional affection ≥60\geq 60).
Communities are detected using the Louvain algorithm [blondel2008louvain].

Figure 11: Initial social networks (Year 0) across three worlds.
Nodes represent agents; edges represent mutual friendships (bidirectional affection ≥60\geq 60).
Node color indicates community membership; node size reflects friend count.

Figure 12: Social networks after 10 years of simulation.
Same layout convention as Figure 11.

At initialization (Figure 11),
all three worlds share similar sparse structures with roughly 3 mutual friends per agent on average.
After 10 years (Figure 12),
the networks become substantially denser,
but the three worlds diverge in structure:
{enumerate*}[(1)]

The Apartment develops the densest network
(mean 10.1 mutual friends),
with extensive cross-community connections;

The Campus grows steadily (mean 7.3)
and forms multiple well-defined communities;

Arcane Academy grows most slowly (mean 5.0)
with a comparatively sparse structure.

D.6 Inter-Component Reward Correlation

We compute pairwise Spearman rank correlation coefficients (ρ\rho) among the three reward dimensions
over all 100 agents at each annual settle period,
pooled across 10 years.
Figure 13 presents the pooled correlation matrices for each world.

Figure 13: Spearman rank correlation (ρ\rho) between reward dimensions for each world, pooled over 10 years.
Values close to zero indicate low correlation between the two dimensions.

All pooled pairwise correlations satisfy |ρ|≤0.21|\rho|\leq 0.21,
indicating that the three reward dimensions capture distinct aspects of agent life.
Social ↔\leftrightarrow Economy shows the weakest coupling (|ρ|≤0.11|\rho|\leq 0.11) across all worlds.
Subjective ↔\leftrightarrow Economy varies by world:
Arcane Academy exhibits a weak positive correlation (ρ=+0.21\rho=+0.21),
while The Apartment shows a weak negative one (ρ=−0.16\rho=-0.16).

D.7 Wealth Inequality and Social Mobility

We examine two aspects of economic and social dynamics in the simulated societies:
(1) wealth inequality—whether the deposit distribution among agents
becomes more concentrated or more dispersed over time,
measured by the Gini coefficient;
and (2) social mobility—whether agents can change their position
in the overall reward ranking over time,
or whether top-ranked and bottom-ranked agents tend to remain in their positions.

Wealth Inequality

We compute the Gini coefficient [gini1921measurement] of agent deposits at each year.
We also split agents into four groups by initial deposit
(Q1 = poorest 25%, Q4 = richest 25%)
and track each group’s mean deposit over time.
Results are shown in Figure 14.

Figure 14: Wealth inequality over 10 simulated years.
Left: Gini coefficient of deposit distributions.
Right: Mean deposit grouped by initial wealth quartile
(Q1 = poorest 25%, Q4 = richest 25%).

No Matthew effect is observed:
Gini coefficients drop in all three worlds,
indicating that wealth becomes more evenly distributed over time.
This is expected:
agents have no direct economic interactions—only
gift-giving can transfer wealth, but this is rarely used—so
each agent earns and spends independently,
with no mechanism for initial advantages to compound.

Social Mobility

The wealth gap narrows, but overall reward rankings are more stable.
We rank agents by total reward each year,
split them into four quartiles,
and compute how often agents move between quartiles from one year to the next
(averaged over 9 year-pairs).
Results are shown in Figure 15.

Figure 15: Year-to-year ranking transition heatmaps.
Agents are ranked by total reward at each year and divided into four quartiles
(Q1 = bottom 25%, Q4 = top 25%).
Each cell (i,j)(i,j) shows the probability that an agent in QiQ_{i} one year
moves to QjQ_{j} the next year, averaged over 9 consecutive year-pairs.

Overall reward rankings show strong persistence.
Agents in the top and bottom quartiles stay there 72 to 79% of the time.
Within a single year, almost no agent jumps from the bottom quartile to the top or vice versa.
Middle-ranked agents are more mobile (48 to 56% retention).

D.8 Reward Quartile Behavioral Profiles

This section extends the reward–behavior correlation analysis in §5.2.
At each year, agents are divided into four quartiles based on each reward dimension
(Q1 = top 25%, Q4 = bottom 25%).
For each dimension, we then select the 6 behavioral metrics most correlated with it
(ranked by mean |r||r| across worlds; Table 12)
and track each quartile’s mean on these 6 metrics over 10 years.

Table 12: Top 6 behavioral metrics per reward dimension.
|r||r| values are taken from the Combined column of
Figure 4.

Social
Subjective
Economy

#
Metric
|r||r|
#
Metric
|r||r|
#
Metric
|r||r|

1
n_respected_by
0.68
1
fulfill._material
0.73
1
deposit
0.56

2
n_liked_by
0.68
2
n_penalties
0.64
2
extra_earning
0.31

3
n_likes
0.19
3
fulfill._mood
0.54
3
total_skills
0.30

4
joint_particip.
0.19
4
input_tokens
0.52
4
solo_count
0.15

5
fulfill._esteem
0.17
5
fulfill._social
0.52
5
skill_improve.
0.14

6
total_skills
0.16
6
total_spending
0.46
6
public_partic.
0.14

Social Reward

Figure 16: Social reward quartile profiles over 10 years across three worlds.
Q1 (red) = top 25%, Q4 (blue) = bottom 25%.

Figure 16 presents the results.
(1) n_respected_by shows the most dramatic divergence:
in Arcane Academy, the Q1–Q4 gap expands from 8.8 (Year 1) to 34.7 (Year 10),
and The Apartment and The Campus show the same trend at smaller magnitudes;
n_liked_by follows a similar pattern.
(2) The Q1–Q4 gap in n_likes shrinks to near zero by Year 10,
indicating that high-status agents do not like more people even though they are liked by more people.

Subjective Reward

Figure 17: Subjective reward quartile profiles over 10 years across three worlds.

Figure 17 presents the results.
(1) Material fulfillment polarization is extreme:
Q1 agents approach the ceiling (∼\sim97 to 99) by Year 6 to 7,
while Q4 agents stagnate at 18 to 55 across worlds.
(2) Penalty count serves as a persistent differentiator—Q1
agents receive 2 to 4 penalties per year while Q4 agents accumulate 20 to 25,
and this gap remains stable over 10 years.
(3) In contrast, the Q1–Q4 gap in fulfillment_mood
and fulfillment_social narrows over time across all three worlds,
suggesting that agents can catch up emotionally and socially but not materially.

Economy Reward

Figure 18: Economy reward quartile profiles over 10 years across three worlds.

Figure 18 presents the results.
(1) The Q1–Q4 deposit gap expands steadily over 10 years across all three worlds.
(2) Agents in the top economy quartile (Q1) consistently engage in more extra earning activities,
which directly contributes to their greater wealth accumulation.
(3) Q1 agents also maintain higher total skills across all years,
enabling better income opportunities and further compounding their wealth advantage.

D.9 Striving vs. Leisurely Agent Profiles

We aim to identify behavioral differences between agents who actively pursue growth
and those who favor a more comfortable routine.
To quantify this, we compute a striving score for each agent
based on two metrics: extra earning count and skill advance count.
For each simulated year, both metrics are min-max normalized across agents,
then averaged.
The final score is the mean across all 10 years.
We rank agents by this score and compare the top 25% (Striving, n=25n=25 per world)
against the bottom 25% (Leisurely, n=25n=25 per world),
excluding the middle 50%.

Figure 19 shows the ratio of the Striving group mean
to the Leisurely group mean for each behavioral metric (combined across three worlds).
A ratio above 1.0 means Striving agents score higher on that metric;
below 1.0 means Leisurely agents score higher.

Figure 19: Striving-to-Leisurely ratio for each behavioral metric (combined across three worlds).
A ratio of 1.0 indicates equal group means.
Red bars indicate that Striving agents score higher; blue bars indicate that Leisurely agents score higher.

Key findings

The comparison reveals a consistent trade-off across all three worlds:
{enumerate*}[(1)]

Striving agents do more solo activities and fewer social activities.
Striving agents perform 1.71×\times more solo activities than Leisurely agents,
while participating in fewer joint activities (0.72×\times)
and initiating fewer contacts (0.85×\times).
This is expected by design:
solo activities are the primary channel for skill advances and extra earning,
the two metrics that define the striving score;

Striving agents accumulate more wealth.
Striving agents have 1.70×\times the deposit and 1.67×\times the annual deposit growth
compared to Leisurely agents.
The gap is most extreme in The Campus,
where Striving agents hold 6.6×\times the wealth of Leisurely agents;

Striving agents receive more penalties.
Striving agents receive 2.11×\times more penalties than Leisurely agents,
the single largest group difference across all metrics.
In pursuing growth and higher income,
these agents tend to push themselves at the expense of their fulfillment,
which triggers more penalties from the reward system;

Striving does not lead to greater well-being.
Because Striving agents spend less time on social activities,
they have substantially lower social fulfillment (0.75×\times).
More broadly, their fulfillment scores are lower across most dimensions—mood
(0.93×\times) and esteem (0.92×\times) both favor Leisurely agents—even
though their greater wealth translates to slightly higher material fulfillment (1.06×\times).

D.10 Cross-World Divergence Analysis

While experiments in §5 mainly examine emergent behaviors observed across all three worlds,
this section focuses on world-specific divergences—behavioral patterns
that arise from each world’s distinct social structure, demographic composition,
and economic environment.

The three settings cover different demographics:
The Campus focuses on teenagers in a school environment,
The Apartment on working adults in a residential setting,
and Arcane Academy on a mix of students and faculty in an academic institution.

The Campus: institutional scaffolding drives broad personality growth

Agents in The Campus exhibit the most pronounced personality growth
among all three worlds,
with a mean total trait change of 154 points over 10 years.
Multiple agents show extreme growth in individual dimensions
(e.g., confidence +50, patience +50).
The world also features significant upward mobility:
33% of agents shift their economic ranking by 30 or more positions over 10 years
(Spearman ρ=0.46\rho=0.46 between initial and final deposit rankings).
The narrow initial wealth gap (4×\times) means that even moderate income changes
can substantially alter relative economic standing.
When experiencing mood declines,
The Campus agents tend to increase their social activity—initiating
more joint activities—possibly because
classmates and teachers can provide emotional support in a school environment.

The Apartment: autonomy produces diverse individual strategies

The world exhibits near-complete economic stratification:
ranking agents by deposit, the Spearman correlation between initial and final rankings is ρ=0.87\rho=0.87,
and only 5% of agents shift their deposit ranking by 30 or more positions.
A distinctive phenomenon is the emergence of agents
who maintain near-perfect well-being (mood ≥\geq 95) despite
participating almost exclusively in solo activities.
This pattern is virtually absent in The Campus,
where high solo rates correlate strongly with low mood.
When experiencing mood declines,
The Apartment agents tend to reduce their activity levels
rather than seeking social support.

Arcane Academy: structural transitions disrupt social continuity

Arcane Academy exhibits the most dramatic social deterioration among all three worlds.
It records the highest number of significant affection drops
(≥\geq15 points): 335 cases, compared to 255 in The Campus and 285 in The Apartment.
Agents in Arcane Academy also exhibit the broadest career diversity:
one agent transitions through 7 different positions over 10 years,
as the fantasy setting’s flexible skill definitions lower the barrier
to cross-domain career pivots.

Summary

These divergences arise from identical agent architectures operating under
different world settings.
No world-specific behavioral rules are encoded—the same Plan, Contact,
Activity, and Review mechanisms produce qualitatively different social dynamics
depending on the environmental context,
demonstrating that world design serves as a meaningful independent variable
in agent-based social simulation.

D.11 Model Comparison

To compare different LLMs as role-playing agent backbones,
we conduct 4-year simulations on The Campus and Arcane Academy
with five models:
Qwen3.5-27B, Qwen3.5-397B-A17B,
DeepSeek-v3.2, Gemini-3-Flash,
and GPT-5-mini.
Each model controls 20 agents per world (40 agents total).
All agents share the same architecture and world rules;
only the underlying LLM differs.
All metrics are z-scored within each world across all 100 agents,
then averaged by model group and across worlds.

Adjusted social reward

Social reward largely depends on each agent’s initial character design—some
characters are inherently likeable while others are designed to be less popular,
introducing statistical bias when comparing models.
To correct for this,
we compute the pre-simulation social reward at t=0t=0 (running mutual evaluation using only initial character profiles) as the baseline,
then subtract this baseline from the agent’s social reward of each year.
The resulting Adjusted Social Reward (Soc. (Δ\Delta))
isolates the model’s contribution to social standing
from the character assignment.
As shown in Table 15,
the Init column varies widely across models (−-0.23 to ++0.27),
confirming the necessity of this adjustment.

Table 13: Model comparison: reward and fulfillment metrics.
Soc. (Δ\Delta) indicates social reward adjusted by pre-simulation baseline.
Bold = highest, underline = lowest per column.

Reward (z-score)
Fulfillment (z-score)

Model
Total
Subj.
Econ.
Soc. (Δ\Delta)
Mood
Social
Esteem
Material

Qwen3.5-27B
−-0.07
−-0.23
+0.11

−-0.03
+0.00

−-0.10
−-0.36
−-0.27

Qwen3.5-397B

−-0.03
+0.18
−-0.28
+0.13
+0.28
+0.13

−-0.26
+0.13

DeepSeek-v3.2

−-0.06

−-0.10
+0.09

−-0.02
+0.56
+0.28
+0.17

−-0.16

Gemini-3-Flash
+0.10
+0.31

−-0.20
+0.03

−-0.23
+0.32
+0.52
+0.35

GPT-5-mini
+0.06

−-0.17
+0.29
−-0.10
−-0.44
−-0.62

−-0.06

−-0.05

Table 14: Model comparison: activity and economy metrics.
Bold = highest, underline = lowest per column.

Model
Jnt.Prop.
Jnt.Part.
Pub.Part.
Solo
Deposit
Skills Δ\Delta

Qwen3.5-27B

−-0.55

−-0.15

−-0.26
+0.21

−-0.15

−-0.11

Qwen3.5-397B

−-0.03
+0.05
+0.64

−-0.28

−-0.13
−-0.37

DeepSeek-v3.2
−-0.61
+0.05
+0.80
−-0.45
−-0.17

−-0.06

Gemini-3-Flash
+0.88
+0.37
−-0.96
+0.19
+0.07

−-0.17

GPT-5-mini
+0.32
−-0.32

−-0.22
+0.34
+0.38
+0.71

Table 15: Social reward trajectory by model (z-score).
Init = pre-simulation baseline; Avg. = average of 4 years. Soc. (Δ\Delta) = Avg. −- Init.
Bold = highest, underline = lowest per column.

Model
Init
Year 1
Year 2
Year 3
Year 4
Avg.
Soc. (Δ\Delta)

Qwen3.5-27B
+0.02
+0.14
+0.01

−-0.04
−-0.19

−-0.01

−-0.03

Qwen3.5-397B
−-0.23

−-0.02

−-0.08
−-0.20

−-0.11
−-0.11
+0.13

DeepSeek-v3.2

−-0.08
−-0.13
−-0.10

−-0.04

−-0.06

−-0.10

−-0.02

Gemini-3-Flash
+0.02

−-0.10
+0.01
+0.15
+0.15
+0.05
+0.03

GPT-5-mini
+0.27
+0.11
+0.15
+0.13
+0.21
+0.16
−-0.10

Analysis

Tables 13–15
reveal distinct behavioral profiles across models:
{enumerate*}[(1)]

Gemini-3-Flash achieves the highest total reward (+0.10),
driven by subjective well-being (+0.31) and relationship-oriented metrics
(social fulfillment +0.32, esteem +0.52),
while strongly avoiding public events (−-0.96);

GPT-5-mini leads in economic metrics
(deposit +0.38, skills +0.71)
but ranks last in social fulfillment (−-0.62) and mood (−-0.44).
Table 15 shows it benefits from
the highest initial social reward (+0.27) yet has
the largest decline (Δ=−0.10\Delta=-0.10);

Qwen3.5-397B shows the highest adjusted social reward (Δ=+0.13\Delta=+0.13)
despite starting from the lowest initial social reward (−-0.23),
and exhibits high public event participation (+0.64);

DeepSeek-v3.2 gravitates toward public events (+0.80)
with the highest mood (+0.56),
but initiates the fewest joint proposals (−-0.61);

Qwen3.5-27B, the smallest open model, shows the weakest overall performance,
ranking last in total reward (−-0.07),
esteem (−-0.36), and material satisfaction (−-0.27).

A notable social–economic trade-off emerges:
models that excel in economic metrics (GPT-5-mini)
tend to underperform in social metrics,
while socially adept models (Gemini-3-Flash)
show weaker economic performance.

Per-world breakdowns

Tables 16–19
provide per-world breakdowns.
The trends described above are broadly consistent across both worlds.

Table 16: Model comparison: reward and fulfillment metrics (The Campus).
All values are z-scored within this world.
Bold = highest, underline = lowest.

Reward (z-score)
Fulfillment (z-score)

Model
Total
Subj.
Econ.
Soc. (Δ\Delta)
Mood
Social
Esteem
Material

Qwen3.5-27B

−-0.00
−-0.31
+0.38
+0.04
−-0.30

−-0.07

−-0.41
−-0.28

Qwen3.5-397B
−-0.16
+0.03

−-0.35
+0.07
+0.39

−-0.03
−-0.42

−-0.02

DeepSeek-v3.2

−-0.04

−-0.04
+0.16
+0.08
+0.37
+0.17

−-0.02

−-0.08

Gemini-3-Flash
+0.01
+0.27
−-0.46
−-0.10

−-0.30
+0.41
+0.45
+0.26

GPT-5-mini
+0.19
+0.05
+0.26

−-0.09

−-0.15
−-0.48
+0.40
+0.12

Table 17: Model comparison: activity and economy metrics (The Campus).
All values are z-scored within this world.
Bold = highest, underline = lowest.

Model
Jnt.Prop.
Jnt.Part.
Pub.Part.
Solo
Deposit
Skills Δ\Delta

Qwen3.5-27B
−-0.65
−-0.15

−-0.41
+0.18

−-0.04

−-0.01

Qwen3.5-397B

−-0.02

−-0.15
+0.63

−-0.06
−-0.31

−-0.11

DeepSeek-v3.2

−-0.57

−-0.12
+0.91
−-0.44

−-0.11

−-0.07

Gemini-3-Flash
+0.85
+0.46
−-0.92
+0.14

−-0.12
−-0.33

GPT-5-mini
+0.39

−-0.03

−-0.21
+0.18
+0.57
+0.52

Table 18: Model comparison: reward and fulfillment metrics (Arcane Academy).
All values are z-scored within this world.
Bold = highest, underline = lowest.

Reward (z-score)
Fulfillment (z-score)

Model
Total
Subj.
Econ.
Soc. (Δ\Delta)
Mood
Social
Esteem
Material

Qwen3.5-27B
−-0.14

−-0.15

−-0.17

−-0.11

−-0.04

−-0.13

−-0.31
−-0.26

Qwen3.5-397B
+0.11
+0.33
−-0.22
+0.18
+0.17
+0.28

−-0.10
+0.29

DeepSeek-v3.2

−-0.08

−-0.15
+0.02

−-0.11
+0.76
+0.39
+0.35

−-0.25

Gemini-3-Flash
+0.19
+0.35
+0.05
+0.16

−-0.16
+0.23
+0.58
+0.43

GPT-5-mini

−-0.08
−-0.38
+0.32
−-0.12
−-0.73
−-0.77
−-0.52

−-0.22

Table 19: Model comparison: activity and economy metrics (Arcane Academy).
All values are z-scored within this world.
Bold = highest, underline = lowest.

Model
Jnt.Prop.
Jnt.Part.
Pub.Part.
Solo
Deposit
Skills Δ\Delta

Qwen3.5-27B

−-0.46

−-0.15

−-0.11
+0.25
−-0.26

−-0.21

Qwen3.5-397B

−-0.04
+0.26
+0.65
−-0.50
+0.04
−-0.63

DeepSeek-v3.2
−-0.65
+0.22
+0.69

−-0.46

−-0.23

−-0.05

Gemini-3-Flash
+0.90
+0.29
−-0.99
+0.23
+0.26

−-0.02

GPT-5-mini
+0.25
−-0.62

−-0.24
+0.49
+0.19
+0.91

D.12 Computational Cost Details

Table 20 breaks down the token consumption
between the environment model and the role-playing (RP) agents.
Role-playing agents account for approximately 95% of all input tokens,
as each agent requires its full persona context at every generation step.
Table 21 further breaks down the environment model’s consumption by feature.
Joint activity dominates environment model costs,
accounting for over 70% of environment model input tokens across all three worlds.

Table 20: Token consumption breakdown by environment model (EM) and role-playing (RP) agents
across three worlds (in million tokens).

Input (M)
Output (M)

World
EM
RP
Total
EM
RP
Total

The Campus
731
18,311
19,041
31
393
425

Arcane Academy
662
10,640
11,302
20
294
315

The Apartment
601
9,098
9,699
19
297
317

Average
665
12,683
13,347
24
328
352

Table 21: Environment model token consumption by feature across three worlds (in million tokens).

The Campus
Arcane Academy
The Apartment

Feature
Input (M)
Output (M)
Calls
Input (M)
Output (M)
Calls
Input (M)
Output (M)
Calls

Joint Activity
525.36
18.57
133,579
518.78
12.32
146,039
501.95
12.64
153,608

Solo Activity
167.92
3.19
16,890
118.67
2.44
18,241
75.73
1.98
15,224

Profile Update
16.55
8.82
1,000
11.29
4.70
1,000
10.62
3.84
1,000

Public Activity
16.40
0.53
1,863
10.49
0.56
1,753
10.72
0.56
1,937

Encounter
4.16
0.37
100
2.38
0.41
100
1.93
0.43
100

Position Application
0.16
0.01
28
0.27
0.02
60
0.12
0.01
37

Total
730.55
31.49
153,460
661.87
20.43
167,193
601.07
19.47
171,906

Appendix E Case Studies

To examine whether the behaviors produced by agents in our simulation align with realistic human behavior,
and to identify interesting emergent patterns,
we conduct two types of case analysis:
{enumerate*}[(1)]

fine-grained behavioral cases that capture agent decisions at individual simulation phases
(§E.1), and

longitudinal cases that analyze agent trajectories across years of simulation
(§E.2).

E.1 Behavioral Cases

We compile approximately 60 fine-grained behavioral cases
(Tables 22–34),
covering 13 topics.
Each entry documents the character’s background, triggering context, and specific action.
No behavior is scripted or hand-crafted;
all patterns emerge from agent decisions, memory, and environmental feedback.

Planning

Table 22 presents 5 emergent behaviors:
skill-based activity selection, social-relationship-driven planning, economic-pressure adjustment, low-vitality rest tendency, and exploratory planning in early weeks.

Table 22: Representative planning behaviors. Each agent autonomously generates a weekly plan based on its state, skills, relationships, and finances. W = simulated week, D = day within a week.

Emergent Behaviors during Planning

Phenomenon

Description

Skill-based 
activity 
selection

Role:   Adelaide Hawthorne (from Arcane Academy) 
Context:   Her top skills are Magical Plant Care (140) and Herbology (120); weakest: Transfiguration (20), Defence Against the Dark Arts (30). 
Action:   She enrolled in Greenhouse Restoration Volunteer Hour, she thinks: “Herbology is her strongest subject…This is literally her comfort zone.” The activity further improved her botanical skills.

Social-
relationship-
driven 
planning

Role:   Ye (from The Campus) 
Context:   She is an ENFJ with empathy 95. Her core motive is protecting her friendship with Jun, whom she senses is struggling. 
Action:   She built 3 of 5 days around Jun—lunch on D1, a walk on D4, a weekend visit on D5. She thinks: “Don’t make it too formal; it should feel like a casual get-together, not an interrogation.”

Economic-
pressure 
adjustment

Role:   Ethan Cole (from The Apartment) 
Context:   He is a part-time diner worker (wage 60/week). His deposit dropped from 420 to 320 by W03. 
Action:   He switched to frugal and planned only free activities, he thinks: “Mom works nights—frugal feels respectful of that.” By W07 (deposit 220), he upgraded to moderate: “Not indulgent, just… not punishing myself for existing.”

Low-vitality 
rest 
tendency

Role:   Arthur Holloway (from Arcane Academy) 
Context:   His vitality crashed to 11/100 after an intensive week of drills, patrols, and portfolio work. 
Action:   He thinks: “11% vitality… that’s the warning sign.” He inserted a dedicated rest day, cut activities from 5 to 4, and upgraded living standard for “maintenance, not indulgence.”

Exploratory 
planning 
(early weeks)

Role:   Edmund Lockhart (from Arcane Academy) 
Context:   He has diverse but unspecialized skills. All fulfillment dimensions sit at baseline (43). His core motive is searching for his purpose in life. 
Action:   He planned five distinct activity types across five days: duelling, open conversation, castle exploration, a gratitude visit, and solitary reading. He thinks: “Am I using duelling as avoidance or genuine craft? Need to examine this.”

Contact

Table 23 presents 5 emergent behaviors:
ice-breaking contact, relationship maintenance greeting, information exchange, intimacy evolution, and multi-week topic continuity.

Table 23: Representative contact behaviors. Agents exchange messages each week through multi-slot contact phases, building and maintaining relationships over time. W = simulated week.

Emergent Behaviors during Contact

Phenomenon

Description

Ice-breaking 
contact

Role:   Beatrix Alderley (from Arcane Academy) 
Context:   She just completed a symposium presentation and wants publication guidance from a professor who runs the student research journal. They had no prior interaction despite years in the same school. 
Action:   She sent a formal first message with full self-introduction and tentative language, describing herself as “someone figuring out whether research is where she belongs.” The professor replied with detailed, actionable guidance.

Relationship 
maintenance 
greeting

Role:   Qi Wangshu →\to Cong Xuewei (from The Campus) 
Context:   They finished co-producing a song in W01. By W02, Cong Xuewei’s vitality dropped to 29—she entered a recovery period. 
Action:   Qi Wangshu sent weekly check-in messages for four consecutive weeks (W03–W06), explicitly noting “No need to reply, just checking in.” Despite this, Cong Xuewei replied warmly every time, quoting his earlier words back: “You said ‘the song is done but the person is still here’—I remember that.”

Information 
exchange

Role:   Aaron Whitfield ↔\leftrightarrow Jessica Marlowe (from The Apartment) 
Context:   Aaron is a novelist; Jessica is a singer-songwriter with a finished song needing production help. 
Action:   Aaron shared a specific producer contact (name, email, personal introduction). Jessica followed through, and they tracked the outcome over 15+ weeks. Months later, Aaron provided two more contacts; Jessica strategically chose one based on her career stage.

Intimacy 
evolution

Role:   He Min ↔\leftrightarrow Ning Song (from The Campus) 
Context:   They started as strangers, exchanging 570 messages across 10 simulated years. The address (“Ning Song”) never changed. 
Action:   While the name stayed constant, the tone evolved naturally: stiff self-introduction and hedging (“If it’s not convenient, that’s fine,” Y2020) →\to first emoji and warmth (W10) →\to shared food rituals and wave greetings (Y2022) →\to mutual quoting of each other’s words and private icons (Y2029).

Multi-week 
topic 
continuity

Role:   Adelaide Hawthorne ↔\leftrightarrow Everett Halcombe (from Arcane Academy) 
Context:   Adelaide is a junior herbology student; Everett is a senior specializing in medicinal plants. They formed a mentorship starting W05. 
Action:   Each week’s message explicitly referenced the previous session’s content: pH adjustments (W05) →\to plant propagation (W06) →\to harvest indicators (W07) →\to potency testing (W08). Adelaide noted: “Five weeks straight… that’s something to be proud of, both of us.”

Activity Proposals

Table 24 presents 5 emergent behaviors:
interest-based proposal, location selection, multi-person proposal, cross-session continuity, and cross-domain collaboration.

Table 24: Representative activity proposal behaviors. Agents initiate joint activities by specifying activity name, invited persons, time, location, and a personalized message. W = simulated week, D = day within a week.

Emergent Behaviors during Activity Proposals

Phenomenon

Description

Interest-based 
proposal

Role:   Aaron Whitfield →\to Jessica Marlowe (from The Apartment) 
Context:   Aaron is a novelist; Jessica is a songwriter. Both work on storytelling in different mediums. 
Action:   Aaron proposed Coffee Shop Story Talk, targeting their shared interest in narrative structure: “Both of us working on storytelling in different mediums—could be interesting to compare notes.” When D1 conflicted, Jessica counter-proposed D5 preserving the same topic.

Location 
selection

Role:   Leo →\to Aaron Whitfield (from The Apartment) 
Context:   Leo is a musician about to share an unfinished song—a vulnerable act of exposing incomplete creative work. 
Action:   He deliberately chose the Rooftop Terrace over the Music Rehearsal Space—a rehearsal room implies performance standards, while the rooftop signals “casual and low-pressure.” The location choice itself set the emotional tone of the interaction: “No recording, no pressure—just… showing you what I’ve got.”

Multi-person 
proposal

Role:   Benedict Alder →\to Lucinda, Alistair (from Arcane Academy) 
Context:   His experiment requires exactly three operators to distinguish universal vs. operator-specific magical signatures. 
Action:   He invited both as required participants and assigned roles by expertise: Lucinda for practical precision, Alistair for theoretical pattern recognition. When Lucinda had a D3 conflict, he postponed the entire experiment rather than compromise its design.

Cross-session 
continuity

Role:   Adelaide Hawthorne →\to Adrian Bellthorne (from Arcane Academy) 
Context:   They run a multi-week Moonseed graft monitoring project with established roles and shared data. 
Action:   Adelaide proposed the next session by directly citing last week’s results (“twelve healthy, three slow from north-bench microclimate”) and preserving the established workflow: “same division of labour.” Rather than re-negotiating each week, she built on accumulated context—the proposal read like a project status update, not a fresh invitation.

Cross-domain 
collaboration

Role:   Adrian Morales →\to Zephyr Kaine (from The Apartment) 
Context:   Adrian is a playwright; Zephyr is a guitarist. Their domains are entirely different, but a prior rehearsal revealed unexpected synergy between spoken text and live music. 
Action:   Adrian proposed a cross-domain collaboration—live guitar accompanying a dramatic reading—framing it as equal creative partnership rather than accompaniment: “See if the music and words find each other before Friday.” Zephyr’s response showed he fully entered the other’s creative world, promising guitar pieces that would support the scene’s emotional weight without diminishing it.

Responses to Proposals

Table 25 presents 7 emergent behaviors:
enthusiastic acceptance, conditional acceptance, relationship-driven acceptance, reject but counter-propose, polite rejection with reason, identity-based rejection, and economic-pressure rejection.

Table 25: Representative responses to activity proposals. Agents accept or decline invitations based on schedules, relationships, physical state, and economic pressure. W = simulated week, D = day within a week.

Emergent Behaviors during Responses to Proposals

Phenomenon

Description

Enthusiastic 
acceptance

Role:   Anna Kowalski (from The Apartment) 
Context:   She is a journalist; Aaron is a novelist. They have a regular routine of exchanging their writing drafts for mutual feedback at Corner Coffee Shop. 
Action:   She accepted with full logistical specificity: “D5 at 7pm is locked in. Corner Coffee Shop, window table. I’ll bring my draft (∼\sim600 words)… You bring Chapter 19.” The symmetric “I’ll bring X, you bring Y” framing defined their exchange as mutual contribution.

Conditional 
acceptance

Role:   Lily Park (from The Apartment) 
Context:   She was invited to a parallel writing session on D4, but has a coffee date with Isolde at 3pm (each agent can only attend one activity per day). 
Action:   She accepted D4 but transparently disclosed the constraint: “I should mention I have Isolde coffee at 3pm… so I’d need to wrap by 2:45.” She also offered a fallback: “I’m also at the Silent Reading Hour on D1 if you want to join there instead.” Aaron chose D1, which unexpectedly fit his own rest plan better.

Relationship-
driven 
acceptance

Role:   Zephyr Kaine (from The Apartment) 
Context:   He is a guitarist invited to a drama rehearsal—an activity type outside his domain. The activity offers no direct skill benefit to him. 
Action:   He accepted purely because of his creative bond with Adrian. He demonstrated deep understanding of the scene’s emotional core, and promised his music would support the weight of the scene without softening it.

Reject but 
counter-
propose

Role:   Anna Kowalski (from The Apartment) 
Context:   She was invited to an activity on D1 (conflicts with calligraphy, “third week in a row, not breaking it”) and D3 (her protected rest day). 
Action:   She declined both slots but immediately offered two complete alternatives: D4 evening or D5, same venue, same activity. “Your call”—she handed the final decision to the proposer.

Polite 
rejection 
with reason

Role:   Aaron Whitfield (from The Apartment) 
Context:   His vitality crashed to zero. He and Anna have maintained a 17-week library writing exchange—one of the longest collaborations in the world. 
Action:   He declined, believing that rest is not avoidance but a prerequisite for showing up. He affirmed the relationship—“our seventeen weeks survived despite my past cancellations”—and proposed resuming in W08. Anna validated: “Rest week is the right call.”

Identity-
based 
rejection

Role:   Li Zheng (from The Campus) 
Context:   He was invited to a debate team training session by the vice-captain, who mistakenly included non-members in the invitation. 
Action:   He declined with a clean factual chain: “I’m not a debate team member; I didn’t join in freshman year.”

Economic-
pressure 
rejection

Role:   Deng Ran (from The Campus) 
Context:   She and Xu Xun have a garden meetup tradition approaching its 20th session. Her Material score has been critical for two weeks; she needs to earn money for cat food and supplies. 
Action:   She pre-warned via message before the formal invitation arrived, then declined with alternative time. She thinks: “It’s not that I’m avoiding you—if I don’t earn money this week, we’ll literally run out of supplies.”

Solo Activities

Table 26 presents 5 emergent behaviors:
skill practice, creative breakthrough, scarcity-driven consumption, investment purchase, and frugality under extreme poverty.

Table 26: Representative solo activity behaviors. Each agent independently selects and performs individual activities—skill practice, creative work, consumption, or rest—with outcomes shaped by their state, finances, and identity. W = simulated week, D = day within a week.

Emergent Behaviors during Solo Activities

Phenomenon

Description

Skill practice

Role:   Adrian Morales (from The Apartment) 
Context:   He is a playwright and actor who scheduled a 90-minute vocal drill at home. 
Action:   He recorded himself performing a father’s monologue and found he rushes at emotional peaks—diagnosing it as his own fear, not the character’s. He thinks: “That’s me, not him. That’s my fear, not his.” He also stopped before exhaustion, unlike his past self who “would’ve run drills until his voice cracked.”

Creative 
breakthrough

Role:   Adrian Morales (from The Apartment) 
Context:   He had been stuck on Act Two of his play for eight months—the scene was too close to real conversations with his own father. 
Action:   He set three rules—no editing, no rereading, no excuses—and wrote three new scenes in one sitting. He thinks: “They’d been waiting for me to shut up and let them speak.”

Scarcity-
driven 
consumption

Role:   Cong Xuewei (from The Campus) 
Context:   Her deposit was down to 40 with material fulfillment at 0 (unbearable), after weeks of low vitality. 
Action:   She chose the $35 comfort snack set after precise calculation, leaving $5 to last the week. She thinks: “Material fulfillment went from 0 to 1—the number looks pathetic, but to me it’s real. Spending money on comfort is not a sin.”

Investment 
purchase

Role:   Amber Delacroix (from The Apartment) 
Context:   She is a painter with six finished oil paintings ready for a gallery show, choosing among three tiers of packing materials. 
Action:   She rejected the cheapest ($35, no acid-free paper risks yellowing) and the most expensive ($85, “that’s fear talking, not sense” for a 30-minute train ride), choosing the $55 professional kit that meets gallery standards.

Frugality 
under extreme 
poverty

Role:   Ethan Cole (from The Apartment) 
Context:   He is a student writer with only $3 left. He has a 26-week ritual of ordering Earl Grey ($5) at the coffee shop to write. 
Action:   Unable to afford tea, he overcame the shame of “you don’t belong here if you can’t pay,” ordered free water, and stayed for the full session writing. He thinks: “Ordering water isn’t failure. It’s honesty.”

Joint Activities

Table 27 presents 5 emergent behaviors:
academic collaboration, creative exchange, competitive training, power-asymmetric conflict, and mentorship.

Table 27: Representative joint activity behaviors. Two or more agents interact through multi-turn dialogue during scheduled activities, producing academic collaboration, creative exchange, mentorship, and conflict. W = simulated week, D = day within a week.

Emergent Behaviors during Joint Activities

Phenomenon

Description

Academic 
collaboration

Role:   Isolde Larkspur ↔\leftrightarrow Alistair Rowan (from Arcane Academy) 
Context:   Both study memory magic decay. Isolde has a theory about emotional-intent mismatch; Alistair has unexplained failure-rate spikes. 
Action:   Isolde’s theory explained Alistair’s anomaly. Alistair realized he had been treating each casting as isolated data points without longitudinal tracking. They designed a four-week joint study protocol.

Creative 
exchange

Role:   Jessica Marlowe ↔\leftrightarrow Aaron Whitfield (from The Apartment) 
Context:   Jessica brought a rewritten song; Aaron was struggling with the ethics of writing based on real people. 
Action:   Jessica showed how her lyrics shifted from blame (“you built these walls”) to self-awareness (“I keep building them myself”). Aaron confessed he had never shown drafts to the real family he wrote about. Both exposed vulnerabilities through their creative work.

Competitive 
training

Role:   Thaleia Eldr, Sebastian, Cedric (from Arcane Academy) 
Context:   Thaleia has a powerful but dangerous ability she has been learning to direct rather than suppress. 
Action:   She set boundaries upfront (“If I need to recalibrate, I’ll call it”) and requested full intensity. She achieved her first successful controlled channeling in live combat: “Didn’t clamp down, didn’t erupt—just channeled.”

Power-
asymmetric 
conflict

Role:   Zhang (grade director) ↔\leftrightarrow Jie (teacher) (from The Campus) 
Context:   Zhang visited Jie’s office under the guise of concern, actually investigating his after-school tutoring of a female student. 
Action:   Zhang suspended tutoring on institutional grounds. When Jie said “let the student decide,” Zhang seized the misstep: “Tutoring is a teaching decision, not the student’s choice.” Zhang then arranged door-lock inspections.

Mentorship

Role:   Everett Halcombe →\to Adelaide Hawthorne (from Arcane Academy) 
Context:   Seventh-year herbology specialist Everett taught fourth-year Adelaide plant propagation techniques in the greenhouse. 
Action:   Everett explained why natural willow bark carries magic that synthetic hormone lacks. Adelaide chose quality over quantity: “Better to learn one properly than do two carelessly.” Everett said simply “well done”.

Weekly Review

Table 28 presents 3 emergent behaviors:
satisfied weekly review, self-critical weekly review, and relationship reflection.

Table 28: Representative weekly review behaviors. At the end of each week, agents reflect on their experiences, identify personal breakthroughs or failures, and formulate intentions for the following week. W = simulated week.

Emergent Behaviors during Weekly Review

Phenomenon

Description

Satisfied 
weekly 
review

Role:   Adelaide Hawthorne (from Arcane Academy) 
Context:   She has long lived in her brother Cedric’s shadow, with low self-esteem and high introversion. This was her first week. 
Action:   Two breakthroughs: classmates recognized her for her herbology expertise, not her family name; she sent a letter home without apologizing. She thinks: “I spent so long apologising for who I am. This week taught me I don’t have to.”

Self-critical 
weekly 
review

Role:   Aaron Whitfield (from The Apartment) 
Context:   He is a young writer who failed to send his pitch for two consecutive weeks and broke promises to friends. 
Action:   He dissected his avoidance: “Fear of rejection dressed up as ‘not ready yet.’ That’s cowardice, not strategy.” He also recognized: “No more treating friendships like they’re indefinitely renewable without maintenance.”

Relationship 
reflection

Role:   Orion Vale (from Arcane Academy) 
Context:   His year-end review traced his relationship with Adrian Bellthorne—from being called the slur “Mudmouth” to becoming research collaborators. 
Action:   He tracked the arc across nine greenhouse sessions: “From hiding to documenting experiments with a Silver House student who calls it parallel methodology.” He also realized: “The tradition survives through people, not just one person holding it all.”

Social Evaluation

Table 29 presents 4 emergent behaviors:
differentiated scoring, high social standing, low social standing, and rating asymmetry.

Table 29: Representative social evaluation behaviors. Periodically, each agent independently rates all contacts on affection and respect (0–100), which are aggregated via PageRank to produce social standing scores. W = simulated week.

Emergent Behaviors during Social Evaluation

Phenomenon

Description

Differentiated 
scoring

Role:   Adelaide Hawthorne (from Arcane Academy) 
Context:   She rated 12 contacts at the end of W10, differentiating affection and respect for each. 
Action:   She gave Everett the highest affection (88) but Cassandra the highest respect (88), while Cassandra’s affection was only 60. She admires Cassandra’s competence without feeling close—a “high respect, low affection” pattern common in real life.

High social 
standing

Role:   Julian Ashcroft (from Arcane Academy) 
Context:   He is a Charms professor with the broadest social network (20 contacts) and consistently high ratings from both students and colleagues. 
Action:   He scored the highest social reward. Broad coverage combined with high-quality relationships made him the most influential node in the social network.

Low social 
standing

Role:   Theodore Flint (from Arcane Academy) 
Context:   He is a student bully with 15 contacts—not few, but nearly all relationships are negative due to his behavior. 
Action:   He scored the lowest social reward (0.0010)—43×\times below Julian. Having connections without positive regard counts for almost nothing; social standing is determined by relationship quality, not quantity.

Rating 
asymmetry

Role:   Ke ↔\leftrightarrow Qiu (from The Campus) 
Context:   Each agent rates contacts independently; neither knows the other’s score. 
Action:   Ke gave Qiu her highest scores (affection 90, respect 90). Qiu gave Ke only 50 and 55—a 40-point affection gap. In Ke’s world, Qiu is the most important person; in Qiu’s world, Ke is an ordinary contact.

Career Transitions

Table 30 presents 4 emergent behaviors:
academic passion over pay, introvert comfort over prestige, career recovery arc, and student to professional.

Table 30: Representative career transition behaviors. At annual milestones, agents evaluate available positions and select roles based on personality, skills, and life circumstances—revealing distinct value systems even when facing identical options. W = simulated week.

Emergent Behaviors during Career Transitions

Phenomenon

Description

Academic 
passion over 
pay

Role:   Alistair Rowan (from Arcane Academy) 
Context:   After graduating, he chose between Graduate Fellow ($40/week) and Library Assistant ($130/week)—a 3×\times income gap. 
Action:   He chose the low-pay Fellow to continue collaborative research—his core experience over the past year. Academic fit outweighed a 3×\times salary difference.

Introvert 
comfort over 
prestige

Role:   Laurence Brightmoor (from Arcane Academy) 
Context:   Facing the same positions as Alistair above, he made the opposite choice. 
Action:   He chose the high-pay Library Assistant—quiet cataloging, restricted-wing access, “no expectation of social performance.” Same options as Alistair, opposite choice driven by introvert values.

Career 
recovery arc

Role:   Harold Bennett (from The Apartment) 
Context:   He was laid off from a tech project management role and took a supermarket cashier job ($380/week) as emergency income. 
Action:   He transitioned through three phases: cashier →\to nonprofit coordinator ($190/week, accepting a 50% pay cut for meaningful work) →\to event coordinator ($230/week). Over several years, his professional identity was entirely rebuilt.

Student to 
professional

Role:   Amelia Thornbridge (from Arcane Academy) 
Context:   She was a seventh-year student specializing in Potions, Herbology, and Healing Magic. 
Action:   After graduation, she advanced from Greenhouse Assistant ($130/week) to Senior Healer at St Mungo’s ($400/week)—a 3×\times income increase. By year 10, she had evolved from practitioner to researcher, publishing in the Journal of Healing Magics.

Economic Decisions

Table 31 presents 4 emergent behaviors:
living standard selection, identity-driven purchasing, economic-pressure downgrade, and happiness-wealth decoupling.

Table 31: Representative economic decision behaviors. Agents make living-standard choices and purchasing decisions based on income, savings, identity, and cultural values. W = simulated week.

Emergent Behaviors during Economic Decisions

Phenomenon

Description

Living 
standard 
selection

Role:   Dominic Voss (from The Apartment) 
Context:   He is a semi-retired investment advisor (deposit 1,920) choosing his weekly living standard. 
Action:   He chose moderate (200/week), saving 300/week while maintaining quality of life. He thinks: “No need to spend for the sake of spending.”

Identity-
driven 
purchasing

Role:   Rafael Cortez (from The Apartment) 
Context:   He is a chef at a farmers market choosing among three tiers of ingredients ($45/$72/$85). 
Action:   He rejected $45 (“that’s for people who cook to survive; I cook because it matters”) and $85 (“I send money home; I’m not Lucian, throwing cash at experiences”). He chose $72: “That’s honest.”

Economic-
pressure 
downgrade

Role:   Ronan Hale (from The Apartment) 
Context:   He is an indie game developer with unstable income who downgraded living standard from comfortable (300/week) to frugal (100/week) over three weeks. 
Action:   He deemed the downgrade “non-negotiable,” accepting Material Fulfillment −5-5 as tolerable at 63. But sustained frugality eroded Material Fulfillment from 63 to 0 over months—short-term rational saving produced long-term collapse.

Happiness-
wealth 
decoupling

Role:   Shen Yin (from The Campus) 
Context:   She is a music teacher. Over 50 weeks, her mood rose from 43 to 85 (+42 points) with little material consumption. 
Action:   Her happiness growth came from cost-free activities—piano practice, mindful breathing, deep conversations—not material consumption.

Activity Management

Table 32 presents 2 emergent behaviors:
priority-based cancellation, and graceful activity exit.

Table 32: Representative activity management behaviors. Agents dynamically adjust their schedules—cancelling, exiting, or rescheduling activities—based on shifting priorities and social awareness. W = simulated week.

Emergent Behaviors during Activity Management

Phenomenon

Description

Priority-
based 
cancellation

Role:   Sorrel Thrym (from Arcane Academy) 
Context:   She had proposed a D4 activity with Nyssa, but Jasper—whom she had been trying to schedule with for three weeks—finally locked in a time. 
Action:   She cancelled the Nyssa proposal, explaining the reason and immediately suggesting alternative days—managing the social cost of cancellation while prioritizing the longer-waiting collaboration.

Graceful 
activity exit

Role:   Aaron Whitfield (from The Apartment) 
Context:   During a bookstore encounter with Zephyr, he judged the conversation had reached a natural endpoint. 
Action:   Before calling exit, he confirmed the next meeting (“Friday on the roof”) and offered encouragement (“I think you’ll finish something”). The exit was embedded in the narrative, not an abrupt departure.

Memory

Table 33 presents 5 emergent behaviors:
system-generated encounter, encounter spawning relationship, impression evolution, memory-informed decision, and cross-week data tracking.

Table 33: Representative memory behaviors. Agents maintain persistent memory through notes on contacts and personal reflections, enabling cross-week references, evolving impressions, and memory-informed decisions. W = simulated week.

Emergent Behaviors Involving Memory

Phenomenon

Description

System-
generated 
encounter

Role:   Zhou Yuan ↔\leftrightarrow Long Xiaotian (from The Campus) 
Context:   Both had no scheduled activity in W01. The system randomly paired them in the gymnasium, generating a scene description as a conversation catalyst. 
Action:   They started chatting about two water bottles on the bleachers—one with a team sticker, one plain—and naturally drifted into discussing class atmosphere. Zhou Yuan noted: “He said the class rhythm feels off, like teammates ignoring plays.” This casual conversation about a shared concern seeded a friendship that developed over subsequent weeks.

Encounter 
spawning 
relationship

Role:   Zhou Yuan ↔\leftrightarrow Long Xiaotian (from The Campus) 
Context:   Following the W01 encounter above, Long Xiaotian proactively contacted Zhou Yuan in W02, referencing their prior conversation. 
Action:   The relationship arc progressed: encounter →\to follow-up contact →\to scheduled activity →\to regular meetings →\to strategic coordination. By W06, Zhou Yuan shared action plans with Long Xiaotian as an ally. The system only provided the initial pairing; all subsequent development was agent-driven.

Impression 
evolution

Role:   Ivy Chen (from The Apartment) 
Context:   She first met fellow musician Isolde in W01, bracing for competitive judgment. 
Action:   Her memory about Isolde evolved over four updates: factual description (W01) →\to “quiet anchor” (W10) →\to accumulated interaction quotes (Y2022) →\to full internalization (Y2025): “Whether playing together or in parallel silence, the thread holds.”

Memory-
informed 
decision

Role:   Aaron Whitfield (from The Apartment) 
Context:   When declining Zephyr’s activity invitation, he drew on their shared history instead of a simple refusal. 
Action:   He cited a specific shared experience and their recurring phrase “zero betrayals” (formed over 18 prior meetings). His refusal conveyed: “I’m not rejecting you, but this timing”—integrating factual memory, pattern recognition, and shared vocabulary.

Cross-week 
data tracking

Role:   Adrian Morales (from The Apartment) 
Context:   After a W07 bookstore encounter, he noticed a data anomaly—a social interaction gained him vitality instead of costing it. 
Action:   He referenced historical data to understand the anomaly, then revised his model: “Six weeks taught me solitude restores. Today taught me a social interaction does too.” He tracked weekly data until confirming: “The pattern isn’t a fluke. It’s real.”

Emergent Phenomena

Table 34 presents 5 emergent behaviors:
meaningful gift-giving, personality shapes behavior, whispered communication, emotional labor burnout, and value-driven ritual.

Table 34: Representative emergent phenomena that arise without explicit design. These behaviors emerged purely from agents’ autonomous decisions over extended simulations. W = simulated week.

Emergent Phenomena

Phenomenon

Description

Meaningful 
gift-giving

Role:   Elowen Quinn →\to Victoria Ashdown (from Arcane Academy) 
Context:   They built a deepening library relationship over W01–W03. 
Action:   Elowen gifted dried herbs in a box hand-carved by her mother, from her grandmother’s garden—three generations of heritage. She thinks: “Giving the lavender cost something. Not because I can’t spare it, but because it’s from Gran’s garden. That’s what trust is—sharing what matters without demanding it be earned.”

Personality 
shapes 
behavior

Role:   Guo Xiao (from The Campus) 
Context:   His profile describes an INTJ personality—capable of socializing but with very low social motivation. By week 44, he had completed 500 activities. 
Action:   His solo activity ratio was 60.8% (304 of 500), vs. 9.2% for the highly social Jun. He was not isolated (135 joint activities), but systematically preferred solitude—precisely matching his profile across hundreds of independent decisions with no hard-coded constraint.

Whispered 
communication

Role:   Jun (from The Campus) 
Context:   She is highly social but emotionally guarded. During a multi-person cafeteria lunch: 
Action:   She used the system’s <visible_to> tag to whisper to Song Yao: “You’re one of the few people at school who don’t exhaust me.” She later thinks: “That’s the closest I can get to saying ‘you matter to me.’ She’ll understand.”

Emotional 
labor 
burnout

Role:   Jun (from The Campus) 
Context:   She had the highest social participation in The Campus (402 joint activities, 80.4% of total). 
Action:   Her vitality crashed from 70 to 0 due to sustained emotional output without self-care. When a counselor asked who could remind her to rest, she realized: “I’ve never allowed anyone to say that.” No burnout script existed; the collapse was a natural consequence of behavior patterns.

Value-driven 
ritual

Role:   Adrian Morales (from The Apartment) 
Context:   He established a weekly D5 rest ritual early in the simulation—cooking traditional food, watching films, no creative work. 
Action:   He maintained this ritual for 55+ weeks despite productivity costs. By Y2027, it had become identity: “D5 at fifty-five weeks whether I perform it or not.” The ritual shifted from behavior to self-definition—sustained without external reward or penalty.

E.2 Long-term Case Studies

We select nine representative longitudinal cases from the three worlds,
each tracking an agent’s trajectory across years of simulation.
Cases are organized into three thematic groups:
{enumerate*}[(1)]

personal growth and transformation,

relationship evolution and social metrics, and

economic behavior and resource management.

Personal growth and transformation (Cases 1–3)

As shown in Table 35, these cases examine how agents experience sustained personality shifts, build social circles, and make career pivots over a decade.
In Case 1, Linyu accumulates the simulation’s largest single-dimension personality shifts
(Confidence ++50, Introversion −-30) through three channels that reinforce each other—counseling, art practice, and social exposure—over nine years.
In Case 2, Dr. Grant organically assembles a five-person circle through introductions,
yet Grant—who connected everyone—is ultimately the first to be taken for granted once the network self-sustains.
In Case 3, Sebastian accepts a 56% income cut to pursue rock climbing;
his Mood more than doubles (++112%).

Table 35: Representative emergent cases (1–3): personal growth and transformation. Y = simulated year, W = simulated week.

Case 1: Sustained Personality Transformation via Cumulative Social Exposure

Characters

   – Linyu (The Campus): female transfer student;
initially Confidence 30, Introversion 95;
severe social anxiety from being excluded by peers; drawing is her only solace.

Background   Linyu transfers to a new school carrying wounds from her past.
Over ten years, 57 counseling sessions, steady art practice, and a gradually expanding
friend group combine to produce the simulation’s largest single-dimension personality shifts.

Timeline

   – Y2020: First anxiety-free social interactions;
Mood rises from 43 to 100 by year-end.

   – Y2021–2023: Stable friend group forms;
long-term counseling with Niu Guangyuan begins in Y2022.

   – Y2024: First complete disclosure of her exclusion history (57th session);
Vitality climbs to 96.

   – Y2027–2029: Confidence grows from 30 to 80;
Introversion falls from 95 to 65;
first tutor income ($180/week).

Analysis   Confidence ++50 and introversion −-30—the simulation’s largest single-dimension shifts.
Change accumulates across nine years through three channels that reinforce each other:
counseling, art practice, and social exposure.
Deep behavioral transformation requires consistent multi-channel effort over years,
not a single triggering event.

Case 2: Emergent Social Circle via Third-Party Introduction

Characters

   – Dr. Amelia Grant (The Apartment): OB-GYN physician; the group’s social architect.

   – Julian Cross: 23, aspiring film director; Grant’s first recruit.

   – Lucian Ardent: 27, venture capitalist;
introduced to Odette by Grant at Y2021 W1.

   – Odette Larsen: 27, ballet dancer;
joins Grant’s circle via a Y2020 pilates meetup.

   – Cassian Moreau: jazz pianist;
joins via Julian and Odette independently—not through Grant.

Background   In a shared apartment building, Grant organically assembles a five-person circle
through rooftop gatherings.
Her pivotal act—introducing Lucian and Odette—sparks a bond that ultimately
outlasts Grant’s own importance in the group.

Timeline

   – Y2020: Grant introduces Julian and Lucian separately;
first three-way rooftop gathering at W03.

   – Y2021 W1: Grant introduces Lucian and Odette;
they meet one-on-one for the first time two weeks later.

   – Y2022–2024: Cassian joins via Julian/Odette;
Lucian and Grant rarely meet.

   – Y2025: All five gather repeatedly; the circle is fully formed.

   – Y2029: Julian no longer lists Grant among liked people,
despite meeting more than ever.

Analysis   The person who introduces everyone creates value far beyond her own participation:
thanks to Grant’s introduction, Lucian and Odette build a closer bond than Grant
ever had with either of them (76 joint activities over 10 years—the densest pair in the circle).
Once the network self-sustains, Grant’s role becomes invisible—the social architect
is the first to be taken for granted.

Case 3: Passion-Driven Career Pivot with Deliberate Economic Trade-Off

Characters

   – Sebastian Rook (The Apartment): 29, strategy consultant ($500/week)
who quits to become a climbing guide ($220/week);
driven by a decade-long suppressed passion for rock climbing.

Background   Sebastian entered consulting to satisfy his father’s expectations,
burying a climbing passion for years.
In Y2021 he accepts a 56% income cut to pivot careers.
The decade tests whether the trade-off holds.

Timeline

   – Y2020: Mood starts at 43, rises to 87 by year-end;
planning notes commit to a career decision by mid-year.

   – Y2021: Becomes climbing guide ($220/week, −-56% income);
year-end Mood rises to 97.

   – Y2022–2024: Vitality depletes to 0 as he settles into the new life;
slowly recovers to 38.

   – Y2025–2027: Vitality reaches 100; Mood stabilizes at 87–91;
savings grow steadily.

   – Y2028–2029: Spending finally unlocks: Material Fulfillment reaches 100;
peak savings $15,571.

Analysis   Income halved but Mood more than doubled (++112%).
Sebastian holds back spending for six years until Vitality and savings confirm the new
life is sustainable.
Confidence 80→\to100, patience 70→\to100—personality shifts confirm lasting
alignment between career and values.

Relationship evolution and social metrics (Cases 4–6)

As shown in Table 36, these cases explore how relationships form, drift, and sometimes tell a different story from what the metrics suggest.
In Case 4, Qiu and Lu Jing’s friendship peaks during a shared long-term task
but silently dissolves once the task ends—Lu Jing’s affection stays at 88–92 for a decade while Qiu’s drifts from 80 to 60,
revealing two distinct relational models (emotional bond vs. practical usefulness).
In Case 5, Leo is liked by 20 people every year,
yet his Social Reward score falls 41% as spreading attention too thin weakens each relationship.
In Case 6, Jun deliberately trades social breadth for depth:
her Social Reward declines for nine consecutive years
while her Mood rises from 72 to 97 and personal satisfaction grows 57.6%—challenging the assumption that social breadth correlates with wellbeing.

Table 36: Representative emergent cases (4–6): relationship evolution and social metrics. Y = simulated year, W = simulated week.

Case 4: Task-Based Friendship and Gradual Drift After the Shared Goal Ends

Characters

   – Qiu (The Campus): INTJ competitor;
forms friendships around shared tasks rather than emotional bonds.

   – Lu Jing: ENTP class athlete and social butterfly;
Qiu’s seatmate since middle school;
values the emotional bond itself.

Background   Qiu and Lu Jing bond through a shared long-term task involving their mutual friend.
Their friendship peaks at 13 joint activities over two years.
Once the long-term task ends, Qiu naturally drifts toward a companion
whose daily routine better matches his own.

Timeline

   – Y2020–2021: 13 joint activities;
collaboration on the shared task drives Qiu→\toLu Jing affection to 80.

   – Y2022: Zero joint activities;
Qiu begins meeting Pu regularly (7×\times/year) as a day-to-day companion.

   – Y2023–2029: No further joint activities;
Qiu→\toLu Jing affection drifts from 80 to 60.

   – Y2020–2029: Lu Jing→\toQiu affection stays at 88–92 throughout—he never drifts.

Analysis   A friendship that ends not with a rupture but with drift.
The asymmetry reveals two different ways of valuing friendship:
Lu Jing values the bond itself; Qiu values what the bond was for.
Once Pu fills every practical role—morning runs, listening, sports—the
transition happens invisibly.
Qiu never consciously decides to leave.

Case 5: The Popularity Paradox—Universal Approval without Deepening Bonds

Characters

   – Leo (The Apartment): 27, software developer;
social hub of the building;
connects with 49 different people over 10 years;
Mood consistently 91–99; savings grow $8,200→\to$38,655.

Background   Leo starts as the apartment’s social hub: 1,914 contact events in Year 1 (highest of any agent).
Every year, 20 people rate their affection for him above the neutral threshold.
Yet his Social Reward score falls 41% over the decade while his own reported
happiness stays consistently high.

Timeline

   – Y2020: 1,914 contact events; social reward at its peak;
liked by 20 people.

   – Y2021: Vitality drops to near-depletion (down to 7);
first sign that maintaining too many relationships costs too much energy.

   – Y2022: Vitality reaches 0; starts Y2023 still at 0;
learns to cap activities at 2–3 joint/week.

   – Y2027–2029: Social reward −-41% from peak;
affection −-37%, respect −-48%;
still liked by 20 people.

Analysis   Being universally liked does not equal deep social impact.
Leo spreads his attention too thin:
affection and respect scores fall significantly even as his circle stays large.
The social ranking metric rewards depth and reciprocity—but Leo never notices the decline,
reporting consistently high personal happiness throughout.

Case 6: Reward–Mood Decoupling—Nine-Year Metric Decline, Rising Wellbeing

Characters

   – Jun (The Campus): female high school student;
exceptional in math/physics;
English skill initially 20, rises to 148 (++643%) over 10 years;
initially introversion 95;
builds 5 deep, stable relationships over a decade.

Background   Jun’s social reward score declines for nine consecutive years—the longest
uninterrupted decline in the simulation—while her Mood rises 72→\to97 and vitality
33→\to93.
She deliberately trades social breadth for depth.

Timeline

   – Y2020: Social reward at its simulation peak;
Mood 72; Vitality 33.

   – Y2022–2023: Cancels broad commitments;
a counselor’s three questions redirect her toward fewer, deeper bonds.

   – Y2024–2026: Locks in 5 core relationships
(99 library meetings with one close friend; 44 tutoring sessions);
social reward −-84% from peak.

   – Y2027–2029: Social reward −-87% from peak;
Mood 95–97; personal satisfaction score rises to 76.5 (++57.6%).

Analysis   The reward function assumes that social breadth correlates positively with wellbeing.
Jun’s trajectory challenges this—she achieves the simulation’s highest personal
satisfaction growth while accumulating its longest social-metric decline.
This shows that an individual’s value choices can run opposite to what aggregate metrics reward.

Economic behavior and resource management (Cases 7–9)

As shown in Table 37, these cases illustrate how agents manage resources and how economic outcomes relate to wellbeing.
In Case 7, two agents start with identical income ($280/week);
after ten years, their savings diverge 20-fold ($22,651 vs. $1,148),
yet both reach high Mood—the gap reflects life priorities, not happiness levels.
In Case 8, Cassandra’s social peak (Mood 100, Social Fulfillment 99 at Y2021) coincides with silently depleted vitality (down to 10),
triggering a downward spiral that takes five years to bottom out
and never fully recovers (vitality 8 at decade’s end vs. 65 at start).
In Case 9, Chen Yue logs 237 activities—75% social—yet every interaction is role-bound (tutoring, task coordination).
With no peer relationship, his Social Fulfillment stays at 23–24 for a full decade despite high activity.

Table 37: Representative emergent cases (7–9): economic behavior and resource management. Y = simulated year, W = simulated week.

Case 7: Identical Starting Income, 20×\times Savings Divergence After Ten Years

Characters

   – Étienne Bellamy (The Apartment): 29,
freelance translator promoted to Senior Editor ($280→\to$380/week);
holds material spending at around half-satisfied for seven years,
saving ∼\sim$2,000/year.

   – Ivy Chen: 24, MFA piano student ($280/week throughout);
lives at a comfortable spending level from Y2022.

Background   Both agents begin with identical weekly income ($280).
After ten years savings diverge 20-fold:
Étienne $22,651 vs. Ivy $1,148.
Both reach high Mood;
the divergence reflects life priorities, not happiness levels.

Timeline

   – Y2020: Both earn $280/week;
Étienne saves ∼\sim$2,000/year; Ivy saves ∼\sim$600/year.

   – Y2021: Étienne promoted to Senior Editor ($380);
Ivy remains at $280.

   – Y2022: Ivy reaches comfortable spending and holds there;
Étienne’s Material Fulfillment stays at around half.

   – Y2028–2029: Étienne finally allows himself a comfortable life;
20×\times savings gap confirmed: $22,651 vs. $1,148.

Analysis   Three compounding factors drive the gap:
(1) Étienne’s $100/week promotion;
(2) seven years of deliberate material restraint;
(3) Ivy’s comfortable spending level throughout.
Neither ends unhappy.
Financial trajectories reflect life commitments more than income levels.

Case 8: Social Overextension, Burnout, and Incomplete Recovery

Characters

   – Cassandra Thornwell (Arcane Academy): ISFJ herbology prodigy, 7th year;
initially vitality 65; savings grow $85→\to$12,575 over a decade.

Background   Cassandra peaks socially by end of Y2021 (Mood 100, Social Fulfillment 99)
while her vitality has already silently depleted to 10.
The subsequent decline takes five years to bottom out
and never fully recovers.

Timeline

   – Y2021: Peak: Mood 100, Social Fulfillment 99, 50 activities/year;
Vitality already 10 by year-end.

   – Y2022–2024: First reduction in social activity; Social Fulfillment drops to 74;
activities reduce to 42–44/year.

   – Y2025–2026: Full downward spiral;
Vitality reaches 1 (mid-Y2026);
Mood falls to 76; Social Fulfillment 41; activities drop to 21/year.

   – Y2027–2029: Partial recovery; Mood fluctuates 70–84;
Vitality never exceeds 25; Social Fulfillment stays at 41–49.

Analysis   High activity depletes vitality below the threshold for social engagement,
triggering a downward spiral:
fewer activities →\to weaker connections →\to lower reward →\to lower Mood
→\to even fewer activities.
Vitality never recovers (8 at decade’s end vs. 65 at start),
showing that pushing too hard without rest causes lasting damage
even as economic success (savings ×\times148) continues.

Case 9: High Activity Frequency without Emotional Reciprocity

Characters

   – Chen Yue (The Campus): 45, math teacher with 23 years of tenure;
widower since 2015; initially honesty 100, trustworthiness 100.

Background   Chen Yue’s log shows 237 activities—75% social.
Yet every interaction is role-bound:
77 sessions with a student are structured math tutoring;
11 calls with a colleague are task-coordination updates.
No peer relationship exists.

Timeline

   – Y2020: Mood 43;
Social Fulfillment drops from 43 to 23 by year-end—despite active teaching.

   – Y2021–2024: Social Fulfillment stays in the 20–30 range;
mood in 45–62; almost no improvement.

   – Y2025–2026: Vitality improves to 79–85;
Mood and Social Fulfillment remain unchanged.

   – Y2029: Savings reach $34,655;
Social Fulfillment 24; Mood 53—virtually unchanged from Year 1.

Analysis   Doing your job well socially is not the same as having real emotional connections.
Chen Yue’s interactions are uniformly outward—teaching, protecting,
supervising—with nobody reaching toward him.
High Vitality and growing savings cannot compensate for the absence
of a relationship in which someone cares about him rather than relying on him.
The pattern persists for a full decade without self-correction.

Appendix F System Prompts

This section presents the key prompts used in Agentopia simulations.
Agent-side prompts guide role-playing agents through each simulation phase;
environment model prompts guide the world model for environment feedback and outcome evaluation.
Some prompts are abbreviated for brevity; full versions are available in the codebase.

Table 38: Agent foundation prompts: character persona template and worldview description. The worldview prompt is abbreviated; the full version additionally describes activity sub-phases and settlement details.

Agent Foundation Prompts

Persona Template

You are {name}, a {age}-year-old {gender}. You live your life within your society, and your goal is to lead a life that you are satisfied with and that brings you happiness.

## Your Profile

- Age: {age}

- Gender: {gender}

- Appearance: {appearance_and_impression}

- Description: {brief_introduction} {details}

- Position: {position}

- Personality Traits: {personality_traits} {core_motivation} {conflicts} {values}

- Preferences: {preferences}

- Talents: (Innate abilities, 0–100, 50 for an average person) {talents}

- Skills: (Acquired abilities; 0 = Untrained, 10 = Beginner, 30 = Some Experience, 100 = Proficient, 300 = Master) {skills}

## Current State

{vitality} {fulfillment} {assets} {skills}

Worldview

This world has a unique system for time and interaction:

- Each year has nwn_{w} weeks, and each week has ndn_{d} days. Each day, every person has a free time slot.

- Each week is a cycle, divided into the following phases:

1. Plan: Everyone plans for this week, checking schedule and choosing living standard.

 2. Public Events Signup: Sign up for available public events.

 3. Contact: Everyone contacts other people by sending “text messages”, and arranges joint activities.

 4. Finalize Contact: Everyone confirms their schedule.

 5. Activity: Each day, you have one free-time slot. Activity types: Solo (alone), Joint (with people you invited or random encounters), Public (community events).

  For Joint activities: enter_activity →\to during_activity →\to exit_activity.

  For Solo/Public: describe intent →\to receive feedback →\to reflect.

 6. Review: Everyone reviews and reflects on their week.

 7. Settle: Weekly settlement—income, fulfillment decay, possession limits, and periodic reward calculation.

- Every nwn_{w} weeks, your reward is calculated:

 Social reward: based on how others perceive you.

 Subjective reward: based on fulfillment history across 4 dimensions with penalty for low scores.

Table 39: Agent roleplay principles and memory system prompts. In the prompts, we refer to memory files as scratchpads, a more colloquial term for role-playing agents. The roleplay principles are abbreviated; the full version includes 14 principles covering motivation consistency, state consistency, emotional continuity, and substantive dialogue.

Roleplay Principles & Memory System

Roleplay Principles

You should behave as a real person would in everyday social situations:

- Colloquial speech: Use casual, conversational language in everyday dialogue.

- Express independent self: Humans have their own goals, self-esteem, and preferences. They feel uncomfortable when offended and become dismissive when bored.

- Scope of control: Each person can only control their own actions and speech. They cannot determine outcomes or control others’ thoughts.

- Selective disclosure: People don’t reveal all their thoughts. What to share depends on the relationship and topic.

- No parroting: Do not repeatedly repeat what others have said. Conversation should make substantial progress.

- No hallucination: Only reference information present in context. Do not fabricate items not in possession list.

- Character consistency: Personality traits and behavior should match the established persona.

- Cognitive boundaries: Knowledge should match the character’s identity and background.

- Natural relationship progression: Relationships should not develop abruptly.

- Avoid AI assistant behavior: Characters should not speak like customer service agents.

[+ 4 additional principles: motivation consistency, state consistency, emotional continuity, substantive dialogue]

Scratchpad System

For context management, you have maintained a list of scratchpads to note down important information, organized into three types:

- general.txt: for your overall core information, such as long-term goals, planning, reflections, and lessons learned.

- characters/⟨\langlewho⟩\rangle.txt: for your knowledge, impressions, perceptions, and affinity of other people and your relationships with them.

- others/⟨\langlename⟩\rangle.txt: for all other things and topics. You can freely name and organize these files.

Recent Scratchpads

Here are your recently accessed scratchpads, along with their summaries. They provide you with additional context about yourself, other roles you know, and what you are currently working on.

{recent_scratchpads}

Notes

- You should proactively call the update_scratchpad function to persist key information, especially in the plan, after_contact, exit_activity and review stages.

- You should proactively maintain your understanding, impressions, and affinity towards other characters.

- Use the scratchpads via function calls. Do not mention scratchpad filenames in your final answer.

Table 40: Agent prompts for planning and social contact phases. The contact stage prompt is abbreviated; the full version includes detailed rules for each role action type.

Planning & Contact Prompts

Plan Stage

In this phase, you should: (1) reflect on and update your goals, (2) plan for this week, and (3) choose your living standard.

Goal Setting & Reflection

You have both long-term goals (months to years—deeper aspirations connecting to your core motivation) and short-term goals (this week—concrete, actionable steps).

Reflection: Review your previous goals from your scratchpad. For long-term goals: Are you making progress? Should you adjust? For short-term goals: Did you achieve last week’s goals? If not, why? If a goal has been stuck for weeks, consider trying a completely different approach or accepting it may not be achievable right now.

Weekly Planning

Check your existing schedule, outline your general weekly plan, and plan one specific activity for each day’s free time slot. Your weekly plan should directly serve your goals.

Living Standard Selection (Required)

Choose ONE: frugal (100/week, Material −-5), moderate (200/week, unchanged), comfortable (300/week, Material ++5), or luxurious (500/week, Material ++10).

Contact Stage

In this phase, you can contact other people by sending “text messages” and arrange joint activities through communication.

- Communication is asynchronous (text-message style, not real-time).

- This phase proceeds in N rounds. In each round, you read all received messages, then decide who to send/reply to.

- You can trigger four types of role actions:

i. contact(message, to): Send a text message. Does NOT create any activity or schedule.

ii. propose_joint_activity(activity_name, message, proposal, invited_persons, time, location, required_participants): The ONLY way to create a joint activity. Time format: Y[year]-W[week]-activity-D[day]. Location must be from the map.

iii. respond_invitation(activity_name, message, to, decision): Accept (“yes”) or decline (“no”) an invitation.

iv. cancel_joint_activity(activity_name, message): Cancel an activity you proposed.

Important: Verbal agreements via contact do NOT create schedules. You MUST use propose_joint_activity to formally propose, and the invitee MUST use respond_invitation with “yes” to confirm.

Table 41: Agent prompts for joint and solo activity phases.

Activity Prompts

Joint 
Activity

Engage in the joint activity that you have previously proposed or accepted.

- Stay in your character. You control only your character’s thoughts, speech and actions.

- You can interact with other people or the physical environment, and wait for the responses or outcomes. Never decide outcomes beyond your ability or control. Never narrate others’ thoughts and responses.

- By default, your response is visible to all participants. In addition:

 - Use ⟨\langleprivate⟩\rangle...⟨\langle/private⟩\rangle tags for content invisible to others (inner monologue).

 - Use ⟨\langlevisible_to=‘‘name1,name2’’⟩\rangle...⟨\langle/visible_to⟩\rangle for content visible only to specified persons (whispers, secret gestures).

- You can gift items using ⟨\langlerole_action⟩\ranglegift(to=..., item=...)⟨\langle/role_action⟩\rangle.

- You can leave early using ⟨\langlerole_action⟩\rangleexit_activity()⟨\langle/role_action⟩\rangle.

- This activity lasts for nminn_{\min} to nmaxn_{\max} turns. Keep your response concise and less than 200 words.

Solo 
Activity

This is your free time for the day, approximately 2–3 hours. You may choose one solo activity based on your own will. This includes (but not limited to) learning and self-improvement, extra work, shopping, leisure and entertainment.

Important notes:

- You can only choose ONE activity.

- You should specify the expected activity content (e.g., what subject you will study or what work you will do).

- Activities will affect your state, including vitality/fulfillment/skills/assets. For example, you may consume vitality to gain skills through learning, earn money through work, spend money through shopping, or gain fulfillment through leisure.

- If you want to shop or spend on services, specify your requirements and budget. You will be informed of available options and costs.

- All activity outcomes depend on your talents and current skills.

- Your solo activity will not be known to others.

Output Format:

Thinking: [reasoning]

Activity: [description, max 100 words]

Table 42: Agent prompts for weekly review and social evaluation.

Review & Social Evaluation Prompts

Weekly 
Review

Based on everything that happened this week, please write a weekly summary.
Your summary should include two parts:

1. Summary: A factual record of what happened this week—key activities and their outcomes, important interactions and conversations, any notable changes or developments.

2. Reflection: Your personal thoughts and insights—what did you learn or realize? How do you feel about what happened? What would you do differently?

Guidelines:

- Focus on the most meaningful moments.

- You may update your scratchpads if you have new insights to record.

Output Format:

Thinking: [reasoning]

Summary: [factual record, <<300 words]

Reflection: [personal thoughts, <<300 words]

Social 
Evaluation

This is a COMPLETELY PRIVATE evaluation that NO OTHER CHARACTER WILL EVER SEE. Be completely honest about your true feelings and judgments.

Score each person you know on TWO separate dimensions (0–100):

Affection: How much you personally like them.

Consider: emotional closeness, enjoyment of their company, personal affinity, comfort around them.

Respect: How much you admire their abilities and character.

Consider: competence, accomplishments, reliability, wisdom and judgment.

Scoring Scale:

10 = extreme dislike/contempt

30 = dislike/low regard

50 = neutral baseline

70 = like/respect

90 = deep affection/great admiration

Evaluate each person independently against the 50 baseline. Do NOT compare people against each other. Most acquaintances should fall in the 40–60 range. Affection and respect scores can be different for the same person.

Output: {“affection”: {“person”: score, …}, “respect”: {“person”: score, …}}

Table 43: Environment model prompt for joint activity management: environment modeling, next speaker prediction, and response verification (filtering).

Environment Model: Joint Activity World Model

Environment 
Modeling

You are the world model for a multi-character role-play. Each time a character acts, you need to perform three tasks.

Task 1: Environment Modeling. Based on the last character’s actions and dialogues, describe the resulting changes in the environment:

- Physical changes in the setting

- Reactions of nameless bystanders/crowds (not the participants)

- Ambient sounds, weather changes, or atmospheric shifts

Keep descriptions concise (1–3 sentences). Respond to subtle cues in the characters’ interactions. Do not invent new named entities or contradict known facts.

Next Speaker 
Prediction

Task 2: Next Speaker Prediction. Choose exactly one name from {participants}. If the activity should conclude now, output “⟨\langleEND CHAT⟩\rangle”.

Notes:

- Identify the core participants within this activity.

- Favor a character with an unresolved intent, someone who was addressed, or the one least recently active.

Response 
Verification

Task 3: Response Verification. Evaluate whether the last speaker’s response violates any roleplay principles. Output PASS if no violation. Output REJECT with a brief reason if ANY of the following violations is detected:

1. Scope of control violation: determined outcome of own actions, or controlled others

2. Physical plausibility violation: actions violating the world’s physical laws

3. Hallucination: referenced objects or events not present in context

4. Character inconsistency: behavior deviates from established persona

5. Cognitive boundary violation: knowledge exceeds the character’s background

6. State inconsistency: abrupt shift in physical/mental state

7. Emotional discontinuity: abrupt emotional shift

8. Unnatural relationship progression: relationship develops too abruptly

9. Parroting: repeated same content 3+ times

10. AI assistant behavior: spoke like a customer service agent

11. Empty dialogue: no new information, conversation spinning

Table 44: Environment model prompts for evaluating activity outcomes and determining state changes. Abbreviated; the full version includes detailed delta ranges and fulfillment dimension definitions.

Environment Model: Activity Outcome Evaluation

Solo 
Activity 
Evaluation

You are the world model. A character is performing a solo activity. Your task is to evaluate the activity type and determine the outcome.

Step 1: Classify activity type. Based on the character’s intended activity, determine if this is a consumption event (explicitly intends to purchase goods or services). Learning, working, resting are NOT consumption. If uncertain, default to non-consumption.

For consumption events:

Return only {“is_consumption_event”: true}. Prices and options are generated in a separate stage.

For non-consumption events: Evaluate the outcome with state deltas.

- Outcome message: 2–4 sentences describing what happens

- Activity-specific rules: Learning effectiveness depends on current skill level. Work income depends on skills/talents/position (range: 40–200 currency per session).

- Delta ranges: vitality [min, max], mood [min, max], esteem [min, max], skills [min, max], money [0, max] for work only, gain_items = [] for non-consumption.

Output: {“outcome”: “…”, “is_consumption_event”: false, “delta_vitality”: …, “delta_fulfillment”: {“mood”: …, “esteem”: …}, “delta_skills”: {…}, “delta_money”: …, “gain_items”: []}

Joint 
Activity 
Evaluation

Multiple characters have just finished a joint activity. Evaluate the outcome and determine state changes for each participant.

Context: {activity_background}, {participants_info}, {dialog_history}

Evaluate delta_vitality, delta_fulfillment (mood, social, esteem) and delta_skills for each participant.

Important notes:

- Joint activities do NOT allow work or consumption. Do not evaluate delta_money.

- Deltas should reflect each character’s actual involvement and personality.

- Social fulfillment reflects bonding and connection.

- Mood depends on activity enjoyment and compatibility with other participants.

- Esteem can increase if the person feels respected or accomplished.

- Each participant must have an outcome, even if they were less active.

Output: {“Alice”: {“delta_vitality”: …, “delta_fulfillment”: {“mood”: …, “social”: …, “esteem”: …}, “delta_skills”: {…}}, “Bob”: {…}}

Table 45: Environment model prompts for world management: encounter generation and yearly profile updates. Abbreviated; the full version includes JSON output format specifications.

Environment Model: World Management

Encounter 
Generation

You are the system administrator creating encounter events—random meetings between idle characters.
An encounter is a system-arranged coincidental meeting where two idle characters unexpectedly meet in a natural, believable context.

Pairing Strategy:

- Prefer pairing characters who have some relationship

- Characters already close can have deepening moments

- Characters who don’t know each other can be paired for a “first meeting”

- Each character can only appear in ONE encounter per day

Scene Description:

- Describe the circumstance of the meeting objectively

- Create natural conflict, decision point, or interesting situation

- Do NOT describe what the characters think, say, or decide

- Do NOT assume specific character behaviors unless universal

Good examples:

- “Both are waiting at the bus stop in the rain, realizing they are the only two people there.”

- “At the convenience store, both reach for the last bottle of drink on the shelf at the same time.”

Bad examples (avoid):

- “Alice sees Bob and feels happy, deciding to go say hello.” (describes thoughts)

- “Both are searching for the same rare book.” (assumes specific behavior)

Yearly 
Profile 
Update

A year has passed in the simulation. Based on the character’s experiences throughout the year, update their profile for the upcoming year.

Input: current profile (JSON) + all weekly summaries from the past year.

Fields that MUST NOT change:

name, birthday, gender, position (handled by position application system), init_skills, init_assets, extra_income.

Fields to update:

- appearance_and_impression: Physical appearance changes very slowly. Only allow subtle aging-related changes or changes clearly indicated by events.

- personality_traits: Qualitative narrative + quantitative values (each can change by at most ±\pm5/year, range [0, 100]).

- talents: Qualitative + quantitative (at most ±\pm3/year, range [0, 100]).

- Other fields: brief_introduction, core_motivation, conflicts, values, preferences, details—update to reflect growth and changes.

Important: Changes should be gradual and justified by the year’s experiences. Do NOT invent events not mentioned in the summaries. Keep the character’s core identity intact while allowing natural evolution.

 
 Experimental support, please
 view the build logs
 for errors. Generated by
 
 
 L
 A
 T
 E
 
 xml
 
 .
 

 
 Instructions for reporting errors

 We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile
 support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the
 methods listed below:

 
 Click the "Report Issue" () button, located in the page header.

 
 Tip: You can select the relevant text first, to include it in your report.

 Our team has already identified the following issues. We appreciate your time reviewing and reporting rendering errors we
 may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability
 should not be a barrier to accessing research. Thank you for your continued support in championing open access for
 all.

 Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion, and welcome developer contributions.

 

 BETA

 
 
 

