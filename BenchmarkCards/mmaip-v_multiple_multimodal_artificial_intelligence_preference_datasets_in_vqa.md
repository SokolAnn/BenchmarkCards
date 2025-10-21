# MMAIP-V (Multiple Multimodal Artificial Intelligence Preference Datasets in VQA)

## 📊 Benchmark Details

**Name**: MMAIP-V (Multiple Multimodal Artificial Intelligence Preference Datasets in VQA)

**Overview**: High-quality video-text preference data crucial for Multimodal Large Language Models (MLLMs) alignment, addressing existing data scarcity with 24,000 entries constructed by sampling from response distributions and using an external scoring function for evaluation.

**Data Type**: video-text pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate preference learning and improve alignment capabilities of Multimodal Large Language Models through high-quality video-text preference data.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Video Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from video question-answering pairs sampled from WebVid, VIDAL, and ActivityNet datasets, combined with responses generated from different MLLM architectures.

**Size**: 24,000 pairs

**Format**: N/A

**Annotation**: Automatically scored responses by external visual reward models and GPT-4o for relevance and quality.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Evaluation based on the alignment of model responses to ground truth while incorporating visual information for comprehensive assessments.

**Interpretation**: Scores indicate alignment accuracy of MLLMs in generating video-based answers.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
