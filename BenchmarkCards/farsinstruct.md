# FarsInstruct

## 📊 Benchmark Details

**Name**: FarsInstruct

**Overview**: FarsInstruct is a comprehensive instruction dataset designed to enhance the instruction-following ability of large language models specifically for the Persian language. It includes a mixture of tasks derived from existing datasets as well as translations from the Public Pool of Prompts, ensuring diverse linguistic representation.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Persian

**Similar Benchmarks**:
- FLAN
- P3
- SuperNaturalInstruction

**Resources**:
- [Resource](https://huggingface.co/datasets/PNLPhub/FarsInstruct)
- [GitHub Repository](https://github.com/Hojjat-Mokhtarabadi/FarsInstruct)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust dataset that improves the instruction comprehension of large language models for Persian, a low-resource language.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Text Classification
- Question Answering
- Sentiment Analysis
- Text Summarization
- Translation
- Named Entity Recognition
- Word Sense Disambiguation
- Reading Comprehension
- Query Paraphrasing
- Textual Entailment

**Limitations**: FarsInstruct may not fully capture the rich diversity of Persian dialects and languages, and the prompts might not sufficiently challenge models in handling complex instructions.

## 💾 Data

**Source**: Publicly available Persian NLP datasets and translations from the Public Pool of Prompts.

**Size**: N/A

**Format**: N/A

**Annotation**: Human-annotated and translation-based methods.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- ROUGE-L

**Calculation**: ROUGE-L F1 scores evaluate overlap of n-grams between generated text and reference texts.

**Interpretation**: Higher ROUGE-L scores indicate better performance in mimicking human language understanding and generation.

**Validation**: The dataset is validated through a comparison against various models fine-tuned on instruction data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The dataset's language support necessitates that future iterations cover a broader array of Persian dialects.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
