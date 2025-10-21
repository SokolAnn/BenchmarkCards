# GUMsley

## 📊 Benchmark Details

**Name**: GUMsley

**Overview**: GUMsley is the first entity salience dataset covering all named and non-named salient entities for 12 genres of English text, aligned with entity types, Wikification links, and full coreference resolution annotations.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- UD English GUM corpus

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate entity salience in summarization across various English genres and assist in improving entity-aware summarization methods.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Model Developers

**Tasks**:
- Entity Salience Extraction
- Text Summarization

**Limitations**: N/A

## 💾 Data

**Source**: GUM (Georgetown University Multilayer corpus)

**Size**: 57,359 mentions across 213 documents

**Format**: N/A

**Annotation**: Manually annotated by trained experts with entity salience labels.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- ROUGE-1
- ROUGE-2
- ROUGE-L
- BERTScore

**Calculation**: Metrics were calculated based on overlap between generated summaries and reference summaries.

**Interpretation**: Higher scores in metrics indicate better performance in capturing salient entities and summarization quality.

**Baseline Results**: BRIO, CTRLSum, and GPT-4 models were evaluated against the GUMsley dataset.

**Validation**: Evaluation combines qualitative and quantitative analyses of summary quality and entity capture.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
