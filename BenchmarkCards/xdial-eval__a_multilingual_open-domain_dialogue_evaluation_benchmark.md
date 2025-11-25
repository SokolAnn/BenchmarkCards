# xDial-Eval: A Multilingual Open-Domain Dialogue Evaluation Benchmark

## 📊 Benchmark Details

**Name**: xDial-Eval: A Multilingual Open-Domain Dialogue Evaluation Benchmark

**Overview**: xDial-Eval is a multilingual dialogue evaluation benchmark featuring 14,930 annotated turns and 8,691 dialogues in 10 languages, enabling comprehensive analyses of automatic metrics across languages.

**Data Type**: turn-level and dialogue-level annotated data

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- Spanish
- German
- French
- Japanese
- Korean
- Hindi
- Arabic
- Russian

**Similar Benchmarks**:
- DailyDialog
- Persona

**Resources**:
- [GitHub Repository](https://github.com/e0397123/xDial-Eval)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of automatic dialogue evaluation metrics across multiple languages and improve multilingual dialogue evaluation methods.

**Target Audience**:
- ML Researchers
- Dialogue System Developers

**Tasks**:
- Dialogue Evaluation
- Metrics Comparison

**Limitations**: The research primarily focuses on context relevance and dialogue coherence; further multidimensional evaluation aspects are suggested for future studies.

## 💾 Data

**Source**: 12 turn-level and 6 dialogue-level open-source English evaluation datasets translated into 9 languages.

**Size**: 14,930 annotated turns and 8,691 annotated dialogues

**Format**: CSV

**Annotation**: Annotated by human evaluators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Pearson correlation
- Spearman correlation

**Calculation**: Metrics calculated based on the correlation between automatic scores and human judgments.

**Interpretation**: High correlation scores indicate better performance of models in dialogue evaluation.

**Baseline Results**: Comparison to state-of-the-art BERT-based metrics and various LLMs.

**Validation**: Comprehensive analyses conducted are cross-validated against multiple datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Exposing personal information

**Demographic Analysis**: Evaluation across multiple languages provides insights into biases affecting different linguistic groups.

**Potential Harm**: Potential misuse in evaluation settings without adequate context for culturally sensitive dialogue.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data is sourced from publicly accessible datasets with no personally identifiable information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
