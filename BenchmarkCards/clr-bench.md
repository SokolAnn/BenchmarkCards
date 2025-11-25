# CLR-Bench

## 📊 Benchmark Details

**Name**: CLR-Bench

**Overview**: CLR-Bench is a benchmark specifically designed to evaluate the reasoning capabilities of large language models in college-level tasks, focusing on computer science and artificial intelligence, comprised of 1,018 discipline-specific questions across five question types.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- MMLU-Pro
- CMMLU
- C-Eval
- GSB-8K
- MATH

**Resources**:
- [Resource](https://anonymous.4open.science/r/CLR-Bench-7771)

## 🎯 Purpose and Intended Users

**Goal**: To comprehensively evaluate the reasoning ability of large language models in college-level tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Collected from 16 authoritative college textbooks guided by domain experts and structured according to a hierarchical topic graph.

**Size**: 1,018 questions

**Format**: JSONL

**Annotation**: Expert-guided rationale generation using GPT-4o and manual verification.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Expert evaluation

**Metrics**:
- Q →A
- Q →AR

**Calculation**: Metrics are calculated based on the correctness of the answers and the quality of the rationales provided.

**Interpretation**: Higher scores in Q →A indicate better answer predictions; Q →AR assesses both answer correctness and rationale quality.

**Baseline Results**: N/A

**Validation**: Extensive experiments conducted across 40 language models to validate results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
