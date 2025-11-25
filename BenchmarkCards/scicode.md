# SciCode

## 📊 Benchmark Details

**Name**: SciCode

**Overview**: SciCode is a scientist-curated coding benchmark designed to evaluate language models' capabilities in generating code for solving real scientific research problems across 16 diverse natural science sub-fields, such as mathematics, physics, chemistry, biology, and materials science.

**Data Type**: programming tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://scicode-bench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the code generation capabilities of language models in scientific contexts and to motivate research into new AI methods for accelerating scientific research.

**Target Audience**:
- ML Researchers
- AI Developers
- Scientific Researchers

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Problems sourced from the everyday workflows of scientists and existing literature, curated by domain experts.

**Size**: 338 subproblems

**Format**: N/A

**Annotation**: Annotated, revised, and verified by at least two senior researchers in the relevant scientific domain.

## 🔬 Methodology

**Methods**:
- Automated evaluation
- Comparative evaluation

**Metrics**:
- Pass@1 rate

**Calculation**: Metrics are calculated based on the proportion of problems correctly solved by models.

**Interpretation**: A higher pass@1 rate indicates better performance in solving the coding tasks.

**Baseline Results**: Claude3.5-Sonnet: 4.6% pass@1 rate for main problems.

**Validation**: Three rounds of validation by in-domain and out-of-domain scientists, followed by GPT-4 validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
