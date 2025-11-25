# ELUDe (Entity-Level Unlearning Dataset)

## 📊 Benchmark Details

**Name**: ELUDe (Entity-Level Unlearning Dataset)

**Overview**: ELUDe is the first dataset designed to evaluate entity-level unlearning, which involves removing all knowledge related to a specific entity while preserving the remaining model capabilities. It contains 20 real-world target entities and 144 unique neighboring entities, comprising a total of 15,651 forget samples and 90,954 retain samples.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TOFU (Task of Fictitious Unlearning)
- RWKU (Real-World Knowledge Unlearning)

**Resources**:
- [GitHub Repository](https://github.com/brightjade/Opt-Out)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset that enables evaluation of machine unlearning techniques, specifically focused on unlearning knowledge related to specific entities.

**Target Audience**:
- ML Researchers
- Data Privacy Practitioners

**Tasks**:
- Knowledge Unlearning Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Wikipedia

**Size**: 15,651 forget samples and 90,954 retain samples

**Format**: JSON

**Annotation**: Automatically generated QA pairs from Wikipedia pages.

## 🔬 Methodology

**Methods**:
- Entity-Level Unlearning via Optimal Transport

**Metrics**:
- Forget Quality (FQ)
- Retain Quality (RQ)

**Calculation**: FQ is computed as the harmonic mean of probabilities and ROUGE scores on the forget set, while RQ is measured across the retain and world sets.

**Interpretation**: Higher values of FQ and RQ indicate better performance in unlearning and retention.

**Baseline Results**: OPT-OUT (our method) achieves high FQ and competitive RQ performance compared to existing unlearning methods.

**Validation**: Evaluated incorporating existing LLM benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data, Data privacy rights alignment
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is obtained from publicly available Wikipedia pages and does not contain actual user data.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
