# BIGbench

## 📊 Benchmark Details

**Name**: BIGbench

**Overview**: BIGbench is a unified benchmark for evaluating multi-dimensional social biases in Text-to-Image (T2I) models, featuring a carefully designed dataset of 47,040 prompts categorized across four dimensions of bias.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- DALL-EV AL
- HRS-Bench
- ENTIGEN
- TIBET

**Resources**:
- [GitHub Repository](https://github.com/username/bigbench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for identifying and analyzing social biases in T2I models.

**Target Audience**:
- ML Researchers
- AI Ethics Scholars
- Industry Practitioners

**Tasks**:
- Bias Evaluation

**Limitations**: The benchmark's algorithm utilizes only implicit prompts for calculating the manifestation factor, which may lead to incomplete bias analysis.

## 💾 Data

**Source**: Constructed dataset consisting of 47,040 prompts, covering occupations, characteristics, and social relations.

**Size**: 47,040 prompts

**Format**: N/A

**Annotation**: Data mainly evaluated using automated alignment via a multi-modal LLM and verified through human evaluation.

## 🔬 Methodology

**Methods**:
- Automated evaluation
- Human evaluation

**Metrics**:
- Implicit bias score
- Explicit bias score
- Manifestation factor

**Calculation**: Scores are calculated based on the proportions of demographic attributes generated versus expected demographic distributions.

**Interpretation**: A higher implicit or explicit bias score indicates a lower level of bias in the model's outputs.

**Baseline Results**: The benchmark evaluated eight mainstream T2I models and three debiasing methods.

**Validation**: Human evaluations were conducted to ensure reliability, with trained evaluators assessing the generated images.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark includes demographic breakdowns across various bias dimensions in T2I models.

**Potential Harm**: The benchmark aims to detect and mitigate harms related to entrenched social stereotypes and biases in AI-generated content.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Openly accessible under GPL v3.0.

**Consent Procedures**: All evaluators provided informed consent prior to the study.

**Compliance With Regulations**: Not Applicable
