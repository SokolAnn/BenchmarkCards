# Diplomatic Chinese-English Parallel Dataset

## 📊 Benchmark Details

**Name**: Diplomatic Chinese-English Parallel Dataset

**Overview**: A high-quality diplomatic Chinese-English parallel dataset consisting of 5,528 parallel sentences to evaluate the effectiveness of the Adaptive Few-Shot Prompting framework in machine translation.

**Data Type**: parallel sentences

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To automatically select suitable translation demonstrations for various source input sentences to elicit the translation capability of an LLM for better machine translation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Machine Translation

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from speeches made by spokespersons during routine press conferences regarding diplomatic issues, and publicly accessible data.

**Size**: 5,528 parallel sentences

**Format**: N/A

**Annotation**: Translated by professional translators from specialized institutions.

## 🔬 Methodology

**Methods**:
- Hybrid Retrieval Module
- Reranking

**Metrics**:
- BLEU
- METEOR
- ROUGE-1
- ROUGE-2
- ROUGE-L
- CHRF
- COMET-Kiwi

**Calculation**: Suboptimal examples or instructions can degenerate translation outcomes.

**Interpretation**: Higher scores indicate better translation quality.

**Validation**: Extensive experiments evaluated both our proposed dataset and the United Nations Parallel Corpus.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**
- **Accuracy**: Poor model accuracy
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
