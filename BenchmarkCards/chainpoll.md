# ChainPoll

## 📊 Benchmark Details

**Name**: ChainPoll

**Overview**: ChainPoll is a novel hallucination detection methodology that substantially outperforms existing alternatives and is evaluated using the RealHall benchmark suite.

**Data Type**: text

**Domains**:
- open-domain
- closed-domain

## 🎯 Purpose and Intended Users

**Goal**: To provide a reliable method for detecting hallucinations in large language model outputs.

**Target Audience**:
- researchers
- developers
- practitioners in NLP

**Tasks**:
- evaluation of hallucination detection metrics
- measurement of LLM performance

**Limitations**: N/A

## 💾 Data

**Source**: RealHall benchmark suite

**Size**: four benchmark datasets

**Format**: text-based prompt and completion

**Annotation**: Boolean labels indicating the presence of hallucinations

## 🔬 Methodology

**Methods**:
- ChainPoll-Correctness
- ChainPoll-Adherence

**Metrics**:
- AUROC

**Calculation**: Aggregate AUROC scores calculated from benchmark datasets.

**Interpretation**: Higher AUROC indicates better performance in detecting hallucinations.

**Validation**: Head-to-head comparisons against other existing metrics (e.g., SelfCheckGPT, TRUE, G-Eval) were performed.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy
- Explainability

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Exposing personal information
- **Explainability**: Unexplainable output

**Demographic Analysis**: N/A

**Potential Harm**: Potential for misleading outputs due to hallucinations in model responses.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personally identifiable information is used in the training data or evaluation.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
