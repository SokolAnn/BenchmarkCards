# ArrangementPuzzle

## 📊 Benchmark Details

**Name**: ArrangementPuzzle

**Overview**: ArrangementPuzzle is a novel puzzle dataset designed to analyze the internal representations of reasoning in large language models (LLMs). It allows for automated stepwise correctness verification and is used for training a classifier model on LLM activations to assess reasoning correctness.

**Data Type**: structured puzzle statements

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Solid-Energy-Systems/arrangement_puzzle)
- [GitHub Repository](https://github.com/Solid-Energy-Systems/activation_classifier)

## 🎯 Purpose and Intended Users

**Goal**: To investigate LLM internal representations of reasoning and provide insights into their reasoning mechanisms.

**Target Audience**:
- ML Researchers
- AI Developers

**Tasks**:
- Reasoning Analysis

**Limitations**: While our study provides insights into the internal representations of reasoning in large language models (LLMs), it has several limitations, including the restricted nature of the dataset and its applicability to real-world reasoning tasks.

## 💾 Data

**Source**: Custom constructed dataset of puzzles designed for testing LLM reasoning.

**Size**: 10,000 prompts

**Format**: N/A

**Annotation**: Manually annotated based on LLM outputs compared to ground-truth solutions.

## 🔬 Methodology

**Methods**:
- Classifier training
- Automated correctness verification

**Metrics**:
- Accuracy

**Calculation**: The classifier predicts whether a reasoning step is accurate based on activations from LLMs.

**Interpretation**: An accuracy above 80% indicates effective differentiation between correct and incorrect reasoning steps.

**Baseline Results**: N/A

**Validation**: Evaluation was conducted on 1141 withheld test puzzles.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
