# FB-Bench: A Fine-Grained Multi-Task Benchmark for Evaluating LLMs’ Responsiveness to Human Feedback

## 📊 Benchmark Details

**Name**: FB-Bench: A Fine-Grained Multi-Task Benchmark for Evaluating LLMs’ Responsiveness to Human Feedback

**Overview**: FB-Bench is a fine-grained, multi-task benchmark designed to evaluate LLMs’ responsiveness to human feedback under real-world usage scenarios in Chinese. It comprises 591 meticulously curated samples, encompassing eight task types, five deficiency types of response, and nine feedback types.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/PKU-Baichuan-MLSystemLab/FB-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To comprehensively evaluate the responsiveness of LLMs to various human feedback across real-world usage scenarios in Chinese.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Classification
- Error Correction
- Response Maintenance

**Limitations**: N/A

## 💾 Data

**Source**: The dataset was curated from a combination of online chat services and human preference data, ensuring high task diversity and authenticity.

**Size**: 591 samples

**Format**: N/A

**Annotation**: The data was annotated using a combination of GPT-4o for pre-annotation followed by human annotators for refinement and quality checks.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Models are evaluated based on their performance in following up on user feedback with scores determined by a weighted checklist.

**Interpretation**: Higher scores indicate better responsiveness to human feedback.

**Baseline Results**: N/A

**Validation**: The benchmark's robustness was validated through a comparison of performance across various popular LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
