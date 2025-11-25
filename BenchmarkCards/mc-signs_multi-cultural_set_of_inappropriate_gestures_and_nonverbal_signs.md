# MC-SIGNS (Multi-Cultural Set of Inappropriate Gestures and Nonverbal Signs)

## 📊 Benchmark Details

**Name**: MC-SIGNS (Multi-Cultural Set of Inappropriate Gestures and Nonverbal Signs)

**Overview**: MC-SIGNS is a dataset of 288 gesture-country pairs annotated for offensiveness, cultural significance, and contextual factors across 25 gestures and 85 countries, aimed at evaluating and improving AI systems’ cultural safety.

**Data Type**: gesture-country pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Akhila-Yerukola/culturally-offensive-gestures)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate AI systems’ cultural awareness and improve their handling of inappropriate gestures in diverse cultural contexts.

**Target Audience**:
- ML Researchers
- AI Developers
- Cultural Studies Researchers

**Tasks**:
- Cultural Sensitivity Evaluation
- Offensiveness Detection

**Limitations**: Limited to 25 gestures, does not comprehensively cover all gestures used globally.

## 💾 Data

**Source**: Curated from various sources including online databases, cultural guides, and annotations from cultural experts.

**Size**: 288 gesture-country pairs

**Format**: JSON

**Annotation**: Annotations provided by cultural experts from respective regions on offensiveness and cultural significance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Recall
- Specificity

**Calculation**: Metrics are calculated based on the correct identification of offensive and non-offensive gestures.

**Interpretation**: High accuracy indicates effective cultural awareness in AI systems; low accuracy indicates the need for improved sensitivity.

**Validation**: Dataset validation involves human annotations and comparison against predefined thresholds for gesture offensiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Cultural Sensitivity

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Potential Harm**: ['Gender-based harassment', 'Discriminatory content']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All annotators provided informed consent, and only essential demographic information was collected.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent obtained from all annotators.

**Compliance With Regulations**: Study supervised by an Institutional Review Board (IRB).
