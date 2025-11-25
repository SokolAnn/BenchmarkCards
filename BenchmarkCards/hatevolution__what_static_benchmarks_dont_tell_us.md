# Hatevolution: What Static Benchmarks Don’t Tell Us

## 📊 Benchmark Details

**Name**: Hatevolution: What Static Benchmarks Don’t Tell Us

**Overview**: This paper investigates the impact of evolving language on hate speech benchmarking, suggesting the need for time-sensitive linguistic benchmarks, given that current static benchmarks do not account for language evolution.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HateXplain
- Implicit Hate Corpus
- HateCheck
- Dynabench

**Resources**:
- [GitHub Repository](https://github.com/ChiaraDiBonaventura/hatevolution/tree/main)

## 🎯 Purpose and Intended Users

**Goal**: To empirically evaluate the robustness of language models across evolving hate speech detection tasks.

**Target Audience**:
- ML Researchers
- Model Developers
- NLP Practitioners

**Tasks**:
- Hate Speech Detection

**Limitations**: Static benchmarks do not account for the evolving nature of hate speech language.

## 💾 Data

**Source**: Publicly available datasets like Singapore Online Attacks and NeoBench for hate speech detection.

**Size**: N/A

**Format**: N/A

**Annotation**: Manual annotation by experts with substantial agreement (Cohen’s Kappa = 0.67).

## 🔬 Methodology

**Methods**:
- Zero-shot prompting

**Metrics**:
- F1 Score

**Calculation**: The macro F1 score is calculated across time-sensitive evaluations.

**Interpretation**: High and stable time-sensitive F1 scores indicate better adaptation to evolving contexts of hate speech.

**Baseline Results**: Baseline scores from established hate speech models.

**Validation**: Empirical evaluation across different years.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: Potential misalignment could lead to overestimation of language models’ safety.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
