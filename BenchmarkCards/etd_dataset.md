# ETD Dataset

## 📊 Benchmark Details

**Name**: ETD Dataset

**Overview**: The ETD dataset is specifically designed for training and evaluating end-turn detection models, consisting of synthetic and real conversational data to better understand speech heuristics in human dialogue.

**Data Type**: audio

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a public dataset for training and evaluating end-turn detection in spoken dialogue systems.

**Target Audience**:
- ML Researchers
- Speech Processing Practitioners

**Tasks**:
- End-Turn Detection

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic data generated from text dialogues and real speech collected from YouTube and Buckeye speech corpus.

**Size**: 120,000 samples, over 300 hours of conversational data

**Format**: N/A

**Annotation**: Annotations are based on a ternary classification of the speech segments (Speaking Unit, Gap, Pause).

## 🔬 Methodology

**Methods**:
- Binary classification
- Real-time audio segmentation

**Metrics**:
- Precision
- Recall
- F1 Score
- Accuracy

**Calculation**: Metrics are calculated based on the performance of models evaluated on the ETD dataset.

**Interpretation**: Higher values of precision, recall, and F1 score indicate better performance in correctly identifying end-turns in the conversation.

**Baseline Results**: GRU model achieved an accuracy of 79.34%, while Wav2vec 2.0 achieved 99.49% on binary classification.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
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
