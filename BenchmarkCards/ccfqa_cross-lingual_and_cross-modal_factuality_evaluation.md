# CCFQA (Cross-lingual and Cross-modal Factuality Evaluation)

## 📊 Benchmark Details

**Name**: CCFQA (Cross-lingual and Cross-modal Factuality Evaluation)

**Overview**: CCFQA is a benchmark that contains parallel speech-text factual questions across 8 languages, designed to systematically evaluate MLLMs’ cross-lingual and cross-modal factuality capabilities.

**Data Type**: parallel speech-text question pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Mandarin Chinese
- English
- French
- Japanese
- Korean
- Russian
- Spanish
- Yue Chinese

**Similar Benchmarks**:
- TruthfulQA
- HaluEval
- SimpleQA
- Chinese SimpleQA
- KoLasSimpleQA
- SD-QA
- CompA
- VoiceBench
- SpeechIQ

**Resources**:
- [GitHub Repository](https://github.com/yxduir/ccfqa)

## 🎯 Purpose and Intended Users

**Goal**: To provide a foundational research resource to promote the development of MLLMs with more robust and reliable speech understanding capabilities.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering
- Cross-lingual Question Answering
- Multilingual Spoken Question Answering
- Cross-lingual Spoken Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Collected from existing QA datasets and manually curated.

**Size**: 14,400 question-answer pairs

**Format**: JSON

**Annotation**: Manual curation and professional translation into target languages.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: Metrics are calculated based on the consistency of model responses to the same question across different languages and modalities.

**Interpretation**: Higher F1 scores indicate better consistency in factual responses across languages and modalities.

**Baseline Results**: N/A

**Validation**: The benchmark was validated through systematic evaluation of existing MLLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All volunteers have signed a Voice Authorization License Agreement for the use of recorded speech.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Data usage complies with applicable privacy and data protection regulations.
