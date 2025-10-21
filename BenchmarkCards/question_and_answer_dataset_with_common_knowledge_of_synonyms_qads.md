# Question and Answer Dataset with common knowledge of Synonyms (QADS)

## 📊 Benchmark Details

**Name**: Question and Answer Dataset with common knowledge of Synonyms (QADS)

**Overview**: QADS is designed to evaluate machine comprehension models' ability to handle commonsense knowledge of synonyms, generated from SQuAD 2.0 and adversarial challenges.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SQuAD 2.0

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the ability of NLP models to handle commonsense knowledge of synonyms as part of machine comprehension.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated from SQuAD 2.0 dataset using WordNet and enhanced Lesk algorithm.

**Size**: 5,000+ questions

**Format**: N/A

**Annotation**: Crowdsourced verification from native English speakers.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Crowdsourced verification

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on correct answers against total questions.

**Interpretation**: Higher accuracy indicates better performance of models in understanding commonsense synonyms.

**Validation**: Evaluated by fine-tuning models on SQuAD 2.0 and cross-validation on QADS.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
