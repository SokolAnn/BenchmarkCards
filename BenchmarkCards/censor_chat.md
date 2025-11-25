# CENSOR CHAT

## 📊 Benchmark Details

**Name**: CENSOR CHAT

**Overview**: CENSOR CHAT is a dialogue monitoring dataset aimed at detecting whether the dialogue session contains pornographic content, utilizing knowledge distillation of large language models for data annotation and classifier development.

**Data Type**: utterance-level and context-level dialogues

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/qiuhuachuan/CensorChat)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the detection of pornographic text in human-machine interaction dialogues and improve dialogue system safety.

**Target Audience**:
- Researchers in Natural Language Processing
- Developers of dialogue systems
- Content moderation teams

**Tasks**:
- Text Classification

**Limitations**: The dataset may contain mislabeled data due to reliance on large language models for annotation.

## 💾 Data

**Source**: Collected from real-life human-machine interactions in social media platforms.

**Size**: 126,111 examples

**Format**: JSON

**Annotation**: Annotated using knowledge distillation of four open-source large language models and updated with ChatGPT.

## 🔬 Methodology

**Methods**:
- Majority voting
- Knowledge distillation using large language models
- Self-criticism for label calibration

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Evaluated using standard metrics such as precision, recall, and F1-score calculated over the validation and test sets.

**Interpretation**: Higher precision indicates fewer false positives, while higher recall indicates fewer false negatives, particularly critical for detecting pornographic content.

**Validation**: Data was split into training, validation, and test sets ensuring no overlap.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential for misinformation due to classifier errors', 'Risk to users if inaccurate predictions lead to inappropriate interactions']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personal data was used; all data collected is from public online dialogues.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
