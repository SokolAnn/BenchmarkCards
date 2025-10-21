# Panel of LLm Evaluators (PoLL)

## 📊 Benchmark Details

**Name**: Panel of LLm Evaluators (PoLL)

**Overview**: The benchmark proposes to evaluate LLM generations using a Panel of LLM evaluators (PoLL) instead of relying on single large judges, demonstrating better correlation with human judgements and cost-effectiveness.

**Data Type**: evaluation scores

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU

**Resources**:
- [GitHub Repository](https://github.com/lm-sys/arena-hard)

## 🎯 Purpose and Intended Users

**Goal**: To provide a more effective method for evaluating LLM performance while reducing costs and biases associated with single large model evaluations.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The current work only addresses three evaluator settings and a limited number of judges, indicating the need for broader applicability investigations.

## 💾 Data

**Source**: Evaluations conducted using diverse datasets including KILT.

**Size**: N/A

**Format**: N/A

**Annotation**: Human annotations were performed, comprising diverse professional backgrounds.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Cohen’s κ
- Pearson Correlation
- Kendall Tau

**Calculation**: Cohen’s kappa measures inter-rater reliability across different evaluators.

**Interpretation**: A Cohen’s kappa value over 0.6 indicates a moderate correlation, and over 0.8 indicates strong agreement.

**Baseline Results**: PoLL achieved the highest correlation scores with human judgments across various tasks.

**Validation**: Validation processes were based on correlation with human judgments and other established datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Annotations included diverse backgrounds to minimize bias.

**Potential Harm**: Reducing intra-model bias in evaluations to improve fairness.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
