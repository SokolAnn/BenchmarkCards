# LuxGen

## 📊 Benchmark Details

**Name**: LuxGen

**Overview**: LuxGen is a text generation benchmark for Luxembourgish, introducing four new text generation tasks and evaluating model performance in this under-represented language.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Luxembourgish

**Resources**:
- [Resource](https://huggingface.co/instilux)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of text generation models in Luxembourgish and to fill the gap in benchmarks for this language.

**Target Audience**:
- ML Researchers
- Language Model Developers
- NLP Practitioners

**Tasks**:
- Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: Compiled from Luxembourgish news articles, transcribed interviews, user comments, and Wikipedia articles.

**Size**: N/A

**Format**: N/A

**Annotation**: Manual processing and selection of text data.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU Score

**Calculation**: The BLEU score is used to evaluate text generation output based on n-gram overlaps with reference texts.

**Interpretation**: Higher BLEU scores indicate better alignment with the target text outputs.

**Baseline Results**: Compared against LUXT5, mT5, and Llama models.

**Validation**: Results from multiple tasks evaluated for model performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
