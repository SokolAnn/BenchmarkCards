# KleioGPT

## 📊 Benchmark Details

**Name**: KleioGPT

**Overview**: The paper presents a methodology for augmenting Large Language Models (LLMs) with specialized academic sources to assist historical research, demonstrating how LLMs can aid in question-answering and data extraction from a custom corpus of documents.

**Data Type**: text

**Domains**:
- Natural Language Processing
- History

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/GissyGonzalez/KleioGPT)

## 🎯 Purpose and Intended Users

**Goal**: To demonstrate how LLMs can enhance the historical research process by providing conversational assistance and accurate information retrieval from academic corpora.

**Target Audience**:
- Historians
- Researchers in the Humanities
- Machine Learning Practitioners

**Tasks**:
- Question Answering
- Data Extraction

**Limitations**: N/A

## 💾 Data

**Source**: A comprehensive academic corpus of digitized history monographs and genealogical compilations, specifically focusing on Migration Studies.

**Size**: 1,803,596 words across 86 books

**Format**: PDF

**Annotation**: Text extracted from digitized historical documents.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Factual accuracy
- Completeness of answers

**Calculation**: Calculated the proportion of correct answers to the total number of questions assessed.

**Interpretation**: Results interpreted through the performance of LLMs when presented with both prompt-specific questions and context-rich materials.

**Baseline Results**: Comparison against established LLMs such as GPT3 and ChatGPT.

**Validation**: Evaluated by grading responses against known correct answers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The implementation provides private querying capabilities for researchers using the LLMs with their own data without third-party access.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
