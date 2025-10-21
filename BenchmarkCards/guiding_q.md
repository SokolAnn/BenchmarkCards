# GUIDING Q

## 📊 Benchmark Details

**Name**: GUIDING Q

**Overview**: GUIDING Q is a dataset of 10,577 guiding questions extracted from research articles and textbooks to study their roles and effects on human reading comprehension.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/eth-lre/engage-your-readers)

## 🎯 Purpose and Intended Users

**Goal**: To analyze the use, distribution, and roles of guiding questions in academic writing, and to explore automated question generation techniques.

**Target Audience**:
- ML Researchers
- Educators
- Model Developers

**Tasks**:
- Text Classification
- Question Generation

**Limitations**: N/A

## 💾 Data

**Source**: Extracted from textbooks and scientific articles, particularly from OpenStax, arXiv, and PubMed datasets.

**Size**: 10,577 questions

**Format**: CSV

**Annotation**: Questions were extracted and annotated using both human and large language model (LLM) methods.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- BERTScore
- ROUGE-L

**Calculation**: Metrics were calculated based on the generated questions' alignment with expert-generated questions.

**Interpretation**: Higher scores in metrics indicate better quality and relevance of generated questions.

**Baseline Results**: N/A

**Validation**: The dataset and models were validated through human studies and comparisons with existing datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Creating unequal social relationships through question framing.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants consented to the human studies conducted.

**Compliance With Regulations**: Not Applicable
