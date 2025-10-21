# OIBench

## 📊 Benchmark Details

**Name**: OIBench

**Overview**: OIBench is a high-quality, private, and challenging olympiad-level informatics dataset comprising 250 carefully curated original problems, designed to evaluate LLMs on algorithmic reasoning capabilities.

**Data Type**: algorithmic problems

**Domains**:
- Computer Science

**Languages**:
- Chinese
- English

**Similar Benchmarks**:
- HumanEval
- MBPP
- EffiBench

**Resources**:
- [Resource](https://huggingface.co/datasets/AGI-Eval/OIBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs on Olympiad-level algorithmic problems and advance understanding of their reasoning abilities.

**Target Audience**:
- ML Researchers
- Model Developers
- Academics

**Tasks**:
- Algorithmic Problem Solving

**Limitations**: N/A

## 💾 Data

**Source**: Original algorithmic problems curated from ACM-ICPC team coaches.

**Size**: 250 problems

**Format**: N/A

**Annotation**: Problems were curated by experts and verified for originality and difficulty.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Overall pass rate
- Time/Space Completion Curves

**Calculation**: Metrics are calculated based on the performance of various LLMs in solving the benchmark problems.

**Interpretation**: Higher scores indicate better model performance in solving the problems correctly and efficiently.

**Baseline Results**: SOTA models outperform most human participants.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data
- **Robustness**: Evasion attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
