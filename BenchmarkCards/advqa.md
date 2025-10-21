# ADVQA

## 📊 Benchmark Details

**Name**: ADVQA

**Overview**: ADVQA is a newly created human-grounded adversarial question answering dataset that utilizes the ADVSCORE metric for evaluating adversarialness, aiming to provide realistic and high-quality adversarial samples to test model robustness.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TRICKME
- FM2
- BAMBOOGLE

**Resources**:
- [GitHub Repository](https://github.com/yysung/Advscore)

## 🎯 Purpose and Intended Users

**Goal**: The main objective of ADVQA is to provide a robust evaluation framework for assessing the adversarialness of datasets by incorporating human performance into adversarial question answering tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: ADVQA may become less effective over time as models improve and may require periodic updates.

## 💾 Data

**Source**: Collected through human responses from trivia competitions and crowd-sourced writings.

**Size**: 182 questions

**Format**: N/A

**Annotation**: Questions were curated and edited by expert writers based on human feedback in a competitive setting.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- ADVSCORE

**Calculation**: ADVSCORE is calculated using item response theory (IRT), evaluating the margin of human vs. model performance and question discriminability.

**Interpretation**: Higher ADVSCORE values indicate more adversarial and discriminative questions.

**Baseline Results**: N/A

**Validation**: ADVQA's effectiveness is validated against existing adversarial benchmarks like TRICKME and FM2.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Participant privacy was protected under an official IRB review, and consent was obtained for using their responses.

**Data Licensing**: Not Applicable

**Consent Procedures**: Consent forms were collected to allow the use of responses for academic purposes.

**Compliance With Regulations**: The study complied with ethical standards for human subjects research.
