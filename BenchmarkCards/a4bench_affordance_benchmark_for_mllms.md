# A4Bench (Affordance Benchmark for MLLMs)

## 📊 Benchmark Details

**Name**: A4Bench (Affordance Benchmark for MLLMs)

**Overview**: A4Bench is a novel benchmark designed to evaluate the affordance perception abilities of Multimodal Large Language Models (MLLMs) across two dimensions: Constitutive Affordance and Transformative Affordance.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/JunyingWang959/A4Bench)

## 🎯 Purpose and Intended Users

**Goal**: To systematically assess the affordance perception capabilities of MLLMs across two critical dimensions: constitutive affordance and transformative affordance.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: A4Bench consists of 2,000 multimodal question-answer pairs, covering both Constitutive Affordance (1,282 pairs) and Transformative Affordance (718 pairs).

**Size**: 2,000 question-answer pairs

**Format**: N/A

**Annotation**: Questions were developed by a team of 60 human annotators categorized by expertise, followed by rigorous review for accuracy and clarity.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Exact Match Accuracy
- Precision
- Recall
- F1 Score
- Partial Credit
- AUC-ROC
- Hamming Loss

**Calculation**: Metrics are calculated based on the degree of match between MLLM responses and correct answers.

**Interpretation**: A higher exact match accuracy indicates better performance in understanding affordance perception.

**Baseline Results**: Human performance reaches 85.34% exact match accuracy, while the best MLLM achieved 18.05%.

**Validation**: Models were tested in a zero-shot setting using a randomized question format to ensure fair evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
