# JDocQA (Japanese Document Question Answering)

## 📊 Benchmark Details

**Name**: JDocQA (Japanese Document Question Answering)

**Overview**: JDocQA is a large-scale document-based QA dataset, requiring both visual and textual information to answer questions. It comprises 5,504 documents in PDF format and 11,600 annotated question-and-answer instances in Japanese.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Japanese

**Resources**:
- [Resource](https://arxiv.org/abs/2403.19454)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for generative language models to effectively perform question answering on Japanese documents incorporating both visual and textual information.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Japanese documents collected from open-access sources including governmental and public documents.

**Size**: 5,504 documents and 11,600 question-and-answer pairs

**Format**: PDF

**Annotation**: Manual annotation by 43 annotators, including multiple question categories and unanswerable questions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- BLEU Score

**Calculation**: Metrics are calculated based on exact matches for Yes/No, factoid, and numerical questions, and BLEU Score for open-ended questions.

**Interpretation**: Higher scores indicate better question-answering performance.

**Baseline Results**: Results are reported for multiple models including StableLM and OpenAI GPT series.

**Validation**: Models are evaluated on distinct validation and test sets including those with and without unanswerable questions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: Potential harm through hallucination generation in language models.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
