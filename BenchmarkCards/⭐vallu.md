# VaLLu

## 📊 Benchmark Details

**Name**: VaLLu

**Overview**: VaLLu is a meticulously curated benchmark designed for the comprehensive evaluation of the cognitive capabilities of Large Vision-Language Models (LVLMs) across various reasoning tasks.

**Data Type**: Multimodal

**Domains**:
- Science
- Business
- Coding
- Engineering
- Maths
- Medicine

**Similar Benchmarks**:
- AMBER
- MMMU
- MathVista
- HallusionBench
- MATH-Vision
- MMC
- OVEN

**Resources**:
- [Resource](https://sreyan88.github.io/VDGD/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the cognitive capabilities of LVLMs in tasks that require open-ended generation and reasoning.

**Target Audience**:
- Researchers in AI and Machine Learning
- Developers of vision-language models
- Students studying AI

**Tasks**:
- Visual reasoning tasks
- Cognitive capabilities assessment
- Multimodal instruction evaluation

**Limitations**: N/A

**Out of Scope Uses**:
- Tasks not focused on cognitive assessment
- Binary Yes/No or Multi-choice questions

## 💾 Data

**Source**: Combination of existing datasets such as MMMU, MathVista, HallusionBench, MATH-Vision, and more.

**Size**: 1500 instances

**Format**: N/A

**Annotation**: Manually filtered for noisy examples and designed for open-ended generation tasks.

## 🔬 Methodology

**Methods**:
- Visual Description Grounded Decoding (VDGD)
- Expert evaluation for validation of results

**Metrics**:
- Accuracy of generated responses
- Factual correctness
- Engagement and clarity of responses

**Calculation**: N/A

**Interpretation**: Evaluation parameters included scores from 1 to 5 based on response quality.

**Validation**: Expert human evaluation and GPT-based scoring methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness
- Transparency

**Atlas Risks**:
- **Accuracy**: Poor model accuracy, Data contamination
- **Fairness**: Data bias, Output bias
- **Robustness**: Evasion attack, Data poisoning
- **Transparency**: Lack of training data transparency

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
