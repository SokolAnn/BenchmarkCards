# Benchmark of Expert-edited Machine-generated Outputs (Beemo)

## 📊 Benchmark Details

**Name**: Benchmark of Expert-edited Machine-generated Outputs (Beemo)

**Overview**: Beemo includes 19.6k texts, composed of 6.5k human-written texts and 13.1k machine-generated & LLM-edited texts, designed for evaluating machine-generated text detection in various scenarios.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MAGE
- AIGC MPU
- RADAR

**Resources**:
- [Resource](https://huggingface.co/datasets/toloka/beemo)
- [GitHub Repository](https://github.com/Toloka/beemo)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating the detection of machine-generated texts, particularly those that have been edited by experts or LLMs.

**Target Audience**:
- ML Researchers
- Model Developers
- AI Safety Experts

**Tasks**:
- Text Classification
- Machine Generated Text Detection

**Limitations**: N/A

## 💾 Data

**Source**: The dataset comprises texts collected and edited from a variety of instruction-finetuned LLMs and human-written content as prompts.

**Size**: 19,683 texts

**Format**: N/A

**Annotation**: Expert annotators edited the machine-generated texts based on guidelines for accuracy, coherence, and fluency.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Area Under ROC Curve (AUC-ROC)

**Calculation**: AUROC scores are calculated based on the probability that a detector assigns higher scores to a randomly selected machine-generated text than to a randomly selected human-written text.

**Interpretation**: Higher AUROC values indicate better performance of the machine-generated text detectors.

**Validation**: The benchmark has been evaluated using 33 different configurations of MGT detectors.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset does not contain identifiable personal information and uses anonymized expert responses.

**Data Licensing**: Materials are released under MIT and CC-BY-NC-4.0 licenses, depending on the source.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
