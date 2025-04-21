# MoCa: Measuring Human-Language Model Alignment on Causal and Moral Judgment Tasks

## 📊 Benchmark Details

**Name**: MoCa: Measuring Human-Language Model Alignment on Causal and Moral Judgment Tasks

**Overview**: The study investigates the alignment between human causal and moral judgments and those made by large language models (LLMs). It uses a dataset collected from cognitive science literature to evaluate how well LLMs emulate human reasoning in scenarios involving causal and moral judgment.

**Data Type**: text

**Domains**:
- cognitive science
- natural language processing
- ethics

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/cicl-stanford/moca)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and understand the alignment of language models with human intuitions regarding causal and moral judgments.

**Target Audience**:
- researchers in the fields of AI and ethics
- cognitive scientists
- developers of language models

**Tasks**:
- evaluate LLM performance on causal and moral judgment tasks
- identify implicit tendencies in model judgments

**Limitations**: None

## 💾 Data

**Source**: Existing literature in cognitive science

**Size**: 5150 human responses

**Format**: text stories with annotation

**Annotation**: Expert annotation on latent factors influencing judgments

## 🔬 Methodology

**Methods**:
- statistical analysis of LLM responses
- conjoint analysis
- zero-shot learning

**Metrics**:
- Average Marginal Component Effect (AMCE)
- agreement accuracy
- area under the curve (AUC)
- mean absolute error (MAE)
- cross-entropy (CE)

**Calculation**: Calculated using probabilities assigned to responses by LLMs compared to human judgments.

**Interpretation**: The results indicate the degree to which LLMs align with human moral and causal judgments.

**Validation**: Results validated through comparison against human responses and evaluation of annotation agreement.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Transparency
- Explainability

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency
- **Explainability**: Unexplainable output

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personal data was collected from participants.

**Data Licensing**: The dataset is under a Creative Commons license (CC BY 4.0).

**Consent Procedures**: Participants were provided with consent forms at the beginning of the study.

**Compliance With Regulations**: The study received IRB approval for ethical compliance.
