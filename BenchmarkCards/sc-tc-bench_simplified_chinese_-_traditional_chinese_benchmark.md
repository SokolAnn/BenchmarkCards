# SC-TC-Bench (Simplified Chinese - Traditional Chinese Benchmark)

## 📊 Benchmark Details

**Name**: SC-TC-Bench (Simplified Chinese - Traditional Chinese Benchmark)

**Overview**: We provide an open-sourced benchmark dataset to foster reproducible evaluations of future LLM behavior across Chinese language variants.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- ACLUE
- SuperCLUE
- AlignBench

**Resources**:
- [GitHub Repository](https://github.com/brucelyu17/SC-TC-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To investigate potential LLM performance disparities when prompted in Simplified versus Traditional Chinese and to audit the performance and biases of LLMs in these language variants.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Regional Term Choice
- Regional Name Choice

**Limitations**: The benchmark covers several important real-world contexts but does not comprehensively cover all differences in Simplified and Traditional Chinese.

## 💾 Data

**Source**: Dataset includes question-answer pairs reflecting regional term choice and regional name choice tasks, collected with the help of native speakers and manual reviews.

**Size**: 110 regional terms

**Format**: JSON

**Annotation**: Manually verified by native speakers.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Calculated based on the percentage of correct responses in relation to regional term identification and name selection tasks.

**Interpretation**: Higher accuracy indicates better performance in recognizing regional terms and names specific to Simplified and Traditional Chinese prompts.

**Baseline Results**: Comparative performance of 11 leading commercial and open-source LLMs in regional term choice and name selection tasks.

**Validation**: Results were verified through multiple prompting trials and statistical analyses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark considers the implications of different regional biases, reflecting the cultural significance of language usage in Mainland China and Taiwan.

**Potential Harm**: Potential representational harms in LLMs' outputs when prompted in varying Chinese language scripts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution 4.0 International License (CC BY 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
