# CROW (Commonsense Reasoning in Real-World Tasks)

## 📊 Benchmark Details

**Name**: CROW (Commonsense Reasoning in Real-World Tasks)

**Overview**: CROW is a manually-curated, multi-task benchmark that evaluates the ability of models to apply commonsense reasoning in the context of six real-world NLP tasks, using a multi-stage data collection pipeline that rewrites examples from existing datasets using commonsense-violating perturbations.

**Data Type**: context-target pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/mismayil/crow)

## 🎯 Purpose and Intended Users

**Goal**: To assess the ability of NLP systems to apply commonsense reasoning in real-world tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Machine Translation
- Open-domain Dialogue
- Dialogue Summarization
- Intent Detection
- Stance Classification
- Safety Detection

**Limitations**: Commonsense knowledge has many dimensions, and only six core ones are considered.

## 💾 Data

**Source**: Constructed using existing datasets for six real-world NLP tasks.

**Size**: 16,541 examples

**Format**: N/A

**Annotation**: Crowdsourced with validation by multiple annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Macro-F1
- Situational Accuracy

**Calculation**: Macro-F1 is calculated as the average of scores across all tasks, while Situational Accuracy considers the correctness of responses across all targets for each context.

**Interpretation**: Higher scores indicate better performance of the models on commonsense reasoning tasks.

**Baseline Results**: Human performance over various tasks serves as a baseline.

**Validation**: Each stage of data collection included validation by multiple workers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
