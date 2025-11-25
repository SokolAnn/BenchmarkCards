# EconNLI (Economic Natural Language Inference)

## 📊 Benchmark Details

**Name**: EconNLI (Economic Natural Language Inference)

**Overview**: EconNLI is a dataset designed to evaluate Large Language Models’ knowledge and reasoning abilities in the economic domain, specifically focusing on natural language inference about economic events.

**Data Type**: sentence pairs of premise and hypothesis

**Domains**:
- Economics

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/Irenehere/EconNLI)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the economic reasoning abilities of Large Language Models using natural language inference.

**Target Audience**:
- ML Researchers
- Economists
- Financial Analysts

**Tasks**:
- Causal Inference Classification
- Event Generation

**Limitations**: The study does not address the reasoning ability of LLMs in non-economic domains.

## 💾 Data

**Source**: Wikipedia corpus on economics and finance

**Size**: 11,836 examples

**Format**: N/A

**Annotation**: Annotated by human experts and assisted by language models.

## 🔬 Methodology

**Methods**:
- Supervised fine-tuning
- Zero-shot prompting
- In-context learning (ICL) prompting
- Chain of thought (CoT) prompting

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated based on model predictions compared to ground truth labels.

**Interpretation**: Higher scores in accuracy and F1 indicate better performance in reasoning tasks.

**Baseline Results**: LLAMA2 models achieved F1 scores around 0.87, while BERT and FinBERT struggled with scores below 0.8.

**Validation**: A validation set was created by randomly sampling 10% of the training data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
