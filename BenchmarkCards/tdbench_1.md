# TDBench

## 📊 Benchmark Details

**Name**: TDBench

**Overview**: TDBench is a new benchmark that systematically constructs Time-Sensitive Question-Answering (TSQA) pairs by leveraging temporal databases and techniques such as temporal SQL and functional dependencies, aimed at providing scalable and comprehensive evaluation of LLMs on time-sensitive factual knowledge.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/ssoy0701/tdbench.git)

## 🎯 Purpose and Intended Users

**Goal**: To enable a scalable and comprehensive evaluation of LLMs' capabilities in handling time-sensitive factual knowledge.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Time-Sensitive Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Temporal databases sourced from Wikipedia and Kaggle, covering dynamic real-world scenarios.

**Size**: 7,881 questions

**Format**: N/A

**Annotation**: Automatically generated using database techniques.

## 🔬 Methodology

**Methods**:
- Automated metrics
- SQL-based evaluation

**Metrics**:
- Answer accuracy
- Time accuracy
- Answer-Time accuracy

**Calculation**: Metrics are calculated based on correctness of answers and time references outputted by LLMs.

**Interpretation**: Higher values reflect better performance in accurately answering time-sensitive questions and correctly referencing time.

**Baseline Results**: N/A

**Validation**: Evaluation is validated through extensive experiments comparing with existing benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
