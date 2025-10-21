# KoCoSa (Korean Context-aware Sarcasm Detection Dataset)

## 📊 Benchmark Details

**Name**: KoCoSa (Korean Context-aware Sarcasm Detection Dataset)

**Overview**: This paper introduces a new dataset for the Korean dialogue sarcasm detection task, KoCoSa, which consists of 12.8K daily Korean dialogues and the labels for this task on the last response.

**Data Type**: dialogue pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Korean

**Similar Benchmarks**:
- Kocasm

**Resources**:
- [GitHub Repository](https://github.com/Yu-billie/KoCoSa_sarcasm_detection)

## 🎯 Purpose and Intended Users

**Goal**: To provide a valuable resource for advancing research in Korean sarcasm detection.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Sarcasm Detection

**Limitations**: N/A

## 💾 Data

**Source**: NIKL Messenger Corpus and NIKL Online Text Message Corpus

**Size**: 12,824 dialogues

**Format**: N/A

**Annotation**: Expert annotators review the correctness of labels and remove abnormal dialogues.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Balanced Accuracy
- Macro F1
- Weighted F1
- Precision
- Recall

**Calculation**: Metrics calculated considering the imbalanced label distribution in the dataset.

**Interpretation**: Higher scores indicate better performance in identifying sarcasm.

**Baseline Results**: KLUE-RoBERTa fine-tuned on the dataset outperforms GPT-3.5 and performs nearly equivalent to GPT-4.

**Validation**: Dataset validated through human annotation and filtering processes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset was constructed carefully to ensure no personal data is retained.

**Data Licensing**: Not Applicable

**Consent Procedures**: Approval from the Institutional Review Board (IRB) was obtained for data collection.

**Compliance With Regulations**: Not Applicable
