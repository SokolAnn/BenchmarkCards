# LANID (LLM-Assisted New Intent Discovery)

## 📊 Benchmark Details

**Name**: LANID (LLM-Assisted New Intent Discovery)

**Overview**: LANID is a framework designed to tackle the challenge of novel intent discovery in Task-Oriented Dialogue Systems by leveraging Large Language Models to enhance lightweight encoders through contrastive learning.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/floatSDSDS/LANID)

## 🎯 Purpose and Intended Users

**Goal**: To enable systems to autonomously identify novel intents while maintaining robust performance on known ones.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- New Intent Discovery

**Limitations**: N/A

## 💾 Data

**Source**: The BANKING dataset, StackOverflow dataset, and M-CID dataset were used for evaluation.

**Size**: 13,083 utterances for BANKING dataset, 20,000 queries for StackOverflow dataset, 1,745 utterances for M-CID dataset

**Format**: N/A

**Annotation**: The datasets are used with and without labels in both unsupervised and semi-supervised settings.

## 🔬 Methodology

**Methods**:
- Clustering
- Contrastive Learning

**Metrics**:
- Normalized Mutual Information (NMI)
- Adjusted Rand Index (ARI)
- Accuracy (ACC)

**Calculation**: Metrics are calculated based on clustering results comparing predicted clusters with true intent labels.

**Interpretation**: Higher NMI, ARI, and ACC values indicate better clustering performance and model efficacy.

**Baseline Results**: LANID surpassed strong baselines in both unsupervised and semi-supervised settings.

**Validation**: Evaluation was conducted with three benchmark datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
