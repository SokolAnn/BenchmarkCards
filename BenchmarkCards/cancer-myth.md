# Cancer-Myth

## 📊 Benchmark Details

**Name**: Cancer-Myth

**Overview**: Cancer-Myth is an expert-verified adversarial dataset of 585 cancer-related questions with false presuppositions, designed to evaluate LLM and medical agent performance in handling patient questions.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MedQA
- HealthSearchQA

**Resources**:
- [Resource](https://cancermyth.github.io)
- [GitHub Repository](https://github.com/Bill1235813/cancer-myth)
- [Resource](https://huggingface.co/datasets/Cancer-Myth/Cancer-Myth)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate LLM performance in responding to cancer-related patient questions containing false presuppositions.

**Target Audience**:
- ML Researchers
- Model Developers
- Healthcare Professionals

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Adversarial dataset generated from real patient inquiries and myths related to cancer treatment.

**Size**: 585 examples

**Format**: JSONL

**Annotation**: Manually reviewed and verified by hematology oncology physicians.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Presupposition Correction Score (PCS)
- Presupposition Correction Rate (PCR)

**Calculation**: Scores are calculated based on the model's ability to recognize and address false presuppositions in patient questions.

**Interpretation**: Higher scores indicate better performance by successfully identifying and correcting misconceptions.

**Baseline Results**: No model corrected false presuppositions more than 30% of the time.

**Validation**: Reviewed by hematology oncology physicians for relevance and reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Misleading information could lead to incorrect health decisions for patients.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data is fully synthetic and does not include real patient information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
