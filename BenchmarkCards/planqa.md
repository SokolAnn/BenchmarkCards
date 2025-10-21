# PlanQA

## 📊 Benchmark Details

**Name**: PlanQA

**Overview**: PlanQA is a diagnostic benchmark for evaluating geometric and spatial reasoning in large-language models using structured representations of indoor scenes. It includes a dataset of 1,800 structured 2D layouts with 18,000 diverse questions to test various reasoning abilities.

**Data Type**: structured 2D layouts paired with natural language questions

**Domains**:
- Natural Language Processing
- Architecture
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- CLEVR
- SpatialSense
- BabyAI
- ALFRED
- Room-to-Room

**Resources**:
- [Resource](https://OldDelorean.github.io/PlanQA/arXiv:2507.07644v1)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for measuring spatial reasoning capabilities of language models in structured environments.

**Target Audience**:
- ML Researchers
- Model Developers
- Architects

**Tasks**:
- Spatial Reasoning
- Geometry Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic generation using Gemini 2.5 Pro.

**Size**: 1,800 layouts, 18,000 questions

**Format**: JSON

**Annotation**: Questions generated based on structured layout parameters.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Accuracy is calculated based on relative error for numeric outputs and exact match for boolean outputs.

**Interpretation**: Accuracy metrics are employed to gauge reasoning performance, with varying thresholds for question types.

**Validation**: Models were evaluated in zero-shot conditions to ascertain the reasoned outputs based on structured input.

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
