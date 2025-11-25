# EmoMix-3L: A Code-Mixed Dataset for Bangla-English-Hindi Emotion Detection

## 📊 Benchmark Details

**Name**: EmoMix-3L: A Code-Mixed Dataset for Bangla-English-Hindi Emotion Detection

**Overview**: EmoMix-3L is a novel multi-label emotion detection dataset containing code-mixed data from three different languages (Bangla, Hindi, and English) specifically designed to address emotion detection in code-mixed texts.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Bangla
- Hindi
- English

**Resources**:
- [GitHub Repository](https://github.com/GoswamiDhiman/EmoMix-3L)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality test dataset for evaluating multi-label emotion detection models in a code-mixed environment.

**Target Audience**:
- Researchers in Natural Language Processing
- Emotion Detection Model Developers

**Tasks**:
- Emotion Detection

**Limitations**: The dataset is limited in size for training purposes, offering only 1,071 instances.

## 💾 Data

**Source**: Collected from undergraduate students fluent in Bangla, Hindi, and English who created code-mixed posts on various topics.

**Size**: 1,071 instances

**Format**: N/A

**Annotation**: Annotated by fluent speakers of Bangla, Hindi, and English in two stages to ensure high quality.

## 🔬 Methodology

**Methods**:
- Monolingual models evaluation
- Bilingual models evaluation
- Multilingual models evaluation
- Zero-shot prompting with GPT-3.5

**Metrics**:
- F1 Score

**Calculation**: F1 Scores were calculated for various models using both synthetic and natural datasets.

**Interpretation**: Higher F1 Score indicates better performance in correctly identifying emotions in code-mixed texts.

**Validation**: The dataset was validated through multiple annotation rounds to ensure agreement among annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Potential Harm**: The dataset may contain transliterated tokens and misspellings, which could challenge model accuracy.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data was collected with voluntary contributions to avoid privacy concerns.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants were informed of the data usage for research purposes.

**Compliance With Regulations**: Not Applicable
