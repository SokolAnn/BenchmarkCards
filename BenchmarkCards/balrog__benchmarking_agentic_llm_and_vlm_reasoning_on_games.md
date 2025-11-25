# BALROG: Benchmarking Agentic LLM and VLM Reasoning On Games

## 📊 Benchmark Details

**Name**: BALROG: Benchmarking Agentic LLM and VLM Reasoning On Games

**Overview**: BALROG is a novel benchmark designed to assess the agentic capabilities of LLMs and VLMs through a diverse set of challenging games, incorporating various existing reinforcement learning environments.

**Data Type**: Reinforcement Learning environments

**Domains**:
- Artificial Intelligence

**Languages**:
- English

**Similar Benchmarks**:
- SuperGLUE
- MMLU
- BIG-Bench

**Resources**:
- [Resource](https://balrogai.com)

## 🎯 Purpose and Intended Users

**Goal**: To assess the agentic capabilities of long-context LLMs and VLMs across a diverse set of complex, long-horizon tasks in gaming environments.

**Target Audience**:
- AI Researchers
- Model Developers
- Game Developers
- Practitioners in Reinforcement Learning

**Tasks**:
- Long-term Planning
- Spatial Reasoning
- Resource Management
- Navigation
- Exploration

**Limitations**: N/A

## 💾 Data

**Source**: A suite of six reinforcement learning environments including BabyAI, Crafter, TextWorld, Baba Is AI, MiniHack, and NetHack.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Fine-grained performance metrics
- Qualitative analysis

**Metrics**:
- Average Progress

**Calculation**: Scores are calculated based on task completion and fine-grained metrics for model evaluation in RL environments.

**Interpretation**: Higher scores indicate better agent performance, with progress calculated against the game's difficulty levels.

**Baseline Results**: N/A

**Validation**: Performance is validated using statistical significance with multiple evaluation seeds.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Revealing confidential information', 'Operating in unsafe environments']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Open-source under a permissive license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
