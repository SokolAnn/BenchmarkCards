# FFT (Factuality, Fairness, Toxicity)

## 📊 Benchmark Details

**Name**: FFT (Factuality, Fairness, Toxicity)

**Overview**: FFT is a benchmark consisting of 2,116 carefully crafted instances evaluated from three aspects: factuality, fairness, and toxicity, to expand the evaluation scope beyond toxicity.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/cuishiyao96/FFT)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the potential harms of large language models (LLMs) from a broader perspective beyond toxicity.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Factuality Evaluation
- Fairness Evaluation
- Toxicity Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Manually crafted and automatically generated instances for evaluating LLMs.

**Size**: 2,116 instances

**Format**: N/A

**Annotation**: Manually curated misinformation, fairness scenarios, and toxicity prompts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Coefficient of Variation (CV)

**Calculation**: Accuracy is calculated based on the correctness of responses according to predefined rules.

**Interpretation**: Higher accuracy indicates better performance in factuality, while lower CV values indicate better fairness across identities.

**Baseline Results**: N/A

**Validation**: Evaluation was conducted on 9 representative LLMs covering various parameter scales and training stages.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Identity-sensitive evaluation involving gender, race, and religion.

**Potential Harm**: The benchmark aims to detect and evaluate harms related to Factuality, Fairness, and Toxicity within LLM responses.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
