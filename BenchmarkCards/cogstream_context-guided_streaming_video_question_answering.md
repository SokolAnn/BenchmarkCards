# CogStream (Context-guided Streaming Video Question Answering)

## 📊 Benchmark Details

**Name**: CogStream (Context-guided Streaming Video Question Answering)

**Overview**: CogStream introduces a challenging task for streaming video reasoning, requiring models to identify the most relevant historical contextual information to answer questions about current video streams, supported by a densely annotated dataset of question-answer pairs.

**Data Type**: question-answer pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/LiamZhao326/CogStream)

## 🎯 Purpose and Intended Users

**Goal**: To empower and validate streaming video reasoning capabilities through the question-answering (QA) paradigm.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Streaming Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Videos collected from public sources such as MovieChat, MECD, QVhighlights, VideoMME, COIN, and YouCook2.

**Size**: 1,088 videos with a total of 59,032 question-answer pairs

**Format**: JSON

**Annotation**: Semi-automated with a manual review process.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Information Accuracy (IA)
- Detail Completeness (DC)
- Context Awareness (CA)
- Temporal Precision (TP)
- Logical Consistency (LC)

**Calculation**: Metrics are calculated based on the evaluation of generated answers against ground-truth answers using a powerful LLM.

**Interpretation**: Higher scores denote better performance in terms of accuracy, completeness, context awareness, timing consistency, and logical coherence.

**Baseline Results**: Results from various state-of-the-art Vid-LLMs on the CogStream dataset.

**Validation**: Validation through extensive experimental comparisons with existing models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
