# MedAtlas

## 📊 Benchmark Details

**Name**: MedAtlas

**Overview**: MedAtlas is a novel benchmark framework designed to evaluate large language models on realistic medical reasoning tasks. It includes features such as multi-turn dialogue, multi-modal medical image interaction, multi-task integration, and high clinical fidelity, supporting tasks like multi-turn question answering and disease diagnosis.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- VQA-RAD
- SLAKE
- PMC-VQA
- OmniMedVQA

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To establish a challenging evaluation platform for advancing the development of robust and trustworthy medical AI.

**Target Audience**:
- ML Researchers
- Model Developers
- Healthcare Practitioners

**Tasks**:
- Open-ended Question Answering
- Closed-ended Question Answering
- Comprehensive Disease Diagnosis

**Limitations**: N/A

## 💾 Data

**Source**: The MedAtlas dataset is derived from publicly available medical case repositories and expert clinical case collections.

**Size**: 804 cases, 5632 medical images

**Format**: N/A

**Annotation**: Expert-annotated gold standards for all tasks

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Round Chain Accuracy
- Error Propagation Resistance
- BLEU Score
- ROUGE-L

**Calculation**: Metrics are calculated based on the accuracy of answers against ground truth, with specific emphasis on multi-turn reasoning consistency.

**Interpretation**: A high Round Chain Accuracy indicates effective sequential reasoning across multiple questions.

**Baseline Results**: Evaluated models include GPT-4o, Claude-sonnet-4, and LLaMA-4-Maverick, with varied accuracy scores.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
