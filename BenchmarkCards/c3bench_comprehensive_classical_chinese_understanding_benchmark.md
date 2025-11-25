# C3BENCH (Comprehensive Classical Chinese Understanding Benchmark)

## 📊 Benchmark Details

**Name**: C3BENCH (Comprehensive Classical Chinese Understanding Benchmark)

**Overview**: C3bench is a Comprehensive Classical Chinese understanding benchmark that comprises 50,000 text pairs for five primary Classical Chinese Understanding tasks, including classification, retrieval, named entity recognition, punctuation, and translation.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/SCUT-DLVCLab/C3bench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standard benchmark, comprehensive baselines, and valuable insights for the future advancement of LLM-based Classical Chinese Understanding research.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Classification
- Named Entity Recognition
- Retrieval
- Punctuation
- Translation

**Limitations**: The C3bench does not exhaustively cover all types of Classical Chinese understanding tasks and only evaluates zero-shot capacity in CCU tasks.

## 💾 Data

**Source**: The data in C3bench originates from ten different domains covering various categories in classical Chinese.

**Size**: 50,000 text pairs

**Format**: N/A

**Annotation**: Sentences collected from ancient texts, modern Chinese translations obtained via online searches and manual annotation, with entities labeled by professional annotators.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score

**Calculation**: Metrics are calculated using established methods: accuracy for classification and retrieval, F1 score for NER and punctuation, and BLEU score for translation.

**Interpretation**: An accuracy of 1 is given for a correct classification; F1 score is calculated for NER and punctuation tasks; BLEU score is used for translation.

**Baseline Results**: Existing LLMs struggled with classical Chinese understanding tasks, scoring below 50 average accuracy across evaluations.

**Validation**: Extensive evaluations of 15 representative models conducted using C3bench to quantify their capabilities in Classical Chinese understanding.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
