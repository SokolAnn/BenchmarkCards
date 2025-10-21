# SciFaultyQA

## 📊 Benchmark Details

**Name**: SciFaultyQA

**Overview**: SciFaultyQA is a dataset of intentionally faulty science questions designed to evaluate the ability of large language models (LLMs) to recognize and appropriately respond to flawed questions. The dataset includes both text-based and image-text combined questions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SciQA
- GPQA

**Resources**:
- [GitHub Repository](https://github.com/DebarshiKunduPSU/SciFaultyQA)

## 🎯 Purpose and Intended Users

**Goal**: To assess LLMs' ability to identify and handle logically or scientifically flawed questions.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated using GAN-inspired and diffusion-inspired methods from existing science question datasets.

**Size**: 1,333 examples

**Format**: JSON

**Annotation**: Automatically generated with reasoning provided for fault types.

## 🔬 Methodology

**Methods**:
- Iterative Generative Adversarial Network
- Multi-Agent Systems
- Tool Integration

**Metrics**:
- Detection Rate
- Accuracy

**Calculation**: Performance of models evaluated based on their ability to identify faulty questions.

**Interpretation**: Detection rates indicate the proportion of faulty questions that models correctly identify.

**Baseline Results**: GPT 4o: Baseline accuracy of 16%, improved to 65% with web search integration.

**Validation**: Results validated through iterative feedback from multiple LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
