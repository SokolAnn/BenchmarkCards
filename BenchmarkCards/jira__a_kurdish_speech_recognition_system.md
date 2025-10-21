# Jira: a Kurdish Speech Recognition System

## 📊 Benchmark Details

**Name**: Jira: a Kurdish Speech Recognition System

**Overview**: This paper introduces the first large vocabulary speech recognition system (LVSR) for the Central Kurdish language, named Jira. It includes the creation of a speech corpus and pronunciation lexicon for Kurdish, designed to address the lack of speech and text resources for the language.

**Data Type**: speech recordings

**Domains**:
- Natural Language Processing

**Languages**:
- Kurdish

**Similar Benchmarks**:
- N/A

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To develop and evaluate the first speech recognition system for Central Kurdish, including a speech corpus and pronunciation lexicon.

**Target Audience**:
- Speech Technology Researchers
- Linguists
- Developers of Language Resources

**Tasks**:
- Speech Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Speech corpus collected from 576 speakers in various environments including controlled offices and crowdsourcing via Telegram.

**Size**: 43.68 hours of speech

**Format**: WAV

**Annotation**: Manual processing to discard noisy and corrupted samples

## 🔬 Methodology

**Methods**:
- Evaluation of speech recognition accuracy using different acoustic models
- Kaldi toolkit for system setup

**Metrics**:
- Word Error Rate (WER)
- Phoneme Error Rate (PER)

**Calculation**: WER and PER are calculated based on the recognition performance on test sets.

**Interpretation**: Lower WER and PER values indicate better performance in speech recognition accuracy.

**Baseline Results**: The best performance achieved was 13.9% WER and 4.9% for general topic.

**Validation**: Evaluated using separate test sets for different environments and domains.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: Balanced representation of speakers from different genders and education backgrounds.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
