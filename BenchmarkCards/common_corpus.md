# Common Corpus

## 📊 Benchmark Details

**Name**: Common Corpus

**Overview**: Common Corpus is the largest open dataset for language model pre-training, assembled from uncopyrighted or permissible licensed data amounting to about two trillion tokens, covering a variety of languages and domains.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- French
- German
- Spanish
- Latin
- Italian
- Polish
- Greek
- Portuguese
- Russian

**Similar Benchmarks**:
- C4
- Open License Corpus
- Common Pile

**Resources**:
- [Resource](https://huggingface.co/datasets/PleIAs/common_corpus)

## 🎯 Purpose and Intended Users

**Goal**: To provide an open dataset for pre-training large language models that is compliant with data security regulations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Language Modeling
- Text Generation

**Limitations**: Common Corpus does not contain data for instruction-tuning and task-specific fine-tuning.

## 💾 Data

**Source**: Compiles numerous datasets including Open Government, Open Culture, Open Science, Open Code, Open Web, and Open Semantic.

**Size**: 2 trillion tokens

**Format**: Parquet

**Annotation**: Metadata includes document provenance and license information.

## 🔬 Methodology

**Methods**:
- Data filtering
- OCR correction
- Toxicity detection

**Calculation**: Token counts and composition verified through detailed provenance.

**Interpretation**: Dataset designed to ensure quality and compliance for LLM training.

**Validation**: Dataset composition validated through extensive provenance documentation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Includes diverse languages, yet shallow coverage for low-resource languages.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Personally identifiable information removed in compliance with GDPR.

**Data Licensing**: Data primarily falls under Public Domain and various permissive licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Designed to meet legal and regulatory requirements across various jurisdictions.
