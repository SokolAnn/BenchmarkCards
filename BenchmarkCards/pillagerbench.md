# PillagerBench

## 📊 Benchmark Details

**Name**: PillagerBench

**Overview**: PillagerBench is a novel framework for evaluating multi-agent systems in real-time competitive team-vs-team scenarios in Minecraft. It features multiple distinct competitive scenarios to assess the adaptability and strategic decision-making of LLM-based agents.

**Data Type**: multimodal

**Domains**:
- Artificial Intelligence

**Languages**:
- English

**Similar Benchmarks**:
- SMAC (StarCraft Multi-Agent Challenge)
- Lux AI Challenge

**Resources**:
- [GitHub Repository](https://github.com/aialt/PillagerBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous evaluation framework for competitive multi-agent systems, fostering advancements in multi-agent AI.

**Target Audience**:
- ML Researchers
- Game Developers
- AI Practitioners

**Tasks**:
- Multi-Agent Coordination
- Decision Making

**Limitations**: N/A

## 💾 Data

**Source**: Built-in competitive scenarios in Minecraft.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Points
- Sabotage
- Points difference
- Win rate

**Calculation**: Points are calculated based on the average scores in each game episode, sabotage scores reflect points denied to opponents, and win rates are determined by the outcomes of game episodes.

**Interpretation**: Higher points, lower points difference, and increased win rates indicate better performance of the agents.

**Baseline Results**: TactiCrafter outperformed random and Chain-of-Thought baselines in all evaluated metrics.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
