# I am a Strange Dataset

## 📊 Benchmark Details

**Name**: I am a Strange Dataset

**Overview**: A new dataset for assessing language models' capabilities in handling metalinguistic self-reference through generation and verification tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/TristanThrush/i-am-a-strange-dataset)

## 🎯 Purpose and Intended Users

**Goal**: To assess the capacity of models to generate and understand self-referential statements and prerequisite metalinguistic reasoning.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Generation
- Text Verification

**Limitations**: The dataset challenges even the best current language models, with many performing close to chance.

## 💾 Data

**Source**: Hand-crafted by experts and validated by non-expert annotators.

**Size**: 208 examples

**Format**: N/A

**Annotation**: Handcrafted by experts and validated through agreement rates with non-expert annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Generation score
- Validation score

**Calculation**: Metrics are based on the loss assigned to continuations by the models.

**Interpretation**: Lower loss for true statements indicates correct understanding.

**Baseline Results**: GPT 4 is the only model consistently performing above chance.

**Validation**: Models judged statements as true or false through prompts designed for zero-shot and few-shot evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
