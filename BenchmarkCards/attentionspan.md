# AttentionSpan

## 📊 Benchmark Details

**Name**: AttentionSpan

**Overview**: AttentionSpan is an algorithmic benchmark comprising five tasks of infinite input domains aimed at assessing the reliability and robustness of transformer models in algorithmic reasoning, specifically their ability to extrapolate to unseen types of inputs and to analyze attention mechanisms.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CRLS-Text
- BIG-Bench

**Resources**:
- [GitHub Repository](https://github.com/michalspiegel/AttentionSpan)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the reasoning robustness of transformers and trace the attention mechanisms in algorithmic tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Algorithmic Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic generation of tasks including string reversal, long addition, long multiplication, flip-flop language modeling, and value assignment.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Evaluation of attention patterns
- Intervention experiments

**Metrics**:
- Accuracy
- Partial Accuracy

**Calculation**: Exact-match accuracy of output sequences and calculation of partial accuracy based on correct token predictions.

**Interpretation**: An evaluation of model accuracy on in-distribution and out-of-distribution tasks reveals the reliability of attention mechanisms.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
