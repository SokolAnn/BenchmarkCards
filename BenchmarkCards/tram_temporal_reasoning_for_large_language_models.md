# TRAM (Temporal Reasoning for Large Language Models)

## 📊 Benchmark Details

**Name**: TRAM (Temporal Reasoning for Large Language Models)

**Overview**: TRAM is a temporal reasoning benchmark composed of ten datasets, encompassing various temporal aspects of events such as order, arithmetic, frequency, and duration, designed for evaluating the TeR capabilities of large language models.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TimeBank
- TempEval-3
- MCTACO

**Resources**:
- [GitHub Repository](https://github.com/EternityYW/TRAM-Benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To establish a standard for evaluating temporal reasoning in large language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Temporal Reasoning

**Limitations**: N/A

**Out of Scope Uses**:
- Evaluation tasks that diverge from temporal reasoning such as those requiring contextual emotional intelligence.

## 💾 Data

**Source**: Combination of existing datasets (MCTACO, SQuAD) and human-curated problems.

**Size**: 526,668 questions

**Format**: multiple-choice questions

**Annotation**: Derived through a combination of expert annotations and programmatic generation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the performance of LLMs on the multiple-choice format of the tasks.

**Interpretation**: Higher accuracy indicates better temporal reasoning capabilities of the models.

**Baseline Results**: Human experts achieved an average accuracy of 95.2%.

**Validation**: Extensive evaluation was conducted on various popular language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

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
