# Beyond the Hype: Benchmarking LLM-Evolved Heuristics for Bin Packing

## 📊 Benchmark Details

**Name**: Beyond the Hype: Benchmarking LLM-Evolved Heuristics for Bin Packing

**Overview**: This paper conducts the first rigorous benchmarking study of new LLM-generated heuristics for bin packing, comparing them to established heuristics across a large suite of benchmark instances to evaluate their generalization capabilities.

**Data Type**: bin-packing instances

**Domains**:
- Operations Research
- Combinatorial Optimisation

**Languages**:
- English

**Similar Benchmarks**:
- BBOB
- OR-Library

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.14162744)
- [Resource](https://site.unibo.it/operations-research/en/research/bpplib-a-bin-packing-problem-library)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously benchmark LLM-generated heuristics against established heuristics in the bin packing domain and to evaluate their performance across diverse datasets.

**Target Audience**:
- Researchers in Operations Research
- Algorithm Designers
- Industry Practitioners

**Tasks**:
- Heuristic Evaluation
- Algorithm Comparison

**Limitations**: N/A

## 💾 Data

**Source**: Datasets were obtained from literature including BPPLib and other domains, with instances drawn from various distributions.

**Size**: 6,064 instances across 12 datasets

**Format**: N/A

**Annotation**: Items were randomly shuffled for online packing scenarios.

## 🔬 Methodology

**Methods**:
- Comparative Evaluation
- Instance Space Analysis

**Metrics**:
- Average Excess Bins (AEB)
- Falkanauer fitness
- Percentage of Wins

**Calculation**: Metrics calculated based on the performance of each heuristic across the benchmark datasets.

**Interpretation**: Lower Average Excess Bins indicates better packing efficiency among heuristics.

**Baseline Results**: Established hand-designed heuristics (e.g., Best-Fit, First-Fit) were used as baselines.

**Validation**: Validation through extensive comparisons across a broad suite of benchmark instances.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt leaking, Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
