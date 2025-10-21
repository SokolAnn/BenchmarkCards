# Cross-Lingual Transfer from Related Languages: Treating Low-Resource Maltese as Multilingual Code-Switching

## 📊 Benchmark Details

**Name**: Cross-Lingual Transfer from Related Languages: Treating Low-Resource Maltese as Multilingual Code-Switching

**Overview**: We present a novel dataset annotated with word-level etymology to improve cross-lingual transfer capabilities for Maltese, a language influenced by Arabic, Italian, and English.

**Data Type**: word-level etymology annotations

**Domains**:
- Natural Language Processing

**Languages**:
- Maltese
- Arabic
- Italian
- English

**Resources**:
- [GitHub Repository](https://github.com/MLRS/malti/tree/2024.eacl3)

## 🎯 Purpose and Intended Users

**Goal**: To improve the cross-lingual transfer capabilities of Maltese by selectively applying transliteration and translation based on word etymology.

**Target Audience**:
- ML Researchers
- Language Model Developers
- Linguists

**Tasks**:
- Part-of-Speech tagging
- Dependency Parsing
- Named Entity Recognition
- Sentiment Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Annotated dataset extracted from the Maltese Universal Dependencies Treebank consisting of 439 sentences and 9,683 tokens.

**Size**: 9,683 tokens

**Format**: JSON

**Annotation**: Annotated by experts with etymological tags based on language origin (Arabic, Non-Arabic, Mixed).

## 🔬 Methodology

**Methods**:
- Automated metrics
- Fine-tuning language models

**Metrics**:
- Accuracy
- Labelled Attachment Score (LAS)
- F1 Score

**Calculation**: Performance evaluated using fine-tuning on language models and measuring accuracy and F1 scores on downstream tasks.

**Interpretation**: Higher accuracy indicates better language model performance on specified NLP tasks using the newly annotated dataset.

**Baseline Results**: BERTu achieved a top-line accuracy of 98.3% on POS tagging.

**Validation**: Cross-validation was performed using 10 folds to evaluate the reliability of the classifier.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
