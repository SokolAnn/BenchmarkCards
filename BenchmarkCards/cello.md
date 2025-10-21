# CELLO

## 📊 Benchmark Details

**Name**: CELLO

**Overview**: CELLO is a benchmark for evaluating Large Language Models' (LLMs) ability to systematically follow complex instructions through a comprehensive dataset constructed from real-world scenarios, featuring a framework with eight characteristics for complex instructions.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/Abbey4799/CELLO)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the ability of LLMs to comprehend and follow complex instructions in real-world scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Complex Instruction Following

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from real-world scenarios and user interaction logs involving complex instructions.

**Size**: 523 samples

**Format**: JSON

**Annotation**: Manually annotated with agreement from multiple evaluators.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score

**Calculation**: Metrics are calculated based on predefined criteria including Count Limit, Answer Format, Task-prescribed Phrases, and Input-dependent Query.

**Interpretation**: Higher scores indicate better performance in following complex instructions.

**Validation**: Evaluated against multiple representative models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
