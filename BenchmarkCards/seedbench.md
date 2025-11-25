# SeedBench

## 📊 Benchmark Details

**Name**: SeedBench

**Overview**: SeedBench is the first multi-task benchmark specifically designed for seed science, simulating key aspects of modern breeding processes to evaluate large language models (LLMs) in seed breeding.

**Data Type**: question-answering pairs

**Domains**:
- Agriculture
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- AgEval
- AgXQA

**Resources**:
- [GitHub Repository](https://github.com/open-sciencelab/SeedBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of large language models (LLMs) in effectively addressing seed breeding tasks.

**Target Audience**:
- Research Scientists
- AI Practitioners
- Agricultural Experts

**Tasks**:
- Gene Information Retrieval
- Gene Function Prediction
- Variety Breeding Process Query

**Limitations**: N/A

## 💾 Data

**Source**: 308,727 breeding-related publications in English and Chinese were extracted to build a knowledge base for SeedBench.

**Size**: 2,264 questions

**Format**: Markdown

**Annotation**: Expert-validated and machine-processed question-answer pairs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Macro-F1
- ROUGE-L

**Calculation**: Metrics calculated based on comparing model outputs to reference answers.

**Interpretation**: Higher scores indicate better model performance in seed breeding tasks.

**Validation**: Evaluation was performed using one-shot and zero-shot testing methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC-BY 4.0, MIT, Apache 2.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
