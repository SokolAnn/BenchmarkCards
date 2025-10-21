# ReForm-Eval

## 📊 Benchmark Details

**Name**: ReForm-Eval

**Overview**: ReForm-Eval is a new multi-modal benchmark that evaluates large vision language models (LVLMs) via unified re-formulation of task-oriented benchmarks into formats compatible with LVLMs. It encompasses 61 benchmark datasets, covering various dimensions of evaluation for LVLMs.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MMBench
- MME

**Resources**:
- [GitHub Repository](https://github.com/FudanDISC/ReForm-Eval)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for large vision-language models (LVLMs) by re-formulating existing benchmarks into unified formats that address LVLM capabilities.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Visual Question Answering
- Image Classification
- Image Captioning
- Object Detection
- Optical Character Recognition
- Multi-Turn Dialogue

**Limitations**: N/A

## 💾 Data

**Source**: Systematic collection and re-formulation of existing task-oriented multi-modal benchmarks into unified formats suitable for LVLM assessment.

**Size**: 500,000 evaluation instances across over 300,000 images

**Format**: N/A

**Annotation**: Utilizes existing annotations from previously established benchmarks.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Likelihood evaluation
- Black-box evaluation
- White-box evaluation

**Metrics**:
- Accuracy
- F1 Score
- CIDEr (for image captioning)
- Word-level accuracy (for OCR tasks)

**Calculation**: Metrics calculated based on the extent to which LVLM outputs match the provided benchmarks' requirements and structures.

**Interpretation**: The model's performance is interpreted based on accuracy rates in the context of multi-choice and open-ended response requirements. High accuracy signifies successful comprehension and reasoning abilities of the LVLMs.

**Baseline Results**: N/A

**Validation**: Validation procedures involved multiple rounds of testing under varied conditions to ensure reliability of results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack
- **Societal Impact**: Impact on education: bypassing learning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
