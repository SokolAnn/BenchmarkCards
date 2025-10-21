# Medical AI Consensus: A Multi-Agent Framework for Radiology Report Generation and Evaluation

## 📊 Benchmark Details

**Name**: Medical AI Consensus: A Multi-Agent Framework for Radiology Report Generation and Evaluation

**Overview**: The proposed framework serves as both a benchmark and evaluation environment for multimodal clinical reasoning in the radiology ecosystem, integrating large language models (LLMs) and large vision models (LVMs) through a modular architecture composed of ten specialized agents responsible for image analysis, feature extraction, report generation, review, and evaluation.

**Data Type**: multimodal

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2509.17353)

## 🎯 Purpose and Intended Users

**Goal**: To establish a multi-agent benchmarking framework designed to evaluate LLMs and LVMs throughout an end-to-end pipeline of radiology report generation.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Medical Researchers

**Tasks**:
- Report Generation
- Image Analysis
- Clinical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Curated benchmark dataset of multisequence brain MRI scans from cancer patients, annotated by board-certified radiologists.

**Size**: N/A

**Format**: N/A

**Annotation**: Annotated under the supervision of board-certified radiologists.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score
- ROUGE
- Clinical Accuracy
- Readability

**Calculation**: Metrics are calculated using various standard classification and segmentation metrics.

**Interpretation**: Good performance is indicated by high accuracy scores and evaluation agent calibration with expert ratings.

**Baseline Results**: Overall accuracy achieved by the pipeline was 68.6% on the RHUH-GBM dataset.

**Validation**: Validation of the framework was conducted through extensive evaluation against expert radiologist evaluations and shared scoring scripts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
