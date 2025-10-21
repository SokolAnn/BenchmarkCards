# WFMALL Dataset for Definition Extraction

## 📊 Benchmark Details

**Name**: WFMALL Dataset for Definition Extraction

**Overview**: The paper presents a new annotated dataset of mathematical definitions, called WFMALL, for the task of automatic definition extraction from mathematical texts.

**Data Type**: definition sentences

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/uplink007/FinalProject/tree/master/data/wolfram)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for training supervised models aimed at the extraction of mathematical definitions.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Definition Extraction

**Limitations**: N/A

## 💾 Data

**Source**: The dataset was created by collecting and processing articles from Wolfram MathWorld.

**Size**: 6,140 sentences

**Format**: Raw text files

**Annotation**: Sentences were manually labeled by annotators with at least BSc degrees in mathematics.

## 🔬 Methodology

**Methods**:
- Supervised Learning
- Deep Learning with CNN and LSTM

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics were calculated based on evaluation results of models on defined data splits.

**Interpretation**: Higher accuracy and F1 scores indicate better performance in identifying definitions.

**Baseline Results**: DefMiner and traditional models (SVM, Random Forest, etc.) were used as baselines.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
