# SentiQNF (Sentiment Analysis using Quantum Algorithms and Neuro-Fuzzy Systems)

## 📊 Benchmark Details

**Name**: SentiQNF (Sentiment Analysis using Quantum Algorithms and Neuro-Fuzzy Systems)

**Overview**: This study proposes a novel hybrid approach for sentiment analysis called Quantum Fuzzy Neural Network (QFNN), which leverages quantum properties and incorporates a fuzzy layer to overcome the limitations of classical sentiment analysis algorithms. It was tested on two Twitter datasets: the Coronavirus Tweets Dataset (CVTD) and the General Sentimental Tweets Dataset (GSTD), demonstrating quantifiable performance improvements.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2412.12731)

## 🎯 Purpose and Intended Users

**Goal**: To present a novel approach for sentiment detection and classification using a hybrid quantum-fuzzy model.

**Target Audience**:
- ML Researchers
- Quantum Computing Researchers
- Sentiment Analysis Practitioners

**Tasks**:
- Sentiment Analysis

**Limitations**: This research is presently restricted by the utilization of a binary dataset, thereby constraining the application of models to multi-class datasets.

## 💾 Data

**Source**: Tested on two datasets: Coronavirus Tweets Dataset (CVTD) and General Sentimental Tweets Dataset (GSTD).

**Size**: 1000 training examples, 500 testing examples

**Format**: CSV

**Annotation**: Sentiment labels were assigned as positive or negative during the preprocessing of datasets.

## 🔬 Methodology

**Methods**:
- Quantum Neural Network (QNN)
- Hybrid Quantum Neural Network (HQNN)
- Hybrid Fuzzy Neural Network (HFNN)

**Metrics**:
- Accuracy
- Recall
- Precision
- F1 Score

**Calculation**: Metrics are calculated based on the performance of the proposed models compared to classical algorithms.

**Interpretation**: Higher accuracy and lower loss indicate better performance in sentiment classification tasks.

**Baseline Results**: Classical models achieved accuracy between 73.59% and 81%. The proposed QFNN achieved 100% accuracy on CVTD.

**Validation**: The proposed models were validated using two Twitter datasets and compared against various classical machine learning models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
