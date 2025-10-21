# VideoEspresso

## 📊 Benchmark Details

**Name**: VideoEspresso

**Overview**: VideoEspresso is a large-scale VideoQA dataset designed to facilitate high-level reasoning over macroscopic video semantics, featuring VideoQA pairs preserving essential spatial details and multimodal annotations of intermediate reasoning steps.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- How2QA
- ActivityNet-QA
- NExT-QA
- MovieChat
- TVQA
- MSRVTT-QA
- VideoCoT

**Resources**:
- [GitHub Repository](https://github.com/hshjerry/VideoEspresso)

## 🎯 Purpose and Intended Users

**Goal**: To enhance video reasoning by addressing the limitations of existing datasets in terms of scale and granularity.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Video Question Answering
- Video Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Collected from various datasets including raw unannotated Internet videos.

**Size**: 203,546 question-answer pairs

**Format**: N/A

**Annotation**: Automated annotations with Chain-of-Thought evidence.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Evaluation against existing LVLMs

**Metrics**:
- Accuracy

**Calculation**: Performance evaluated based on semantic similarity and logical coherence of answers.

**Interpretation**: The model's performance is assessed by its ability to generate coherent and contextually relevant answers based on video content.

**Validation**: Comparison against 9 popular LVLMs across 14 tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
