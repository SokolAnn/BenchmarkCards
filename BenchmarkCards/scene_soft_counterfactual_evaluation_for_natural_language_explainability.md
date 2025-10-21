# SCENE (Soft Counterfactual Evaluation for Natural language Explainability)

## 📊 Benchmark Details

**Name**: SCENE (Soft Counterfactual Evaluation for Natural language Explainability)

**Overview**: SCENE is a novel evaluation method that leverages large language models (LLMs) to generate Soft Counterfactual explanations in a zero-shot manner, focusing on token-based substitutions to create contextually appropriate and semantically meaningful explanations for explainable AI (XAI) techniques in natural language processing tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/HaoranZhengRaul/SCENE.git)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized framework for evaluating the effectiveness of explainable AI techniques in identifying significant tokens in sentiment analysis tasks through the use of Soft Counterfactuals.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Text Classification
- Sentiment Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Stanford Sentiment Treebank (SST2)

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Model-based evaluation
- Human evaluation

**Metrics**:
- Validitysoft
- Csoft
- Mean Average Precision (MAP)
- Infidelity

**Calculation**: Metrics are calculated based on the changes in model output probabilities when using Soft Counterfactuals compared to original inputs.

**Interpretation**: Higher scores indicate better identification of significant tokens in relation to model behavior.

**Baseline Results**: N/A

**Validation**: The effectiveness of the evaluation metrics was validated through empirical results across various model architectures (CNN, RNN, and Transformer).

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
