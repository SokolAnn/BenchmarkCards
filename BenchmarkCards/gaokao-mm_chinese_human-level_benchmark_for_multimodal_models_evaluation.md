# GAOKAO-MM (Chinese Human-Level Benchmark for Multimodal Models Evaluation)

## 📊 Benchmark Details

**Name**: GAOKAO-MM (Chinese Human-Level Benchmark for Multimodal Models Evaluation)

**Overview**: GAOKAO-MM is a multimodal benchmark based on the Chinese College Entrance Examination (GAOKAO), comprising 646 questions across 8 subjects and featuring diverse images. It evaluates large vision-language models (LVLMs) on human-level capabilities including perception, understanding, knowledge, and reasoning, presenting a significant challenge as none of the tested models achieved over 50% accuracy.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- Chinese

**Similar Benchmarks**:
- VQA
- OK-VQA
- TextVQA

**Resources**:
- [GitHub Repository](https://github.com/OpenMOSS/GAOKAO-MM)

## 🎯 Purpose and Intended Users

**Goal**: Develop a comprehensive benchmark to assess multimodal abilities of LVLMs in a Chinese educational context.

**Target Audience**:
- ML Researchers
- Model Developers
- Educational Researchers

**Tasks**:
- Multimodal Question Answering

**Limitations**: The benchmark has room for improvement in scalability and balanced distribution of data.

## 💾 Data

**Source**: GAOKAO papers from 2010 to 2023 collected from the Internet.

**Size**: 646 questions and 897 images

**Format**: PDF

**Annotation**: Manually extracted multi-choice questions; images processed using OCR.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Rule-based answer extraction

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the percentage of correct answers across the evaluated models.

**Interpretation**: Models with accuracies below 50% were identified as having considerable room for improvement.

**Validation**: Models were evaluated through prompts designed to facilitate reasoning processes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: The benchmark addresses diverse educational subjects relevant to Chinese culture.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No private or sensitive information is included in the dataset.

**Data Licensing**: GAOKAO questions are considered to be in the public domain in China.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
