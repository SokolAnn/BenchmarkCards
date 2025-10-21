# MIntRec2.0 (Multimodal Intent Recognition 2.0)

## 📊 Benchmark Details

**Name**: MIntRec2.0 (Multimodal Intent Recognition 2.0)

**Overview**: MIntRec2.0 is a large-scale benchmark dataset for multimodal intent recognition in multi-party conversations, incorporating 1,245 dialogues and 15,040 multimodal samples with a new intent taxonomy of 30 fine-grained classes.

**Data Type**: text, video, audio

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/thuiar/MIntRec2.0)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive resource for multimodal intent recognition and out-of-scope detection, thereby advancing research in human-machine conversational interactions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Domain Experts

**Tasks**:
- Intent Recognition
- Out-of-Scope Detection

**Limitations**: N/A

## 💾 Data

**Source**: Collected from TV series (Superstore, The Big Bang Theory, Friends)

**Size**: 15,040 samples

**Format**: N/A

**Annotation**: Annotated by six trained students with a majority voting system.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Recall
- Precision

**Calculation**: Metrics are calculated based on true positive, false positive, and false negatives for both in-scope and out-of-scope classes.

**Interpretation**: Higher scores indicate better model performance regarding intent recognition and out-of-scope detection.

**Baseline Results**: MAG-BERT achieved an accuracy of 71% with 7% of training data.

**Validation**: Data split into training, validation, and test sets at a ratio of approximately 7:1:2.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data consists of dialogues from TV shows with no personal identifiers.

**Data Licensing**: CC BY-NC-SA 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
