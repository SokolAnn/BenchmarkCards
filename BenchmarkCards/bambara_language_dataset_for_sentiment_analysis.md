# Bambara Language Dataset for Sentiment Analysis

## 📊 Benchmark Details

**Name**: Bambara Language Dataset for Sentiment Analysis

**Overview**: We present the first common-crawl-based Bambara dialectal dataset dedicated for Sentiment Analysis, available freely for Natural Language Processing research purposes.

**Data Type**: sentiment analysis sentences

**Domains**:
- Natural Language Processing

**Languages**:
- Bambara

**Resources**:
- [GitHub Repository](https://github.com/chaymafourati/BAMBARA-LANGUAGE-DATASET-FOR-SENTIMENT-ANALYSIS)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to provide a dataset for sentiment analysis in the Bambara language and to support further research activities in African languages.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Sentiment Analysis

**Limitations**: The dataset is not balanced, including a majority of positive sentences compared to negative and neutral ones.

## 💾 Data

**Source**: Common-crawl-based dataset collected and manually annotated by two Malian native speakers.

**Size**: 3,046 sentences

**Format**: N/A

**Annotation**: Sentiment annotation was processed manually by native speakers, with sentences annotated as positive (1), negative (-1), or neutral (0).

## 🔬 Methodology

**Methods**:
- Support Vector Machine
- Random Forest Classifier
- Gradient Boosting Classifier
- Logistic Regression
- Ridge Classifier
- Long Short-Term Memory (LSTM)
- Bidirectional Long Short-Term Memory (Bi-LSTM)

**Metrics**:
- Accuracy
- F1 Micro
- F1 Macro
- Recall
- Precision

**Calculation**: Metrics are calculated based on the performance of different models applied to the dataset.

**Interpretation**: Good performance is indicated by higher values of accuracy and F1 scores; SVM was found to perform best overall.

**Baseline Results**: SVM achieved 73% accuracy on Bambara V1 dataset and 71% accuracy on Bambara V2 dataset.

**Validation**: The datasets were split to form train and test datasets in specific ratios (80:20 for ML, 90:10 for DL).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
