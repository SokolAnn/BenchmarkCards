# SafeDialBench

## 📊 Benchmark Details

**Name**: SafeDialBench

**Overview**: SafeDialBench is a fine-grained benchmark for evaluating the safety of Large Language Models (LLMs) in multi-turn dialogues across diverse jailbreak attacks. It incorporates a two-tier hierarchical safety taxonomy covering six dimensions and generates over 4,000 dialogues in both Chinese and English under various scenarios.

**Data Type**: multi-turn dialogues

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- COLD
- BeaverTails
- SafetyBench
- CoSafe

**Resources**:
- [GitHub Repository](https://github.com/drivetosouth/SafeDialBench-Dataset)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of SafeDialBench is to provide a comprehensive evaluation benchmark that rigorously assesses the safety of LLMs in real-world dialogue settings faced with jailbreak attacks.

**Target Audience**:
- ML Researchers
- Model Developers
- Safety Evaluators

**Tasks**:
- Safety Assessment
- Ethical Compliance Evaluation

**Limitations**: SafeDialBench requires incorporation of additional jailbreak attack methods and continuous updates to keep pace with rapid model developments.

## 💾 Data

**Source**: Constructed through LLM interactions combined with manual verification across 22 dialogue scenarios.

**Size**: 4,053 dialogues

**Format**: JSON

**Annotation**: Manual verification by annotators engaging in chats with LLMs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Evaluation scores are calculated based on LLM responses assessed by human experts across various safety dimensions.

**Interpretation**: Higher scores indicate better model performance in identifying, handling unsafe content, and consistency in responses.

**Validation**: Extensive experiments conducted on 17 LLMs with human expert evaluations to validate model safety performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Ethics
- Legal Compliance

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Privacy**: Exposing personal information
- **Robustness**: Prompt injection attack

**Demographic Analysis**: The benchmark includes demographic considerations in its evaluation framework.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset has implemented rigorous ethical protocols including informed consent and fair compensation for annotators.

**Data Licensing**: The dataset is strictly intended for academic research purposes only.

**Consent Procedures**: Informed consent was obtained from participants involved in the dataset creation.

**Compliance With Regulations**: Not Applicable
