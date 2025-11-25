# RUIE-Bench (Robust Universal Information Extraction Benchmark)

## 📊 Benchmark Details

**Name**: RUIE-Bench (Robust Universal Information Extraction Benchmark)

**Overview**: RUIE-Bench is a benchmark dataset designed to evaluate the robustness of Universal Information Extraction (UIE) models. It includes 14 adversarial perturbations for three core IE tasks: Named Entity Recognition (NER), Relation Extraction (RE), and Event Detection (ED).

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RockNER

**Resources**:
- [Resource](https://arxiv.org/abs/2503.03201)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating the robustness of UIE models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Named Entity Recognition
- Relation Extraction
- Event Detection

**Limitations**: Generating more realistic perturbations remains an exploratory direction.

## 💾 Data

**Source**: Generated using Large Language Models (LLMs) and verified for annotation accuracy.

**Size**: 11,580 examples

**Format**: JSON

**Annotation**: Manually verified for accuracy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Micro F1 Score

**Calculation**: Micro F1 Score is computed based on entity, relation, and event trigger predictions against ground truth annotations.

**Interpretation**: Higher Micro F1 Score indicates better performance on the robustness of UIE tasks.

**Baseline Results**: Comparative analysis against 8 open-source LLMs, 4 closed-source LLMs, 4 traditional IE models, and 4 fine-tuned UIE models.

**Validation**: The benchmark is validated by comprehensive evaluation across various perturbations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
