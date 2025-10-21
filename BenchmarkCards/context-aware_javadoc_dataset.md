# Context-Aware Javadoc Dataset

## 📊 Benchmark Details

**Name**: Context-Aware Javadoc Dataset

**Overview**: This study introduces a new dataset specifically for context-aware Javadoc documentation generation, incorporating critical structural and semantic information from modern Java codebases.

**Data Type**: code-Javadoc pairs

**Domains**:
- Natural Language Processing
- Software Engineering

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/ineffablekenobi/Documentation-generation-using-LLMtool)

## 🎯 Purpose and Intended Users

**Goal**: To develop a tailored dataset for automated and context-aware Javadoc generation using publicly available Large Language Models.

**Target Audience**:
- ML Researchers
- Software Engineers
- Model Developers

**Tasks**:
- Code Documentation Generation

**Limitations**: Resource constraints limited dataset size and diversity; potential model biases from the training data.

## 💾 Data

**Source**: Curated from multiple public codebases with a focus on Java and Javadoc templates.

**Size**: 3,614 code-Javadoc pairs

**Format**: JSON

**Annotation**: Manual verification and automated filtering to ensure data quality.

## 🔬 Methodology

**Methods**:
- Fine-tuning
- Evaluation using BLEU and ROUGE scores

**Metrics**:
- BLEU Score
- ROUGE-1
- ROUGE-2
- ROUGE-L
- ROUGE-Lsum

**Calculation**: Metrics are calculated based on n-gram overlap and longest common subsequence matching.

**Interpretation**: Higher scores indicate better alignment with reference documentation.

**Validation**: Models evaluated via zero-shot, few-shot, and fine-tuned settings showing performance improvements.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt leaking

**Demographic Analysis**: N/A

**Potential Harm**: Potential for generated documentation to be factually incorrect or misleading.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset is built using only public repositories with permissive licenses to protect privacy.

**Data Licensing**: MIT License, CC-BY 4.0 License upon acceptance.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
