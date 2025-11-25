# COMPARISON QA

## 📊 Benchmark Details

**Name**: COMPARISON QA

**Overview**: COMPARISON QA benchmark contains 283K abstract questions, each instantiated by a pair of high-frequency and low-frequency entities, enabling controllable comparison to study the role of knowledge frequency in LLM performance.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SimpleQA

**Resources**:
- [GitHub Repository](https://github.com/HKUST-KnowComp/ComparisonQA)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs' factual knowledge and measure their robustness regarding high-frequency and low-frequency knowledge.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated through an automatic pipeline based on raw knowledge bases, specifically DBpedia.

**Size**: 283,455 abstract questions

**Format**: N/A

**Annotation**: Validated through expert verification with majority voting.

## 🔬 Methodology

**Methods**:
- Multiple-choice evaluation
- Two-round method utilizing correctness and uncertainty

**Metrics**:
- Accuracy
- Macro F1-score
- Uncertainty

**Calculation**: Metrics are calculated based on model predictions against ground truth labels.

**Interpretation**: Higher accuracy and lower uncertainty indicate better factual knowledge understanding.

**Baseline Results**: N/A

**Validation**: Expert verification of question quality showed 95.5% correctness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The dataset will be released under a CC license, the DBpedia dataset used is shared under the CC BY-SA license.

**Consent Procedures**: Expert verifications obtained IRB approval and were voluntary.

**Compliance With Regulations**: Not Applicable
