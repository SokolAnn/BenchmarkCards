# Multi-Target Counter Narrative Dataset to Fight Online Hate Speech

## 📊 Benchmark Details

**Name**: Multi-Target Counter Narrative Dataset to Fight Online Hate Speech

**Overview**: This paper presents a novel human-in-the-loop data collection methodology for generating a multi-target expert-based dataset of hate speech and counter narratives (HS/CN). The resulting dataset contains 5000 pairs addressing various hate targets, including race, religion, sexual orientation, and more, and aims to facilitate the generation of non-aggressive responses to hate speech.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CONAN (COunter NArratives through nichesourcing)

**Resources**:
- [GitHub Repository](https://github.com/marcoguerini/CONAN)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality, diverse, and scalable dataset for generating counter narratives against online hate speech.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Counter Narrative Generation

**Limitations**: N/A

## 💾 Data

**Source**: Generated through a human-in-the-loop methodology involving expert review and post-editing of hate speech and counter narrative pairs.

**Size**: 5000 pairs

**Format**: N/A

**Annotation**: Expert annotation via human review for validation and quality assurance.

## 🔬 Methodology

**Methods**:
- Human-in-the-loop data collection
- Iterative refinement with expert review

**Metrics**:
- Imbalance Degree
- Acceptance Rate
- HTER
- Novelty
- Repetition Rate

**Calculation**: Metrics are calculated based on the performance of the data collection methodology across multiple iterations.

**Interpretation**: Higher acceptance rates indicate better data quality; lower HTER values suggest reduced editing effort by reviewers.

**Baseline Results**: N/A

**Validation**: Validation through expert review during each iteration of data collection.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: Data includes multiple hate targets such as race, religion, sexual orientation, and gender.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
