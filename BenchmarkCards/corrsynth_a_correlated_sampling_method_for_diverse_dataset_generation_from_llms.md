# CORRSYNTH (A Correlated Sampling Method for Diverse Dataset Generation from LLMs)

## 📊 Benchmark Details

**Name**: CORRSYNTH (A Correlated Sampling Method for Diverse Dataset Generation from LLMs)

**Overview**: CORRSYNTH generates datasets with high diversity and fidelity to the input prompt using a correlated sampling strategy, improving intrinsic metrics and student model performance across various tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2411.08553)

## 🎯 Purpose and Intended Users

**Goal**: To improve the diversity and quality of synthetic datasets generated for supervised text classification tasks.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Classification

**Limitations**: The current scope is limited to classification tasks in English. Extensions to other tasks or languages have not been validated.

## 💾 Data

**Source**: Datasets synthesized using LLMs such as MIXTRAL or PHI-3 MINI.

**Size**: Variable across tasks, typical generation targets include 6,000 instances per task.

**Format**: N/A

**Annotation**: Automatically generated

## 🔬 Methodology

**Methods**:
- Automated metrics
- Intrinsic evaluation

**Metrics**:
- Accuracy
- MAUVE
- Self-BLEU
- Entity-Entropy

**Calculation**: Metrics are calculated based on generated text compared to human-written text and the diversity of generated instances.

**Interpretation**: High accuracy indicates a good model performance on the synthetic data; lower Self-BLEU scores indicate higher diversity.

**Baseline Results**: Compared against existing text generation methods such as FEWGEN and CFG.

**Validation**: Validations were conducted through intrinsic evaluations showing improvements over baseline methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on education: plagiarism, Impact on affected communities
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Custom licenses for datasets such as AG NEWS and TOI HEADLINES.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
