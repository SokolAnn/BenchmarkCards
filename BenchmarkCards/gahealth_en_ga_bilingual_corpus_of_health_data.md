# gaHealth (EN ↔GA Bilingual Corpus of Health Data)

## 📊 Benchmark Details

**Name**: gaHealth (EN ↔GA Bilingual Corpus of Health Data)

**Overview**: The gaHealth corpus is the first bilingual corpus of health data for the Irish language developed to enhance machine translation performance for low-resource languages. It demonstrates the significant benefits of using in-domain datasets.

**Data Type**: parallel text files

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- English
- Irish

**Similar Benchmarks**:
- LoResMT2021

**Resources**:
- [GitHub Repository](https://github.com/seamusl/gaHealth)
- [Resource](https://aclanthology.org/2022.lrec-1.727)

## 🎯 Purpose and Intended Users

**Goal**: To improve machine translation for low-resource languages through the development of a specialized bilingual corpus in the health domain.

**Target Audience**:
- NLP Researchers
- Machine Translation Developers
- Healthcare Professionals

**Tasks**:
- Machine Translation

**Limitations**: N/A

## 💾 Data

**Source**: Developed from publicly available documents like strategy statements and annual reports from the Irish Department of Health.

**Size**: 16,201 lines

**Format**: parallel text files

**Annotation**: Manual alignment of sentences

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU
- TER
- ChrF

**Calculation**: Metrics are calculated based on model training and evaluation using selected automated evaluation techniques.

**Interpretation**: Higher BLEU, lower TER, and higher ChrF scores indicate better translation quality.

**Baseline Results**: Compared to models from LoResMT2021 Shared Task.

**Validation**: Early stopping criteria with no improvement in validation accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Decision bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Misinterpretation of health information']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
