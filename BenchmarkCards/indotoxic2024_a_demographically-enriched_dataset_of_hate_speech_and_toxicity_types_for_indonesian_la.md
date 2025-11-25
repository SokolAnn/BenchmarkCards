# IndoToxic2024 (A Demographically-Enriched Dataset of Hate Speech and Toxicity Types for Indonesian Language)

## 📊 Benchmark Details

**Name**: IndoToxic2024 (A Demographically-Enriched Dataset of Hate Speech and Toxicity Types for Indonesian Language)

**Overview**: IndoToxic2024 is a comprehensive Indonesian hate speech and toxicity classification dataset comprising 43,692 entries annotated by 19 diverse individuals. It focuses on texts targeting vulnerable groups in Indonesia, particularly during the 2024 presidential election.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Indonesian

**Resources**:
- [GitHub Repository](https://github.com/izzako/IndoToxic2024/tree/main)

## 🎯 Purpose and Intended Users

**Goal**: To enable the creation of better hate speech detection systems specifically for the Indonesian language.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Hate Speech Detection
- Toxicity Classification

**Limitations**: N/A

## 💾 Data

**Source**: Collected from social media platforms including Facebook, Instagram, and Twitter, as well as articles from CekFakta.

**Size**: 43,692 examples

**Format**: N/A

**Annotation**: Annotated by 19 diverse individuals with ten-dimensional demographic information.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Macro F1 score calculated across various classification tasks.

**Interpretation**: A macro F1 score above 0.7 indicates good performance in hate speech detection tasks.

**Baseline Results**: Achieved a macro F1 score of 0.78 with IndoBERTweet fine-tuned for hate speech classification.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset and the annotation process incorporates demographic information to assess the biases in hate speech detection.

**Potential Harm**: The creation of the dataset could inadvertently lead to models generating or amplifying hate speech.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Annotators were warned and asked for consent. They had the option to quit if they felt unable to continue.

**Data Licensing**: Not Applicable

**Consent Procedures**: Annotators were compensated and warned of potential harm.

**Compliance With Regulations**: Not Applicable
