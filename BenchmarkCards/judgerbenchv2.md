# JudgerBenchV2

## 📊 Benchmark Details

**Name**: JudgerBenchV2

**Overview**: JudgerBenchV2 is a comprehensive benchmark evaluating cross-domain judgment accuracy and rank consistency to standardize judge model evaluation.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- JudgeBench
- Rewardbench

**Resources**:
- [GitHub Repository](https://github.com/open-compass/CompassJudger)

## 🎯 Purpose and Intended Users

**Goal**: To improve the evaluation landscape for judge models and provide a more comprehensive and accurate benchmark.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Model Evaluation
- Judging Tasks

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from a variety of publicly available judge and reward datasets, clustered real-world user queries, and high-performing model responses.

**Size**: 10,000 questions

**Format**: N/A

**Annotation**: Judgments based on a Mix-of-Judgers consensus and evaluated by a judge model.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Pairwise comparisons

**Metrics**:
- Accuracy
- Rank fidelity

**Calculation**: Performance scores are derived by comparing judgments against ground truth from a Mix-of-Judgers.

**Interpretation**: Higher scores indicate better judgment accuracy and consistency in rankings.

**Baseline Results**: CompassJudger-2 consistently outperforms other judge models, achieving state-of-the-art performance.

**Validation**: Through rigorous evaluations against multiple judge benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
