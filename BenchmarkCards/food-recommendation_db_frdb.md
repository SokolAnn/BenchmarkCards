# Food-Recommendation DB (FRDB)

## 📊 Benchmark Details

**Name**: Food-Recommendation DB (FRDB)

**Overview**: The Food-Recommendation DB (FRDB) dataset focuses on food recommendations for women around pregnancy and infants, providing domain-specific knowledge to evaluate retrieval-augmented language models.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to evaluate the performance of retrieval-augmented LLMs, specifically the GPT-3.5-turbo, on domain-specific questions regarding food recommendations.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners

**Tasks**:
- Question Answering

**Limitations**: The compression rate and performance may vary based on sentence complexity and initial length.

## 💾 Data

**Source**: Constructed dataset focusing on food recommendations verified by health professionals.

**Size**: 1000 QA pairs and 7588 knowledge entries

**Format**: N/A

**Annotation**: Validated by health-domain professionals, ambiguous content removed.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on the percentage of correctly recommended food items from QA pairs.

**Interpretation**: An accuracy around 90% indicates high performance of retrieval-augmented models on this benchmark.

**Validation**: Performance validated through comparisons with original retrieval-augmented language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Dataset specifically addresses the dietary needs of pregnant women and infants.

**Potential Harm**: Potential misguidance related to food recommendations which can affect health.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
