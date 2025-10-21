# LEXBENCH

## 📊 Benchmark Details

**Name**: LEXBENCH

**Overview**: LEXBENCH is a comprehensive evaluation suite that tests language models on ten semantic phrase processing tasks, including idiomatic expression detection, noun compound identification, and lexical collocation extraction.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/jacklanda/LexBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust evaluation framework for measuring the performance of language models on semantic phrase processing tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Idiomatic Expression Detection
- Idiomatic Expression Extraction
- Idiomatic Expression Interpretation
- Noun Compound Compositionality
- Noun Compound Extraction
- Noun Compound Interpretation
- Lexical Collocation Categorization
- Lexical Collocation Extraction
- Lexical Collocation Interpretation
- Verbal Multiword Expression Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Multiple datasets curated from existing sources, including ID10M and PIE datasets.

**Size**: 10 datasets across various tasks

**Format**: N/A

**Annotation**: Manually annotated and curated for specific semantic tasks.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match (EM)
- Token-level F1 Score
- Phrase-level Accuracy
- ROUGE-L
- BERT Score

**Calculation**: Each metric calculated based on task-specific instructions for evaluating model outputs against gold standards.

**Interpretation**: Higher scores indicate better performance in understanding and processing semantic phrases.

**Baseline Results**: Performance metrics were compared across multiple language models including GPT-4 and Claude-3.

**Validation**: Evaluation included comparisons with human performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
