# GenderCARE

## 📊 Benchmark Details

**Name**: GenderCARE

**Overview**: GenderCARE is a comprehensive framework that encompasses innovative criteria, bias assessment, reduction techniques, and evaluation metrics for quantifying and mitigating gender bias in large language models.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Winoqueer
- BOLD
- StereoSet

**Resources**:
- [GitHub Repository](https://github.com/kstanghere/GenderCARE-ccs24)

## 🎯 Purpose and Intended Users

**Goal**: To assess and reduce gender bias in large language models.

**Target Audience**:
- ML Researchers
- AI Ethicists
- Model Developers

**Tasks**:
- Gender Bias Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Constructed using counterfactual data augmentation and expert reviews.

**Size**: 103,854 prompts across 207 distinct gender identities

**Format**: N/A

**Annotation**: Human construction and GPT-4 review for anti-biased descriptor generation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Bias-Pair Ratio
- Toxicity
- Regard

**Calculation**: Bias-Pair Ratio measures the proportion of biased descriptors selected by the model; Toxicity and Regard measure harmfulness and sentiment, respectively.

**Interpretation**: Lower scores in Bias-Pair Ratio and Toxicity indicate reduced gender bias; higher Regard scores indicate positive sentiment.

**Baseline Results**: Compared against Winoqueer, BOLD, and StereoSet benchmarks.

**Validation**: Extensive experiments on 17 different LLMs demonstrate the robustness of the GenderPair framework.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark includes diverse gender identities, including transgender and non-binary individuals.

**Potential Harm**: The framework aims to prevent the perpetuation of harmful stereotypes and biases against marginalized gender identities.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
