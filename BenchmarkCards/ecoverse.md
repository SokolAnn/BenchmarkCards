# EcoVerse

## 📊 Benchmark Details

**Name**: EcoVerse

**Overview**: EcoVerse is an annotated English Twitter dataset of 3,023 tweets spanning a wide spectrum of environmental topics, designed for Eco-Relevance Classification, Environmental Impact Analysis, and Stance Detection.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/GioSira/EcoVerse.git)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the EcoVerse dataset is to provide a resource for analyzing various environmental topics through Eco-Relevance classification, Environmental Impact analysis, and Stance detection.

**Target Audience**:
- ML Researchers
- Environmental Scientists
- Domain Experts

**Tasks**:
- Eco-Relevance Classification
- Environmental Impact Analysis
- Stance Detection

**Limitations**: N/A

## 💾 Data

**Source**: Annotated tweets collected from Twitter using specific hashtags and keywords related to environmental topics.

**Size**: 3,023 tweets

**Format**: JSON

**Annotation**: Manual annotation by trained annotators with expertise in environmental topics.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall

**Calculation**: Metrics were evaluated using Scikit-learn’s implementation, with an emphasis on Accuracy for multi-class settings.

**Interpretation**: Higher scores in Accuracy and F1 indicate better model performance in identifying eco-relevant tweets, their environmental impact, and associated stances.

**Baseline Results**: BERT and RoBERTa were fine-tuned as baseline models with the best performing models being DistilRoBERTa and ClimateBERT for eco-relevance and environmental impact tasks.

**Validation**: Inter-Annotator Agreement (IAA) was measured and improved after discussions, ensuring the reliability of annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Misinterpretation of tweets due to contextual nuance, especially for neutral stances.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Privacy measures discussed include an awareness of carbon emissions associated with the dataset’s use and training of models.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
