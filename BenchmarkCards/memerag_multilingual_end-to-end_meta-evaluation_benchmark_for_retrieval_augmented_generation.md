# MEMERAG (Multilingual End-to-End Meta-Evaluation Benchmark for Retrieval Augmented Generation)

## 📊 Benchmark Details

**Name**: MEMERAG (Multilingual End-to-End Meta-Evaluation Benchmark for Retrieval Augmented Generation)

**Overview**: This paper develops a multilingual end-to-end meta-evaluation benchmark for retrieval augmented generation (RAG) systems that supports the development of automatic evaluators correlating well with human judgment. The benchmark is built on native-language questions and generates responses using diverse large language models, assessed for faithfulness and relevance by expert annotators.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- German
- Spanish
- French
- Hindi

**Similar Benchmarks**:
- MIRACL

**Resources**:
- [GitHub Repository](https://github.com/amazon-science/MEMERAG)

## 🎯 Purpose and Intended Users

**Goal**: To support the development of reliable automatic evaluation methods for RAG systems across multiple languages, facilitating comprehensive end-to-end benchmarking.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Meta-Evaluation
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: MIRACL dataset

**Size**: 1,250 questions

**Format**: N/A

**Annotation**: Annotated by expert human annotators for faithfulness and relevance.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Balanced Accuracy

**Calculation**: Performance is evaluated with Balanced Accuracy (BAcc), with equal weights on each coarse-grained label and language.

**Interpretation**: Higher Balanced Accuracy indicates better correlation with human judgement for evaluating the quality of model-generated answers.

**Baseline Results**: Baseline results established for various prompting techniques and LLMs on the benchmark dataset.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Lack of multilingual evaluators that correlate with human judgment']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
