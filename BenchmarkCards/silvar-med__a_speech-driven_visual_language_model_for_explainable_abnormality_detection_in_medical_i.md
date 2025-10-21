# SilVar-Med: A Speech-Driven Visual Language Model for Explainable Abnormality Detection in Medical Imaging

## 📊 Benchmark Details

**Name**: SilVar-Med: A Speech-Driven Visual Language Model for Explainable Abnormality Detection in Medical Imaging

**Overview**: SilVar-Med is an end-to-end speech-driven medical visual language model that enables users to interact with the model verbally and focuses on the interpretation of the reasoning behind each prediction of medical abnormalities with a proposed reasoning dataset.

**Data Type**: multimodal

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MultiMedEval
- MultiMedQA
- OmniMedVQA

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To introduce a speech-driven medical VLM that enhances multimodal interactions and supports structured reasoning for abnormality detection.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Medical Imaging Specialists

**Tasks**:
- Medical Image Analysis
- Abnormality Detection
- Reasoning-based Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The dataset includes abnormalities extracted from the SLAKE dataset, with annotations performed by medical image analysis specialists and enhanced by GPT-4o.

**Size**: 866 samples

**Format**: N/A

**Annotation**: Manually annotated by medical image analysis specialists and enhanced with GPT-4o.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- LLM-based evaluation

**Metrics**:
- BERTScore
- BLEU Score
- ROUGE

**Calculation**: Metrics were calculated based on the generated responses of SilVar-Med and compared against ground truth references.

**Interpretation**: The effectiveness of the model is judged based on accuracy, quality of reasoning, and coherence of responses.

**Baseline Results**: Compared against SilVar and commercial speech-driven VLMs like GPT-4o Mini and Gemini Flash 1.5.

**Validation**: Verified by three medical imaging specialists and through the LLM-as-Judge framework.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
