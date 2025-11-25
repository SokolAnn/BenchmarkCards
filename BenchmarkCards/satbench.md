# SATBench

## 📊 Benchmark Details

**Name**: SATBench

**Overview**: SATBench is a benchmark for evaluating the logical reasoning capabilities of large language models through logical puzzles derived from Boolean satisfiability (SAT) problems. The benchmark comprises 2100 automatically generated logical puzzles validated through LLM and solver checks.

**Data Type**: logical puzzles

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LogiQA
- ReClor
- FOLIO
- P-FOLIO

**Resources**:
- [GitHub Repository](https://github.com/Anjiang-Wei/SATBench)

## 🎯 Purpose and Intended Users

**Goal**: To assess large language models' logical reasoning via SAT-derived puzzles emphasizing search-based logical reasoning tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Logical Reasoning

**Limitations**: Focuses only on Boolean satisfiability problems.

## 💾 Data

**Source**: Automatically generated from Boolean satisfiability problems

**Size**: 2100 puzzles

**Format**: N/A

**Annotation**: Validation through LLM-based and solver-based checks, with human validation on a subset.

## 🔬 Methodology

**Methods**:
- LLM evaluation
- Solver-based validation

**Metrics**:
- Accuracy

**Calculation**: Accuracy measured as the percentage of correct satisfiability predictions.

**Interpretation**: Accuracy indicates the model's proficiency in determining satisfiability while also assessing the correctness of the reasoning trace.

**Baseline Results**: The random baseline for satisfiability prediction is 50%.

**Validation**: Quality assurance through both LLM and solver consistency checks, including human validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
