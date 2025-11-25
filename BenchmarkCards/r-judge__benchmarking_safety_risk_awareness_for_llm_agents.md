# R-Judge: Benchmarking Safety Risk Awareness for LLM Agents

## 📊 Benchmark Details

**Name**: R-Judge: Benchmarking Safety Risk Awareness for LLM Agents

**Overview**: R-Judge is a benchmark crafted to evaluate the proficiency of large language models (LLMs) in judging and identifying safety risks given agent interaction records. It consists of 569 records of multi-turn agent interactions across various application scenarios and risk types.

**Data Type**: interaction records

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SafetyBench
- SuperCLUE-Safety

**Resources**:
- [GitHub Repository](https://github.com/Lordog/R-Judge)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the risk awareness of LLMs in managing and identifying safety risks in agent interactions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Risk Identification
- Safety Judgment

**Limitations**: N/A

## 💾 Data

**Source**: Curated from existing interaction records with human safety annotations.

**Size**: 569 examples

**Format**: Custom annotated format

**Annotation**: Annotated with binary safety labels and risk descriptions by trained human annotators.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- F1 Score
- Recall
- Specificity
- Effectiveness

**Calculation**: Metrics are calculated based on binary classification principles comparing model outputs to human annotations.

**Interpretation**: Higher scores indicate better performance in judging safety risks and identifying potentially unsafe actions.

**Baseline Results**: GPT-4o achieved the highest F1 score of 74.45% in safety judgment.

**Validation**: The benchmark was validated through assessments of model performance against human evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Privacy
- Risk Awareness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Privacy**: Personal information in data
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All user data are anonymized in the dataset to prevent potential breaches.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
