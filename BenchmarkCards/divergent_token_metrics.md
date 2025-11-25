# Divergent Token Metrics

## 📊 Benchmark Details

**Name**: Divergent Token Metrics

**Overview**: This study introduces Divergent Token Metrics (DTMs), a novel approach to assessing compressed LLMs, aiming to evaluate performance degradation during model compression processes, specifically targeting the first divergent token in generated text. DTMs provide a more nuanced evaluation compared to traditional metrics like perplexity, allowing for individual component assessment and effective compression strategies.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- PPL (Perplexity)

**Resources**:
- [GitHub Repository](https://github.com/Aleph-Alpha/Divergent_Tokens)

## 🎯 Purpose and Intended Users

**Goal**: To provide a new metric for evaluating the performance degradation of compressed large language models during model compression processes, emphasizing the importance of component-level analyses.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Model Compression Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: The data source includes the Llama2 models and the C4 dataset for training evaluations.

**Size**: 20,000 examples

**Format**: JSON

**Annotation**: Automated annotation through model outputs and evaluations.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Component-wise evaluation
- Model performance analysis

**Metrics**:
- Divergent Token Metrics (DTM)
- First Divergent Token Metric (FDTM)
- Share of Divergent Tokens Metric (SDTM)
- Perplexity (PPL)

**Calculation**: Metrics calculated to assess model divergence during compression based on token outputs comparing original and compressed models.

**Interpretation**: Higher DTM scores indicate better retention of model performance during compression.

**Validation**: Validation performed on various compression scenarios across Llama2 models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
