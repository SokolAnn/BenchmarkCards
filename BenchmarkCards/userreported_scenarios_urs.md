# UserReported Scenarios (URS)

## 📊 Benchmark Details

**Name**: UserReported Scenarios (URS)

**Overview**: A benchmark to evaluate large language models (LLMs) from a user-centric perspective, measuring their efficacy in satisfying user needs under distinct intents using real-world use cases collected from a global user study.

**Data Type**: self-reported logs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- AlpacaEval
- MT-Bench-101
- TencentLLMEval
- MT Bench
- AlignBench
- WildBench

**Resources**:
- [GitHub Repository](https://github.com/Alice1998/URS)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark LLMs based on user-reported scenarios to help users select suitable models for their specific needs and preferences.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- User Intent Recognition
- LLM Evaluation

**Limitations**: The benchmark primarily assesses user satisfaction and efficacy in user-centric scenarios, but does not cover all LLM performance aspects.

## 💾 Data

**Source**: Collected from user studies with 712 participants across 23 countries.

**Size**: 1,846 examples

**Format**: N/A

**Annotation**: Data was vetted through third-party manual quality checks.

## 🔬 Methodology

**Methods**:
- LLM-based pairwise evaluation

**Metrics**:
- Pearson correlation

**Calculation**: Correlation between benchmark scores and human preferences was calculated to validate the evaluation method.

**Interpretation**: Scores align with user satisfaction levels, indicating effective evaluation.

**Baseline Results**: Pearson correlations of 0.95 and 0.94 with real-world experiences and pairwise annotations.

**Validation**: Alignment of benchmark results with human preferences was validated through user studies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Participants were informed their responses might be publicly released for research; no personal information was collected.

**Data Licensing**: The dataset is available under an Apache License.

**Consent Procedures**: Participants voluntarily provided anonymized information.

**Compliance With Regulations**: Not Applicable
