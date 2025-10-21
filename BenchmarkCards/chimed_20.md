# ChiMed 2.0

## 📊 Benchmark Details

**Name**: ChiMed 2.0

**Overview**: ChiMed 2.0 is a large-scale Chinese medical dataset that integrates both traditional Chinese medicine classics and modern general medical texts, facilitating pre-training, supervised fine-tuning, and reinforcement learning from human feedback (RLHF) for medical language models.

**Data Type**: text

**Domains**:
- Healthcare

**Languages**:
- Chinese

**Similar Benchmarks**:
- CMMLU
- CEval

**Resources**:
- [GitHub Repository](https://github.com/synlp/ChiMed-2.0)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for training and evaluating Chinese medical language models.

**Target Audience**:
- ML Researchers
- Medical Professionals

**Tasks**:
- Question Answering
- Medical Report Generation
- Clinical Decision Support

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from online medical platforms, including traditional Chinese medicine classics and modern medical documents.

**Size**: 204.4M characters

**Format**: N/A

**Annotation**: Automated processing using language models, including sensitive content cleaning and QA pair generation.

## 🔬 Methodology

**Methods**:
- Pre-training
- Supervised Fine-Tuning
- Reinforcement Learning from Human Feedback

**Metrics**:
- Accuracy

**Calculation**: Metrics calculated based on model performance on medical benchmark datasets.

**Interpretation**: Improvement in performance across different model scales indicates effectiveness.

**Baseline Results**: Qwen-3 models achieved significant performance gains on medical benchmarks.

**Validation**: Validated through experiments on CMMLU and CEval datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Sensitive content cleaning procedures are implemented to protect user privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
