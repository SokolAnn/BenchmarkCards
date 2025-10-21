# EDA Corpus: A Large Language Model Dataset for Enhanced Interaction with OpenROAD

## 📊 Benchmark Details

**Name**: EDA Corpus: A Large Language Model Dataset for Enhanced Interaction with OpenROAD

**Overview**: EDA Corpus is a curated dataset for physical design automation tasks, specifically designed for training Large Language Models (LLMs) in the context of the OpenROAD EDA toolchain.

**Data Type**: question-answer pairs and prompt-script pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/OpenROAD-Assistant/EDA-Corpus)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate LLM-focused research within the EDA domain and improve accessibility in chip design using OpenROAD.

**Target Audience**:
- ML Researchers
- EDA Practitioners

**Tasks**:
- Question Answering
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Collected from OpenROAD GitHub issues, discussions, and official documentation.

**Size**: 1,000 data points

**Format**: JSON

**Annotation**: Manually curated by OpenROAD experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy measured by evaluating the correctness of LLM-generated responses against factual answers.

**Interpretation**: Higher accuracy indicates better performance in generating correct answers and scripts.

**Baseline Results**: ChatGPT3.5 showed poor performance while fine-tuning improved accuracy significantly.

**Validation**: Dataset validation involved executing scripts in OpenROAD to verify correctness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Permissively licensed.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
