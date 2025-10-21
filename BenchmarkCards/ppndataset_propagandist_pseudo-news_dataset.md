# PPNdataset (Propagandist Pseudo-News dataset)

## 📊 Benchmark Details

**Name**: PPNdataset (Propagandist Pseudo-News dataset)

**Overview**: The PPNdataset is a multisource, multilingual, multimodal dataset composed of news articles extracted from websites identified as propaganda sources. It is created to investigate the stylistic features of propaganda and to compare human annotations with machine classification.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic
- Chinese
- English
- French
- German
- Italian
- Russian
- Spanish
- Ukrainian

**Resources**:
- [GitHub Repository](https://github.com/hybrinfox/ppn)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for analyzing the language of propaganda and to facilitate the training of machine learning models for propaganda detection.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Text Classification

**Limitations**: Annotation experiments were only run on a subset of the French data. There may be parsing errors for some languages, and further analysis from native speakers of other languages may be required before using these parts of the dataset.

## 💾 Data

**Source**: News articles extracted from propaganda sources identified by expert agencies.

**Size**: 27,079 articles

**Format**: N/A

**Annotation**: Multilabel annotation by humans using 11 distinct labels.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics were calculated based on the performance of models on the test set after training.

**Interpretation**: A model is considered good if it achieves high accuracy in detecting propaganda articles compared to regular articles.

**Baseline Results**: Test accuracies for models ranged from 0.921 (XGBoost) to 0.997 (RoBERTa) for propaganda detection.

**Validation**: Validation was performed by splitting the datasets into training, validation, and test sets, ensuring no overlap.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset includes articles in multiple languages, allowing for demographic analysis across different language groups.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Participants in the annotation task were given content warnings and the option to withdraw at any time.

**Data Licensing**: Not Applicable

**Consent Procedures**: All annotators performed the task voluntarily.

**Compliance With Regulations**: Not Applicable
