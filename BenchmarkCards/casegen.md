# CaseGen

## 📊 Benchmark Details

**Name**: CaseGen

**Overview**: CaseGen is the first comprehensive benchmark designed to evaluate large language models (LLMs) in multi-stage legal case document generation. It includes 500 real case samples annotated by legal experts and supports four key tasks: drafting defense statements, writing trial facts, composing legal reasoning, and generating judgment results.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- LegalBench
- LawBench
- LexEval
- LegalAgentBench

**Resources**:
- [GitHub Repository](https://github.com/CSHaitao/CaseGen)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust framework for evaluating LLMs in legal case document generation, identifying strengths and weaknesses in current models.

**Target Audience**:
- Legal Practitioners
- AI Researchers
- Model Developers

**Tasks**:
- Drafting Defense Statements
- Writing Trial Facts
- Composing Legal Reasoning
- Generating Judgment Results

**Limitations**: CaseGen is built on Chinese legal cases and may not capture the diversity and complexity of legal systems worldwide.

## 💾 Data

**Source**: 500 high-quality legal cases selected from China Judgments Online after rigorous filtering and annotation.

**Size**: 500 examples

**Format**: JSON

**Annotation**: Annotations were conducted by legal experts to ensure quality and compliance with legal standards.

## 🔬 Methodology

**Methods**:
- LLM-as-a-judge evaluation

**Metrics**:
- Accuracy
- ROUGE-L
- BERTScore

**Calculation**: LLM judges score generated documents based on task-oriented criteria and a reference answer.

**Interpretation**: Scores from LLM judges are aligned with legal expert annotations indicating quality.

**Baseline Results**: Compared LLM generated documents against high-quality reference documents.

**Validation**: Human evaluations confirm the assessment framework's effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All personal identifiers have been removed from the datasets to ensure privacy.

**Data Licensing**: Released under CC BY-NC-SA 4.0 license for non-commercial academic use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The development adhered to privacy protection laws and data security regulations.
