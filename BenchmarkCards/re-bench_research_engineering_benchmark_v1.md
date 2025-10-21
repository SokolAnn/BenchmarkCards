# RE-Bench (Research Engineering Benchmark, V1)

## 📊 Benchmark Details

**Name**: RE-Bench (Research Engineering Benchmark, V1)

**Overview**: RE-Bench aims to evaluate whether AI agents can fully automate the work of expert AI R&D researchers, using direct performance comparisons between AI agents and human experts under equivalent conditions and resources.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MLE-bench
- SWE-bench
- GAIA
- Sci-code
- GPQA

**Resources**:
- [GitHub Repository](https://github.com/METR/ai-rd-tasks)
- [Resource](https://transcripts.metr.org)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the AI R&D capabilities of AI agents compared to human experts under equivalent conditions.

**Target Audience**:
- ML Researchers
- AI Developers
- Policy Makers

**Tasks**:
- Machine Learning Optimization

**Limitations**: N/A

## 💾 Data

**Source**: 71 attempts by 61 ML experts completing the tasks under equivalent conditions.

**Size**: 71 experiments

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Direct performance comparison
- Expert baseline evaluation

**Metrics**:
- Score@k
- Average normalized score

**Calculation**: Normalized scores are calculated based on the performance comparison between human experts and AI agents.

**Interpretation**: Higher scores indicate better performance of the AI agents compared to human experts under equivalent conditions.

**Baseline Results**: Expert average normalized scores varied, showing significant differences based on experience and environment.

**Validation**: Cross-validation with multiple iterations and expert evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: ['Risk of underestimating AI capabilities in real-world R&D.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
