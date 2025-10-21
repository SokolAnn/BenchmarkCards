# NextQuAD

## 📊 Benchmark Details

**Name**: NextQuAD

**Overview**: NextQuAD is a comprehensive open-domain dataset for Persian designed to enhance the performance of question answering systems, containing 7,515 contexts and 23,918 pairs of question and answer.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Persian

**Similar Benchmarks**:
- ParSQuAD
- PersianQA

**Resources**:
- [GitHub Repository](https://github.com/mosiomohsen/NextQuAD)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality question answering dataset in Persian to improve the design and functionality of QA systems for non-English languages.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Data was gathered through translation of SQuAD 2.0, question-answer pairs from a game application called 'Quiz of Kings', and manual data collection from well-known Persian websites.

**Size**: 7,515 contexts and 23,918 pairs of question and answer

**Format**: N/A

**Annotation**: The dataset was manually reviewed and cross-validated, involving crowdworkers who contributed to the creation and annotation of the question-answer pairs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match (EM)
- F1 Score

**Calculation**: EM is calculated based on the exact match of responses with the ground truth answers; F1 Score is computed similarly considering both precision and recall.

**Interpretation**: A higher Exact Match and F1 Score indicate better performance of the QA system. Values close to 1.0 signify high accuracy in answering.

**Baseline Results**: The model achieved 0.95 Exact Match and 0.97 F1 Score on the evaluation dataset.

**Validation**: K-fold cross-validation with five folds was employed.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
