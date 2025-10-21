# Collab-Overcooked

## 📊 Benchmark Details

**Name**: Collab-Overcooked

**Overview**: Collab-Overcooked is a benchmark for evaluating LLM-based Multi-Agent Systems (LLM-MAS) in a collaborative cooking environment, focusing on the collaboration capabilities of agents through a series of interactive tasks.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Artificial Intelligence

**Languages**:
- English

**Similar Benchmarks**:
- RocoBench
- VillagerBench
- LLMARENA

**Resources**:
- [GitHub Repository](https://github.com/YusaeMeow/Collab-Overcooked)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLM-based Multi-Agent Systems in terms of collaboration effectiveness and task completion within an interactive cooking scenario.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Game Developers

**Tasks**:
- Collaborative Cooking
- Task Planning
- Dynamic Adaptation

**Limitations**: The benchmark is designed specifically for sequential process-specific tasks, which may not generalize to all possible LLM application scenarios.

## 💾 Data

**Source**: Developed from the Overcooked-AI game environment, featuring a simulation setup for interactive collaboration.

**Size**: 30 tasks

**Format**: JSON

**Annotation**: Manually annotated Referential Action Trajectories (RATs) for evaluation purposes.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Trajectory Efficiency Score (TES)
- Incremental Trajectory Efficiency Score (ITES)
- Progress Completeness (PC)

**Calculation**: Metrics are calculated based on the historical action sequence of agents and defined RATs for collaboration tasks.

**Interpretation**: Higher scores indicate better collaboration capabilities and task completion efficiency.

**Baseline Results**: Comparative performance of 13 LLMs, including closed-source and open-source models, highlights varying levels of collaboration efficiency.

**Validation**: Extensive experiments conducted with different models across varying task complexities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: All human experiments conducted with informed consent.

**Compliance With Regulations**: Not Applicable
