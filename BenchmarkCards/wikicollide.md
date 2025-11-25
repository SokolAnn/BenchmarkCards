# WIKICOLLIDE

## 📊 Benchmark Details

**Name**: WIKICOLLIDE

**Overview**: WIKICOLLIDE is the first benchmark capturing real Wikipedia inconsistencies, specifically designed for Corpus-Level Inconsistency Detection.

**Data Type**: atomic facts

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- FEVER
- FEVEROUS
- AmbigQA

**Resources**:
- [GitHub Repository](https://github.com/stanford-oval/inconsistency-detection.2024)

## 🎯 Purpose and Intended Users

**Goal**: To systematically quantify corpus-level inconsistencies in Wikipedia and enhance the accuracy of knowledge in large language models.

**Target Audience**:
- ML Researchers
- Wikipedia Editors
- NLP Practitioners

**Tasks**:
- Corpus-Level Inconsistency Detection
- Fact Verification

**Limitations**: N/A

## 💾 Data

**Source**: English Wikipedia

**Size**: 955 atomic facts

**Format**: N/A

**Annotation**: Manual verification through CLAIRE-assisted analysis.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- AUROC

**Calculation**: Calculated based on performance of CLAIRE and various automated systems against human-annotated labels.

**Interpretation**: Higher AUROC indicates better performance of inconsistency detection systems.

**Baseline Results**: CLAIRE achieves an AUROC of 75.1% on the test set.

**Validation**: The reliability of the benchmark was ensured through manual verification of inconsistencies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
