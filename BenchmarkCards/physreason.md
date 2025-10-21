# PhysReason

## 📊 Benchmark Details

**Name**: PhysReason

**Overview**: PhysReason is a comprehensive benchmark comprising 1,200 physics problems designed to evaluate models' physics-based reasoning capabilities, incorporating both knowledge-based and reasoning-based problems with multi-step solution requirements.

**Data Type**: problem-solving tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ScienceQA
- SciBench
- GPQA

**Resources**:
- [Resource](https://dxzxy12138.github.io/PhysReason/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate large language models' capabilities in physics-based reasoning and identify key bottlenecks in model performance.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Physics Problem Solving

**Limitations**: Though comprehensive, the benchmark focuses on idealized conditions rather than fully reflecting real-world scenarios, and the evaluation framework may increase computational time.

## 💾 Data

**Source**: Collection from public physics problems including International Physics Olympiad, Chinese National College Entrance Examination, and various mock examinations.

**Size**: 1,200 problems

**Format**: JSON

**Annotation**: Problems are annotated with detailed solution steps, diagrams, and educational context.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on answer-level and step-level evaluations.

**Interpretation**: Higher scores indicate better reasoning capabilities and problem-solving skills.

**Validation**: The framework is validated through experimental comparison against existing models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personally identifiable information is included.

**Data Licensing**: MIT License for the benchmark and CC BY-NC-SA for educational materials.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
