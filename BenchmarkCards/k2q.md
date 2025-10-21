# K2Q

## 📊 Benchmark Details

**Name**: K2Q

**Overview**: K2Q is a diverse collection of five datasets converted from Key Information Extraction (KIE) tasks to a prompt-response format using various bespoke templates, enhancing the performance and robustness of visually rich document understanding models.

**Data Type**: prompt-response pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/JPMorgan/K2Q)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large and diverse set of prompt-response questions that better capture the intricacies of KIE and the variety of questions that users can ask in real-world applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Key Information Extraction
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Transformed datasets from existing Key Information Extraction (KIE) datasets, including Ad-Buy, CORD, Docile, Kleister Charity, and Registration Form.

**Size**: 300,000 questions over 12,000 documents

**Format**: N/A

**Annotation**: Templates were manually created by researchers familiar with the datasets.

## 🔬 Methodology

**Methods**:
- Zero-shot prompting
- Fine-tuning

**Metrics**:
- Average Normalized Levenshtein Similarity (ANLS)

**Calculation**: ANLS measures the edit distance to account for how similar the generated and true answers are, normalized against string length.

**Interpretation**: Higher ANLS scores indicate better performance in generating accurate responses.

**Baseline Results**: Models trained on K2Q demonstrate improved performance over those trained on simpler template datasets.

**Validation**: K2Q has undergone human validation to ensure quality and correctness of generated questions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
