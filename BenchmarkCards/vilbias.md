# ViLBias

## 📊 Benchmark Details

**Name**: ViLBias

**Overview**: ViLBias is a VQA-style benchmark and framework for detecting and reasoning about bias in multimodal news, comprising 40,945 text-image pairs from diverse outlets, each annotated with a bias label and concise rationale using a hybrid LLM-as-annotator pipeline.

**Data Type**: text-image pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BiasLab
- BIASsist
- MDAM3
- MMFakeBench
- IndiTag
- VERITE
- MBIB
- BABE
- BASIL
- NewsBag
- FakeNewsNet

**Resources**:
- [Resource](https://arxiv.org/abs/2412.17052)

## 🎯 Purpose and Intended Users

**Goal**: The main goal is to assess the ability of language models, specifically vision-language models (VLMs), to detect and reason about media bias.

**Target Audience**:
- ML Researchers
- Media Analysts
- Model Developers

**Tasks**:
- Bias Detection
- Visual Question Answering

**Limitations**: The dataset coverage skews towards English-language and Western media, limiting cross-cultural generalizability.

## 💾 Data

**Source**: 40,945 text-image pairs collected from diverse news sources including CNN, BBC, and The New York Times.

**Size**: 40,945 examples

**Format**: JSON

**Annotation**: Combines LLM-based automated labeling with extensive human review for quality assurance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- LLM-as-judge evaluation

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated using standard evaluation protocols across multiple model evaluations.

**Interpretation**: Higher accuracy indicates better bias detection, while reasoning quality is assessed by faithfulness to the evidence.

**Baseline Results**: RoBERTa+CLIP achieved F1 of 82.9% and accuracy of 83.6%.

**Validation**: 5-fold cross-validation and human review ensure reliability of annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: The dataset lacks comprehensive coverage of diverse demographic groups.

**Potential Harm**: ['Reinforcement of existing societal biases through biased media representations']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
