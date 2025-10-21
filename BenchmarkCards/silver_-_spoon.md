# SILVER - SPOON

## 📊 Benchmark Details

**Name**: SILVER - SPOON

**Overview**: SILVER - SPOON is a dataset consisting of 12,000 samples designed to investigate the presence of socioeconomic bias in large language models through three subsets: normative judgement evaluation, demographic driven profession prediction, and contextual narrative bias analysis.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/SILVER-SPOON)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the presence of implicit and explicit socioeconomic bias in large language models and to provide a dataset for future research.

**Target Audience**:
- ML Researchers
- Social Scientists
- Ethics Researchers

**Tasks**:
- Normative Judgement Evaluation
- Profession Prediction
- Narrative Bias Analysis

**Limitations**: N/A

## 💾 Data

**Source**: The dataset contains scenarios generated through a combination of prompting and text augmentation techniques, focused on ethical dilemmas faced by socioeconomically underprivileged people.

**Size**: 12,000 samples

**Format**: CSV

**Annotation**: Annotated by individuals from both ends of the socioeconomic spectrum, employing a dual-labeling scheme.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Cohen’s Kappa score
- Jaccard Similarity
- Dice Similarity Coefficient
- Matthews Correlation Coefficient
- Per class Accuracy

**Calculation**: Metrics are calculated based on the agreement between model responses and the gold labels generated via majority voting among trained annotators.

**Interpretation**: A higher score indicates better agreement between the model's predictions and the expected outcomes.

**Validation**: Through extensive qualitative analysis and human evaluation of model responses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
