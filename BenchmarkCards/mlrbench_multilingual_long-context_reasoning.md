# MLRBench (Multilingual Long-Context Reasoning)

## 📊 Benchmark Details

**Name**: MLRBench (Multilingual Long-Context Reasoning)

**Overview**: MLRBench is a new synthetic benchmark for multilingual long-context reasoning, designed to assess multi-hop inference, aggregation, and epistemic reasoning tasks across multiple languages. It is scalable, resistant to leakage, and offers a comprehensive evaluation of LLMs' reasoning capabilities over extended multilingual contexts.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Spanish
- German
- Hindi
- Arabic
- Vietnamese
- Simplified Chinese

**Similar Benchmarks**:
- MLNeedle
- mLongRR

**Resources**:
- [GitHub Repository](https://github.com/AmeyHengle/multilingual-long-context-reasoning)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs' reasoning capabilities over multilingual long contexts beyond retrieval and haystack approaches, providing a rigorous framework for assessment.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Basic Factoid QA
- Yes/No or Negation
- Fact Chaining
- Association
- Counting
- List / Set
- Indefinite Knowledge

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic generation of data instances based on the bAbI dataset structure, translated into multiple languages.

**Size**: 8,000 evaluation prompts per language

**Format**: JSON

**Annotation**: Automated generation using controlled and reproducible procedures.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the percentage of correct answers across the evaluation dataset.

**Interpretation**: A higher accuracy score indicates better performance in reasoning and context understanding tasks.

**Baseline Results**: N/A

**Validation**: Tested for reliability across multiple context lengths.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
