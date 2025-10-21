# RoCoBench

## 📊 Benchmark Details

**Name**: RoCoBench

**Overview**: RoCoBench is a 6-task benchmark for multi-robot manipulation collaboration scenarios introduced to evaluate the flexibility and generality of LLM-based multi-robot coordination and motion-planning methods. It is accompanied by a text-only dataset (RoCoBench-Text) for evaluating agent representation and reasoning.

**Data Type**: multimodal: MuJoCo simulation trajectories (robot joint trajectories and task-space waypoints) and text question-answer pairs

**Domains**:
- Robotics
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://project-roco.github.io)
- [Resource](https://arxiv.org/abs/2307.04738)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate multi-robot manipulation collaboration capabilities (task-level coordination and action-level motion planning) across diverse collaboration scenarios using a 6-task simulated benchmark and an accompanying text-based reasoning dataset.

**Target Audience**:
- Robotics Researchers
- Machine Learning Researchers

**Tasks**:
- Multi-Robot Manipulation
- Motion Planning
- Question Answering
- Human-Robot Collaboration
- Agent Representation and Reasoning

**Limitations**: Assumes accurate perception (oracle state) in simulation which may not hold in real-world settings; open-loop execution of planned trajectories can lead to execution-level errors; relies on querying pre-trained LLMs for every dialog response which can be costly and introduce latency.

## 💾 Data

**Source**: Simulated MuJoCo environments for six multi-robot collaboration tasks (built with MuJoCo and using DMControl, Menagerie, and MuJoCo object assets). RoCoBench-Text is derived from evaluation runs on RoCoBench and contains additional authored question-answer items to evaluate agent representation and reasoning.

**Size**: 6 simulated tasks; RoCoBench-Text contains question counts per category as stated: 57 Self-knowledge questions, 44 Memory questions, 41 Inquiry questions, 96 Responsiveness questions, 31 Adaptation questions.

**Format**: MuJoCo simulation scenes and logs (simulation configurations, robot joint trajectories, task-space waypoint lists) and text question-answer pairs (QA items for RoCoBench-Text).

**Annotation**: Author-designed question-answer pairs with a single correct answer per question (RoCoBench-Text); task outcomes and runs recorded from simulation and real-world experiment logs.

## 🔬 Methodology

**Methods**:
- Automated evaluation in simulation (multiple runs per task)
- Real-world experiments with human-in-the-loop
- Ablation studies
- Comparative evaluation against an oracle LLM-planner baseline

**Metrics**:
- Task Success Rate
- Number of Environment Steps
- Average Number of Re-plan Attempts
- Question-Answering Accuracy
- Planning Success Rate
- Average Number of Attempts
- Planning Time (seconds)

**Calculation**: Task metrics computed over repeated runs: averaged success rates (reported over 20 runs per task for main simulation results), average number of environment steps in successful runs, and average number of re-plan attempts across runs. RoCoBench-Text evaluation measures average question-answering accuracy. Toy 3D path planning experiments report success rates over 30 runs and average attempts.

**Interpretation**: Higher Task Success Rate, lower Number of Environment Steps, and fewer Average Number of Re-plan Attempts indicate better performance. For RoCoBench-Text, higher Question-Answering Accuracy indicates better agent representation and reasoning.

**Baseline Results**: Reported baselines include an oracle 'Central Plan' LLM-planner and ablations. Examples from Table 2 (success rates ± std over 20 runs): Central Plan (oracle) success rates: Pack Grocery 0.82 ± 0.06, Arrange Cabinet 0.90 ± 0.07, Move Rope 1.00 ± 0.00, Sweep Floor 0.96 ± 0.04, Make Sandwich 0.70 ± 0.10, Sort Cubes 0.50 ± 0.11. Dialog (ours) success rates: Pack Grocery 0.44 ± 0.06, Arrange Cabinet 0.75 ± 0.10, Move Rope 0.95 ± 0.05, Sweep Floor 0.80 ± 0.08, Make Sandwich 0.93 ± 0.06, Sort Cubes 0.65 ± 0.11. RoCoBench-Text results (Table 4) report question-answering accuracy for models (example: GPT-4-0314: Capability 0.67 ± 0.06, Communication 0.84 ± 0.06, Adaptation 0.79 ± 0.06, etc.).

**Validation**: Simulation experiments use repeated runs per task (20 runs per task reported for main results). Toy 3D path planning uses 30 runs. Real-world experiments use 10 runs per setup. Ablations and comparisons to oracle planners are used to validate contributions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
