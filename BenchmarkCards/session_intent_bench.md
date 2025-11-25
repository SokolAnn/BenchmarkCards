# SESSION INTENT BENCH

## 📊 Benchmark Details

**Name**: SESSION INTENT BENCH

**Overview**: A multimodal benchmark evaluating L(V)LMs' understanding of inter-session intention shift in E-commerce customer behavior, focusing on four subtasks relating to intention modeling.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- E-commerce

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate L(V)LMs' capability on understanding customer intention shifts in E-commerce sessions.

**Target Audience**:
- ML Researchers
- E-commerce Practitioners
- Model Developers

**Tasks**:
- Intent-Based Purchasing Likelihood Estimation
- Purchasing Likelihood Inference via Valued Attributes Regularization
- Intention Justification via Comparison
- Intention Evolution Modeling

**Limitations**: N/A

## 💾 Data

**Source**: Amazon-M2 and Amazon Review Dataset

**Size**: 1,952,177 intention entries, 1,132,145 session intention trajectories, 13,003,664 tasks

**Format**: N/A

**Annotation**: Human annotations conducted to collect ground-truth labels from a sampled subset of data.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Macro-F1 Score

**Calculation**: Metrics are calculated based on the percentage of correctly answered questions.

**Interpretation**: Accuracy indicates how well the models performed against human-annotated ground truths.

**Baseline Results**: N/A

**Validation**: Extensive experiments on over 20 L(V)LMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Membership inference attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The dataset is released under an Apache 2.0 license, allowing free use for research purposes.

**Consent Procedures**: Annotation workers are paid in compliance with local laws and agree to participate voluntarily.

**Compliance With Regulations**: Not Applicable
