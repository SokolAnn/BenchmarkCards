# BENTO (Benchmark Task Reduction)

## 📊 Benchmark Details

**Name**: BENTO (Benchmark Task Reduction)

**Overview**: BENTO proposes a method for efficiently reducing the number of tasks in large language model benchmarks without compromising evaluation quality, utilizing in-context learning to estimate task transferability.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU

**Resources**:
- [GitHub Repository](https://github.com/tianyi-lab/bento)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate large language models efficiently by reducing the number of tasks in benchmarks while maintaining evaluation accuracy.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: A smaller benchmark may be less diverse and potentially more vulnerable to adversarial attacks.

## 💾 Data

**Source**: MMLU and FLAN benchmarks, consisting of multiple choice questions across diverse topics.

**Size**: 57 tasks (MMLU)

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Task transferability estimation
- Facility location optimization

**Metrics**:
- Accuracy
- Normalized Root Mean Square Error (NRMSE)

**Calculation**: Transferability is estimated using in-context learning; performance on the reduced set is correlated with full benchmark performance.

**Interpretation**: Lower NRMSE indicates better performance of the reduced benchmark compared to the full benchmark.

**Baseline Results**: Reduction achieved from 57 to 3 tasks while maintaining 96% performance accuracy on MMLU.

**Validation**: Performance is evaluated by comparing results on reduced benchmarks against full benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
