# HyGenar: An LLM-Driven Hybrid Genetic Algorithm for Few-Shot Grammar Generation

## 📊 Benchmark Details

**Name**: HyGenar: An LLM-Driven Hybrid Genetic Algorithm for Few-Shot Grammar Generation

**Overview**: This paper presents a dataset consisting of 540 structured grammar generation challenges to evaluate the grammar inference capabilities of large language models (LLMs) using few-shot learning. It introduces the HyGenar algorithm, a hybrid genetic algorithm to optimize grammar generation, significantly improving performance across various LLMs.

**Data Type**: grammar generation challenges

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/RutaTang/HyGenar)

## 🎯 Purpose and Intended Users

**Goal**: To explore and evaluate the few-shot grammar generation capabilities of LLMs and improve their performance using a hybrid genetic algorithm.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Grammar Generation
- Natural Language Processing

**Limitations**: The performance of some LLMs remains unsatisfactory, particularly Mistral:7b-Instruct.

## 💾 Data

**Source**: Challenges designed from LLM-generated reference grammars verified through BNF parsing.

**Size**: 540 challenges

**Format**: N/A

**Annotation**: Manually verified and corrected positive and negative examples based on generated reference grammars.

## 🔬 Methodology

**Methods**:
- Evaluation against baseline models
- Hybrid genetic algorithm

**Metrics**:
- Syntax Correctness
- Semantic Correctness
- Over-Fitting
- Over-Generalization
- Utility

**Calculation**: Metrics are calculated based on the proportion of correct syntax and semantics in the generated grammars against the reference grammars.

**Interpretation**: Higher metrics indicate better performance in generating grammars that accept all positive examples and reject negative ones.

**Validation**: The performance of the proposed HyGenar algorithm was validated against multiple LLMs, showing significant improvements.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
