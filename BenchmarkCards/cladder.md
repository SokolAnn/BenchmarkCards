# CLADDER

## 📊 Benchmark Details

**Name**: CLADDER

**Overview**: CLADDER is a dataset designed to evaluate the ability of large language models to perform causal reasoning by presenting them with causal inference questions based on structured causal graphs. The dataset includes over 10,000 samples and is grounded in formal causal inference rules.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CRASS

**Resources**:
- [Resource](https://huggingface.co/datasets/causalNLP/cladder)
- [GitHub Repository](https://github.com/causalNLP/cladder)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the formal causal reasoning abilities of large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Causal Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Generated dataset based on causal inference principles and causal graphs.

**Size**: 10,112 samples

**Format**: JSON

**Annotation**: Automatically generated using a causal inference engine.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Results computed based on model predictions against ground-truth answers.

**Interpretation**: Accuracy measures the proportion of correct responses out of total questions.

**Baseline Results**: Vanilla GPT-4 achieves an accuracy of 62.03%. With CAUSAL COT, it improves to 70.40%.

**Validation**: Extensive experiments conducted on various language models to verify the effectiveness of the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
