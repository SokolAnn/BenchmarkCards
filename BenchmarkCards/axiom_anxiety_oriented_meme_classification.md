# AxiOM (Anxiety Oriented Meme classification)

## 📊 Benchmark Details

**Name**: AxiOM (Anxiety Oriented Meme classification)

**Overview**: We propose a novel dataset, AxiOM, derived from the GAD anxiety questionnaire, which categorizes memes into six fine-grained anxiety symptoms.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RESTORE

**Resources**:
- [GitHub Repository](https://github.com/flamenlp/M3H)

## 🎯 Purpose and Intended Users

**Goal**: To understand and classify the mental health symptoms expressed in memes.

**Target Audience**:
- ML Researchers
- Mental Health Professionals

**Tasks**:
- Multimodal Classification

**Limitations**: N/A

## 💾 Data

**Source**: Various online sources including Reddit and Instagram, with memes categorized based on the GAD questionnaire.

**Size**: 3,582 memes

**Format**: N/A

**Annotation**: Annotated by healthcare professionals based on the GAD questionnaire.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Macro-F1
- Weighted-F1

**Calculation**: Weighted-F1 score calculated to evaluate performance across multiple symptoms.

**Interpretation**: Higher F1 scores indicate better classification performance.

**Baseline Results**: M3H achieves improvements of 4.94% on Macro-F1 and 4.20% on Weighted-F1 compared to baseline models.

**Validation**: Empirical validation against six competitive baselines.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All personally identifiable information (PII) is thoroughly anonymized to protect user privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
