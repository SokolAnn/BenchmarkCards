# MM-EVAL (Multilingual Meta-Evaluation Benchmark)

## 📊 Benchmark Details

**Name**: MM-EVAL (Multilingual Meta-Evaluation Benchmark)

**Overview**: MM-EVAL is a multilingual meta-evaluation benchmark comprising five core subsets covering 18 languages and a Language Consistency subset spanning 122 languages, designed to assess evaluator LLMs' capabilities across multiple languages with a focus on multilingual-specific challenges.

**Data Type**: evaluation pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Spanish
- French
- German
- Italian
- Chinese
- Japanese
- Korean
- Arabic
- Russian
- Swahili
- Bengali
- Catalan
- Galician
- Thai
- Telugu

**Similar Benchmarks**:
- M-RewardBench
- RewardBench
- LLMBar

**Resources**:
- [GitHub Repository](https://github.com/guijinSON/MM-Eval)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust evaluation framework for assessing the performance of evaluator LLMs across a wide range of languages and ensuring fairness and consistency in evaluations.

**Target Audience**:
- ML Researchers
- Evaluation Methodologists
- Language Technology Developers

**Tasks**:
- Evaluation of Language Models

**Limitations**: N/A

## 💾 Data

**Source**: The dataset was constructed from various multilingual data sources, curated specifically for MM-EVAL, ensuring that each entry undergoes thorough validation to maintain quality.

**Size**: 4,981 instances

**Format**: N/A

**Annotation**: Data was annotated through a combination of manual and automated processes, ensuring reliability and validity.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Language Consistency Index (LCI)

**Calculation**: Metrics are calculated based on the evaluators' ability to distinguish between chosen and rejected responses across different languages.

**Interpretation**: Higher scores indicate better performance in correctly assessing multilingual outputs.

**Baseline Results**: Existing evaluators showed an average accuracy of 68.9%, highlighting the need for improvements in multilingual contexts.

**Validation**: The benchmark was validated by measuring its correlation with Best-of-N rankings, indicating its effectiveness in real-world evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The data used for constructing MM-EVAL is licensed under various open licenses, including CC-BY-SA.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
