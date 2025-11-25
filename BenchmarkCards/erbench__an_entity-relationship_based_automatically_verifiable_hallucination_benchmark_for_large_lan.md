# ERBench: An Entity-Relationship based Automatically Verifiable Hallucination Benchmark for Large Language Models

## 📊 Benchmark Details

**Name**: ERBench: An Entity-Relationship based Automatically Verifiable Hallucination Benchmark for Large Language Models

**Overview**: ERBench is a benchmark that utilizes relational databases based on the entity-relationship model to create complex, automatically verifiable evaluations for large language models. It measures the capability of LLMs to reason correctly while minimizing hallucinations.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/DILAB-KAIST/ERBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide an automated and scalable framework for evaluating the reasoning capabilities of large language models while addressing the issue of factual hallucination.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The benchmark primarily checks for critical keywords to verify LLM rationales, which may not cover the correctness of the entire rationale.

## 💾 Data

**Source**: Public relational databases from various domains including movie, soccer, airport, music, and book datasets, sourced from reputable platforms like Kaggle and GitHub.

**Size**: varied based on the chosen database; typically includes thousands of entities and relationships

**Format**: Relational database format

**Annotation**: Automatically generated using integrity constraints such as functional dependencies and foreign key constraints.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Answer Accuracy
- Rationale Accuracy
- Answer-Rationale Accuracy
- Hallucination Rate

**Calculation**: Metrics are calculated based on the correctness of answers and rationales derived from integrity constraints present in the relational databases.

**Interpretation**: Higher accuracy values indicate better performance of LLMs in generating both correct answers and rationales, while lower hallucination rates suggest fewer incorrect responses.

**Baseline Results**: N/A

**Validation**: Experimental validation conducted across multiple datasets using various contemporary large language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
