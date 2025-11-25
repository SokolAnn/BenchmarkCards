# VLind-Bench

## 📊 Benchmark Details

**Name**: VLind-Bench

**Overview**: VLind-Bench is the first benchmark specifically designed to measure the language priors, or blindness, of various Large Vision-Language Models (LVLMs) and disentangle the root causes of their failures.

**Data Type**: image-question pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- WHOOPS!
- ROME
- IfQA

**Resources**:
- [GitHub Repository](https://github.com/klee972/vlind-bench)

## 🎯 Purpose and Intended Users

**Goal**: To accurately measure language priors in LVLMs and evaluate various capabilities such as commonsense knowledge, visual perception, and commonsense biases.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated via prompts with oversight from graduate students.

**Size**: 14,248 image-question pairs

**Format**: N/A

**Annotation**: Manual verification by three graduate students.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Scores represent the average of the indicator values across all instances that have passed previous tests.

**Interpretation**: Higher scores indicate lesser reliance on language priors.

**Validation**: Conducted using handcrafted evaluation sets to ensure reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
