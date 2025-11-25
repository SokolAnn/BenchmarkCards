# MMLA (Multimodal Language Analysis)

## 📊 Benchmark Details

**Name**: MMLA (Multimodal Language Analysis)

**Overview**: MMLA is a comprehensive benchmark designed for multimodal language analysis, covering six core dimensions (intent, emotion, dialogue act, sentiment, speaking style, and communication behavior) with over 61K multimodal utterances.

**Data Type**: multimodal utterances

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Mandarin

**Resources**:
- [GitHub Repository](https://github.com/thuiar/MMLA)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate foundation models in multimodal language analysis and highlight challenges and insights for future research.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Intent Recognition
- Emotion Recognition
- Dialogue Act Classification
- Sentiment Analysis
- Speaking Style Detection
- Communication Behavior Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Collected from nine publicly available multimodal language datasets.

**Size**: 61,016 multimodal utterances totaling 76.6 hours of video

**Format**: N/A

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Zero-shot inference
- Supervised fine-tuning
- Instruction tuning

**Metrics**:
- Accuracy
- Weighted F1 Score
- Precision
- Recall

**Calculation**: Accuracy and other metrics are calculated based on the predictions against ground truth labels in the dataset.

**Interpretation**: Higher accuracy and F1 scores indicate better model performance in recognizing and understanding multimodal utterances.

**Baseline Results**: The best models achieved accuracies of below 70% on various tasks, post tuning improvements were noted.

**Validation**: Dataset quality assurance through expert annotation and majority voting

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data is released under respective licenses and strictly for academic research purposes.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
