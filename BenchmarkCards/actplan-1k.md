# ActPlan-1K

## 📊 Benchmark Details

**Name**: ActPlan-1K

**Overview**: ActPlan-1K is a multi-modal planning benchmark constructed based on ChatGPT and household activity simulator iGibson2. It evaluates the planning ability of visual language models (VLMs) for procedural planning in household activities, consisting of 153 activities and 1,187 instances with corresponding natural language task descriptions and environment images.

**Data Type**: multi-modal instances (text and images)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Behavior-100
- EgoPlan-Bench
- ALFRED
- Watch-And-Help

**Resources**:
- [GitHub Repository](https://github.com/HKUST-KnowComp/ActPlan-1K)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the procedural planning ability of visual language models (VLMs) in household activities, including counterfactual scenarios.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Procedural Planning
- Counterfactual Planning

**Limitations**: The images collected from iGibson2 simulator are of low-resolution which may influence image understanding of VLMs.

## 💾 Data

**Source**: Generated using iGibson2 simulator and ChatGPT

**Size**: 1,187 instances

**Format**: N/A

**Annotation**: Generated natural language task descriptions and evaluated by human annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Correctness
- Commonsense satisfaction
- Longest Common Subsequence (LCS)
- BLEURT-based accuracy score

**Calculation**: Human annotations are used for correctness and commonsense satisfaction, while automatic metrics are calculated using LCS and BLEURT.

**Interpretation**: Correctness is assessed based on whether the procedural plan achieves the final activity goal, and commonsense satisfaction checks the plausibility of each step. Scores indicate the performance of different VLMs based on these measures.

**Baseline Results**: Results showed that most VLMs struggle to meet human-level procedural planning standards.

**Validation**: Through human evaluation and comparison against gold standard plans.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
