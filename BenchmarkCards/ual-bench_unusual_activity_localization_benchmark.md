# UAL-Bench (Unusual Activity Localization Benchmark)

## 📊 Benchmark Details

**Name**: UAL-Bench (Unusual Activity Localization Benchmark)

**Overview**: UAL-Bench is a comprehensive benchmark for unusual activity localization in videos, featuring three data sets: UAG-OOPS, UAG-SSBD, UAG-FunQA, and an instruction-tune dataset OOPS-UAG-Instruct to improve model capabilities.

**Data Type**: video

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://drive.google.com/drive/folders/1eE_ngd-E6rjdHz0KKttJATzsdxv4Wf_e?usp=sharing)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate models' capabilities in localizing unusual activities in videos and to outline challenges in current methodologies.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Video Activity Localization

**Limitations**: N/A

## 💾 Data

**Source**: Three datasets: UAG-OOPS, UAG-SSBD, UAG-FunQA, and one instruction-tune dataset OOPS-UAG-Instruct.

**Size**: 1,589 videos for UAG-OOPS, 75 videos for UAG-SSBD, 172 videos for UAG-FunQA, 3,778 videos for OOPS-UAG-Instruct.

**Format**: Not explicitly stated

**Annotation**: Annotations include start and end timestamps for activities.

## 🔬 Methodology

**Methods**:
- Evaluation of Video-Language Models (Vid-LLMs)
- Instruction-tuned Vid-LLMs
- Integration of Vision-Language Models and Large Language Models (VLM-LLM)

**Metrics**:
- R@1, IoU ≥m
- R@1, TD≤p
- mTD

**Calculation**: Performance is evaluated based on the localization metrics that measure how well predicted timestamps overlap with ground truth.

**Interpretation**: Higher R@1 and lower mTD indicate better performance.

**Baseline Results**: Random method as a baseline which serves as a lower performance indicator.

**Validation**: Proposed evaluation protocol includes zero-shot settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
