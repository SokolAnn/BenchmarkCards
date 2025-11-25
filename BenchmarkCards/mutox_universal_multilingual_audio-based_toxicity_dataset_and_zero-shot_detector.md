# MuTox (Universal MUltilingual Audio-based TOXicity Dataset and Zero-shot Detector)

## 📊 Benchmark Details

**Name**: MuTox (Universal MUltilingual Audio-based TOXicity Dataset and Zero-shot Detector)

**Overview**: MuTox is the first highly multilingual audio-based dataset with toxicity labels, comprising 20,000 audio utterances for English and Spanish, and 4,000 for the other 28 languages, designed for audio-based toxicity detection.

**Data Type**: audio utterances

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Spanish
- Arabic
- Bengali
- Bulgarian
- Catalan
- Czech
- Danish
- German
- Greek
- Estonian
- Persian
- Finnish
- French
- Hebrew
- Hindi
- Hungarian
- Indonesian
- Italian
- Dutch
- Polish
- Portuguese
- Russian
- Slovak
- Swahili
- Tagalog
- Turkish
- Urdu
- Vietnamese

**Resources**:
- [GitHub Repository](https://github.com/facebookresearch/seamless_communication/tree/mutox/src/seamless_communication/cli/toxicity/mutox)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for multilingual audio-based toxicity detection across 30 languages.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Toxicity Detection

**Limitations**: N/A

## 💾 Data

**Source**: The dataset consists of audio utterances labeled with toxicity, selected from speech transcriptions and annotated manually across multiple languages.

**Size**: 20,000 utterances for English and Spanish, 4,000 utterances for each of the other 28 languages

**Format**: Audio files

**Annotation**: Manual annotation by professional annotators

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- F1 Score
- Precision
- Recall
- Area Under the Curve (AUC)

**Calculation**: Metrics are calculated based on performance comparisons between the MuTox classifier and existing text-based classifiers.

**Interpretation**: Higher F1 Scores and AUC values indicate better performance in toxicity detection.

**Baseline Results**: MuTox improves F1-Score over wordlist-based classifiers by an average of 100%.

**Validation**: The effectiveness of the MuTox dataset and classifier was validated through performance comparisons with text-based toxicity detectors.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Decision bias
- **Robustness**: Evasion attack

**Demographic Analysis**: The dataset includes a diverse set of speakers across different languages, which may contribute to varying perceptions of toxicity.

**Potential Harm**: Potential for misclassifying non-toxic content as toxic, leading to unintended bias in the classifier's performance.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: N/A - Data collection procedures are compliant with ethical guidelines.

**Data Licensing**: Not Applicable

**Consent Procedures**: Annotators were informed of the content and could opt-out.

**Compliance With Regulations**: Not Applicable
