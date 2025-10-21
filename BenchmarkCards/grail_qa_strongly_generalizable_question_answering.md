# GRAIL QA (Strongly Generalizable Question Answering)

## 📊 Benchmark Details

**Name**: GRAIL QA (Strongly Generalizable Question Answering)

**Overview**: The paper introduces GRAIL QA, a large-scale, high-quality dataset with 64,331 questions that supports evaluation of i.i.d., compositional, and zero-shot generalization in knowledge base question answering (KBQA).

**Data Type**: question-logical form pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- WEBQ
- COMPLEX WEBQ
- SIMPLE Q
- QALD
- GRAPH Q

**Resources**:
- [Resource](http://dki-lab.github.io/GrailQA/)
- [GitHub Repository](https://github.com/dki-lab/GrailQA)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the development of KBQA models with stronger generalization through a comprehensive dataset that evaluates three levels of generalization.

**Target Audience**:
- ML Researchers
- Domain Experts
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Crowdsourced questions based on the FREEBASE knowledge base and logical forms generated from it.

**Size**: 64,331 questions

**Format**: JSON

**Annotation**: Crowdsourced via Amazon Mechanical Turk with various quality control mechanisms.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match (EM)
- F1 Score

**Calculation**: Exact match is determined by comparing predicted and gold logical forms based on graph isomorphism.

**Interpretation**: Higher F1 scores and EM indicate better generalization performance of KBQA models across different question types.

**Baseline Results**: RANKING model achieves competitive performance on GRAIL QA and sets new state-of-the-art on GRAPH Q.

**Validation**: The dataset is split into training/validation/test sets with specific questions designated for i.i.d., compositional, and zero-shot evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Analysis of crowd worker demographics for quality and diversity in question generation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution 4.0 International (CC-BY 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
