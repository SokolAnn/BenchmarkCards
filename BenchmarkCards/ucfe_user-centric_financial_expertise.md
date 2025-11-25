# UCFE (User-Centric Financial Expertise)

## 📊 Benchmark Details

**Name**: UCFE (User-Centric Financial Expertise)

**Overview**: The UCFE benchmark is designed to evaluate the ability of large language models (LLMs) to handle complex real-world financial tasks through user-centric interactions and expert evaluations.

**Data Type**: multi-round dialogue interactions involving financial tasks

**Domains**:
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- FLARE
- MMMU
- MMMU-PRO

**Resources**:
- [GitHub Repository](https://github.com/TobyYang7/UCFE-Benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous framework for assessing LLM performance in complex financial scenarios based on user interactions.

**Target Audience**:
- Financial Analysts
- Financial Professionals
- Regulatory Professionals
- General Public

**Tasks**:
- Financial Knowledge Consulting
- Asset Valuation Reporting
- Investment Strategy Evaluation
- Credit Risk Evaluation
- Market Information Summarization

**Limitations**: The benchmark may not fully capture all real-world financial applications due to task coverage limitations.

## 💾 Data

**Source**: Collected user interaction data and financial task scenarios based on user surveys.

**Size**: 330 data points encompassing various user intents and financial tasks.

**Format**: N/A

**Annotation**: Data collected through user surveys and expert evaluations.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Model-based evaluation
- LLM-as-Judge methodology

**Metrics**:
- Pearson correlation
- Elo scores

**Calculation**: Metrics are calculated using user preferences alignment and performance comparisons via Elo rating system.

**Interpretation**: A higher Pearson correlation indicates alignment with human preferences; Elo scores rank model performance.

**Baseline Results**: Model benchmarks exhibited a Pearson correlation of 0.78 in alignment with human evaluations.

**Validation**: Validated using multiple LLM evaluators to assess the robustness of results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Robustness**: Prompt injection attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis included diverse user groups reflecting different financial expertise levels.

**Potential Harm**: The framework aims to minimize biases and ensure equitable model performance across user demographics.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User data collected followed ethical guidelines with no harmful outcomes expected.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent obtained from all survey participants.

**Compliance With Regulations**: Not Applicable
