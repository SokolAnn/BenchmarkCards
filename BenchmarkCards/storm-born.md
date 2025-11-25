# STORM-BORN

## 📊 Benchmark Details

**Name**: STORM-BORN

**Overview**: STORM-BORN is a dataset designed to provide challenging mathematical derivations, sourced from recent academic papers. It ensures high-quality data through a human-in-the-loop and multi-agent framework, showcasing complex mathematical reasoning that LLMs struggle to solve.

**Data Type**: math derivation pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MATH
- GSM8K

**Resources**:
- [GitHub Repository](https://github.com/lwhere/STORM-BORN)

## 🎯 Purpose and Intended Users

**Goal**: To advance the reasoning capabilities of large language models through a dataset of complex mathematical problems.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Filtered academic papers from arXiv.

**Size**: 2,000 synthetic samples

**Format**: JSON

**Annotation**: Curated with human evaluations for complexity and correctness.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Multi-agent data generation framework

**Metrics**:
- Accuracy

**Calculation**: Evaluation includes manual scoring of mathematical proofs by experts against ground truth.

**Interpretation**: Higher scores indicate stronger reasoning capabilities.

**Baseline Results**: Less than 5% accuracy on STORM-BORN for models like GPT-o1-Pro.

**Validation**: Validated through expert reviews and comparative evaluations against state-of-the-art models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
