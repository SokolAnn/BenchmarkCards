# THEMISTO : JUPYTER -BASED RUNTIME BENCHMARK

## 📊 Benchmark Details

**Name**: THEMISTO : JUPYTER -BASED RUNTIME BENCHMARK

**Overview**: This benchmark consists of Jupyter notebooks development trajectories and measures how large language models (LLMs) can leverage runtime information for predicting code output and code generation.

**Data Type**: code execution trajectories

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CruxEval
- REval

**Resources**:
- [Resource](https://zenodo.org/records/14861889)

## 🎯 Purpose and Intended Users

**Goal**: To advance the field of incorporating runtime information into code language models through the evaluation of model performance on Jupyter notebook development trajectories.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Next Cell Prediction
- Cell Output Prediction

**Limitations**: The benchmark has low variability, as it is collected from only two tasks and 20 participants.

## 💾 Data

**Source**: JuNE dataset from Titov et al. (2025), involving tracking notebook development process over 8 hours.

**Size**: 1,453 code executions

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Exact Match
- ROUGE-L
- ChrF

**Calculation**: Performance is measured using exact match counts and ROUGE-L F1 scores.

**Interpretation**: Higher scores indicate better performance in predicting next code cells and outputs.

**Baseline Results**: Baseline results include various models including GPT-4o, Claude 3.5, and others.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
