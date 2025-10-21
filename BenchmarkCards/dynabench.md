# Dynabench

## 📊 Benchmark Details

**Name**: Dynabench

**Overview**: Dynabench is an open-source platform for dynamic dataset creation and model benchmarking which allows dataset creation, model development, and model assessment to inform each other, leading to more robust and informative benchmarks.

**Data Type**: dynamic data collection

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SQuAD
- GLUE
- SuperGLUE
- ANLI

**Resources**:
- [Resource](https://dynabench.org)

## 🎯 Purpose and Intended Users

**Goal**: To provide a platform for dynamic benchmarking that allows for a continuous cycle of data collection and model evaluation to address the shortcomings of traditional static benchmarks.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Natural Language Inference
- Question Answering
- Sentiment Analysis
- Hate Speech Detection

**Limitations**: N/A

## 💾 Data

**Source**: Various sources including crowd-sourced annotations and existing datasets like SQuAD and ANLI.

**Size**: Total of ~263,000 examples across tasks

**Format**: N/A

**Annotation**: Crowdsourced and expert-annotated

## 🔬 Methodology

**Methods**:
- Human-and-model-in-the-loop evaluation

**Metrics**:
- Validation Model Error Rate (vMER)

**Calculation**: The ratio of human-validated model errors to total examples.

**Interpretation**: Lower vMER indicates better model performance when interacting with humans.

**Baseline Results**: Initial vMERs vary by task: NLI 33.24%, QA 33.74%, Sentiment 35.00%, Hate speech 43.90%

**Validation**: Multiple rounds of data collection and validation via human assessment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Prompt injection attack
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
