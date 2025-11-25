# Large Language Models as Medical Codes Selectors: a benchmark using the International Classification of Primary Care

## 📊 Benchmark Details

**Name**: Large Language Models as Medical Codes Selectors: a benchmark using the International Classification of Primary Care

**Overview**: This paper presents a benchmark assessing the potential of large language models (LLMs) to assign ICPC-2 codes using a dataset of Brazilian Portuguese clinical expressions. Performance is evaluated using F1-score alongside other factors.

**Data Type**: text

**Domains**:
- Healthcare

**Languages**:
- Portuguese

**Resources**:
- [GitHub Repository](https://github.com/almeidava93/llm-as-code-selectors-paper)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of large language models in selecting ICPC-2 codes from clinical expressions and provide a benchmark for future studies.

**Target Audience**:
- Healthcare Researchers
- Medical Coders
- AI Researchers

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: A dataset of 437 Brazilian Portuguese clinical expressions annotated with ICPC-2 codes was used for evaluation.

**Size**: 437 examples

**Format**: N/A

**Annotation**: Annotated by peers with experience in medical coding.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- F1 Score

**Calculation**: F1 = 2TP / (2TP + FP + FN), where TP is true positives, FP is false positives, FN is false negatives.

**Interpretation**: Higher F1 Score indicates better model performance in selecting relevant ICPC-2 codes.

**Baseline Results**: Baseline F1-score of 0.8044 from selecting the first result of the search engine.

**Validation**: Evaluation metrics were computed for each model based on their selected codes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
