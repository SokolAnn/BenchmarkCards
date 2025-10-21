# I NDIC LINK

## 📊 Benchmark Details

**Name**: I NDIC LINK

**Overview**: I NDIC LINK is a new evaluation dataset for the task of Multilingual Fact Linking, containing linked WikiData facts and sentences in English and six Indian languages.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Hindi
- Telugu
- Tamil
- Urdu
- Gujarati
- Assamese

**Resources**:
- [GitHub Repository](https://github.com/SaiKeshav/mfl)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research in the task of Multilingual Fact Linking and to provide a dataset to evaluate models linking natural language sentences with knowledge graph facts.

**Target Audience**:
- NLP Researchers
- Machine Learning Practitioners

**Tasks**:
- Fact Linking

**Limitations**: N/A

## 💾 Data

**Source**: Linked WikiData facts and sentences from the relation extraction dataset WebRED, translated into multiple Indian languages.

**Size**: 6,429 sentences

**Format**: N/A

**Annotation**: Manual translation by professional translators and automatic translation for training.

## 🔬 Methodology

**Methods**:
- Retrieval+Generation architecture
- Dual Encoder
- Seq2Seq based generation

**Metrics**:
- Precision@1 (P@1)
- Recall@5 (R@5)

**Calculation**: Metrics are calculated by comparing predicted facts with gold set of facts.

**Interpretation**: Higher Precision@1 indicates that the most confident predicted fact matches a gold fact.

**Baseline Results**: R EFCOG outperforms re-ranking models with a 10.7 points improvement in Precision@1.

**Validation**: 5% of training examples used as a validation set for early stopping.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
