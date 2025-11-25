# Synthetic Dataset Generation for Self-Disclosure Detection

## 📊 Benchmark Details

**Name**: Synthetic Dataset Generation for Self-Disclosure Detection

**Overview**: This paper develops a synthetic, PII-labeled multi-text span dataset generated from large language models to foster reproducible research into personally identifiable information (PII) detection in vulnerable populations.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://netsys.surrey.ac.uk/datasets/synthetic-self-disclosure/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a privacy-preserving synthetic dataset for training models to detect self-disclosure of personally identifiable information (PII).

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Classification
- Named Entity Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic data generated from real posts on Reddit, focusing on vulnerable populations.

**Size**: 3,264 posts

**Format**: N/A

**Annotation**: Annotated for PII-revealing spans by domain experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics are calculated based on model performance comparisons on synthetic vs. original datasets.

**Interpretation**: A higher F1 Score and accuracy indicates better performance and usefulness of synthetic data.

**Baseline Results**: Performance metrics of the multilabel classifier on synthetic datasets are comparable to those on the original dataset.

**Validation**: Validated through user studies measuring indistinguishability and replicability of results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data, Personal information in prompt

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset is synthetic and designed not to be linkable to original users' data.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
