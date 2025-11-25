# VitaBench (Versatile Interactive Tasks Benchmark)

## 📊 Benchmark Details

**Name**: VitaBench (Versatile Interactive Tasks Benchmark)

**Overview**: VitaBench is a challenging benchmark that evaluates agents on versatile interactive tasks grounded in real-world settings, constructed from daily applications in food delivery, in-store consumption, and online travel services. It includes complex life-serving simulation environments with 66 tools and over 400 tasks.

**Data Type**: task-performance assessments with temporal reasoning requirements

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Resources**:
- [Resource](https://vitabench.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To measure LLM-based agents' ability to handle inherent complexity of real-world applications through versatile interactive tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Task Performance Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Derived from real user requests and daily applications across multiple domains, including direct simulations of user interactions.

**Size**: 400 tasks

**Format**: N/A

**Annotation**: Derived from authentic platform data, manually designed and iteratively refined with human verification.

## 🔬 Methodology

**Methods**:
- Evaluative metrics
- Task simulation

**Metrics**:
- Success Rate
- Task Completion Rate

**Calculation**: Success rates calculated based on the completion of tasks under specified conditions.

**Interpretation**: Higher success rates indicate better agent performance in navigating complex task environments.

**Baseline Results**: Top-performing models achieve a maximum of 30% success on cross-scenario tasks.

**Validation**: Evaluated through extensive testing of agent interactions and failure pattern analysis.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**
- **Robustness**: Evasion attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: To protect user data, all personal identifiers are anonymized before being used in the benchmark.

**Data Licensing**: Data will be openly shared to ensure reproducibility in accordance with applicable research guidelines.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
