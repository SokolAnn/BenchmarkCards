# ESSAY JUDGE

## 📊 Benchmark Details

**Name**: ESSAY JUDGE

**Overview**: ESSAY JUDGE is the first multimodal benchmark for assessing the automated essay scoring (AES) capabilities of multimodal large language models (MLLMs) across lexical-, sentence-, and discourse-level traits.

**Data Type**: multimodal essays

**Domains**:
- Education

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/path/to/repository)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the AES capabilities of multimodal large language models (MLLMs) across lexical, sentence, and discourse-level traits.

**Target Audience**:
- ML Researchers
- Educators
- Model Developers

**Tasks**:
- Automated Essay Scoring

**Limitations**: The dataset primarily consists of essays written by non-native speakers of English, which may not fully represent native speakers' essays.

## 💾 Data

**Source**: K-12 Education Organization providing a repository of graded essays by experienced educators.

**Size**: 1,054 multimodal essays

**Format**: N/A

**Annotation**: Multi-round human annotation and verification by educators and linguistic experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Quadratic Weighted Kappa (QWK)

**Calculation**: QWK measures the agreement between model scores and the ground truth.

**Interpretation**: Scores closer to 1 indicate better agreement with human evaluations.

**Baseline Results**: QWK scores reveal gaps in AES performance compared to human evaluators.

**Validation**: Comparative evaluation involving multiple MLLMs and human evaluators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: The dataset includes work from non-native English speakers, which may introduce bias in scoring.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
