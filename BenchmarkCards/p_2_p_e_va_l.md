# P 2 P E VA L

## 📊 Benchmark Details

**Name**: P 2 P E VA L

**Overview**: P 2 P E VA L is a comprehensive benchmark featuring 121 paper-poster pairs and a dual evaluation methodology (Universal and Fine-Grained) that leverages LLM-as-a-Judge and detailed, human-annotated checklists for evaluating academic posters generated from research papers.

**Data Type**: paper-poster pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Postdoc
- Docbank
- ScipostLayout

**Resources**:
- [GitHub Repository](https://github.com/multimodal-art-projection/P2P)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust evaluation framework for academic poster generation systems and to facilitate the assessment of their quality through a comprehensive benchmark.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Poster Generation
- Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: 121 paper-poster pairs collected from the ACL conference series (2022-2024) and SciPostLayout.

**Size**: 121 pairs

**Format**: PDF, PNG

**Annotation**: Four annotators independently review each poster; checklists based on official posters are used for evaluation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- LLM-as-a-Judge

**Metrics**:
- Universal Poster Evaluation
- Fine-Grained Poster Evaluation

**Calculation**: Scores are based on human annotations and automated evaluations.

**Interpretation**: High scores indicate better preservation of content fidelity, visual consistency, and overall poster quality.

**Validation**: Utilized XGBoost for modeling the relationship between evaluation criteria and human annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
