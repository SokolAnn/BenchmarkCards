# GRASP (Grid-Based Benchmark for Evaluating Commonsense Spatial Reasoning)

## 📊 Benchmark Details

**Name**: GRASP (Grid-Based Benchmark for Evaluating Commonsense Spatial Reasoning)

**Overview**: GRASP is a large-scale benchmark consisting of 16,000 grid-based environments designed to evaluate the commonsense spatial reasoning abilities of LLMs through energy collection tasks.

**Data Type**: grid instances

**Domains**:
- Artificial Intelligence

**Languages**:
- English

**Similar Benchmarks**:
- SpartQA
- StepGame
- BabyAI

**Resources**:
- [GitHub Repository](https://github.com/jasontangzs0/GRASP)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark the commonsense spatial reasoning abilities of LLMs within structured grid environments.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Spatial Reasoning

**Limitations**: The synthetic nature of GRASP’s grid environments may not fully capture the complexity of real-world CSR tasks.

## 💾 Data

**Source**: Generated grid environments based on defined parameters for energy distribution, obstacles, and agent constraints.

**Size**: 16,000 environments

**Format**: text

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Baseline comparison with random walk and greedy search methods
- Evaluation of LLM-based agents

**Metrics**:
- Energy collected
- Step length

**Calculation**: Performance is calculated based on the amount of energy collected and the number of steps taken by the agents.

**Interpretation**: Higher energy collected and fewer steps taken indicate better performance.

**Baseline Results**: GPT-3.5-Turbo underperformed against both random walk and greedy search baselines.

**Validation**: Results validated through statistical tests comparing agent performances.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Robustness**: Hallucination, Evasion attack
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
