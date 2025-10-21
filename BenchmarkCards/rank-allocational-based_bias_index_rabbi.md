# Rank-Allocational-Based Bias Index (RABBI)

## 📊 Benchmark Details

**Name**: Rank-Allocational-Based Bias Index (RABBI)

**Overview**: RABBI is a model-agnostic bias measure that assesses potential allocational harms arising from biases in LLM predictions. It compares bias metrics on allocation decision tasks such as resume screening and essay grading, demonstrating its predictive validity across ten LLMs.

**Data Type**: ranking scores

**Domains**:
- Natural Language Processing
- Education
- Finance

**Languages**:
- English

## 🎯 Purpose and Intended Users

**Goal**: To provide a reliable method for evaluating bias risks associated with algorithmic decision-making in resource allocation contexts.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Resource Allocation
- Bias Measurement

**Limitations**: N/A

## 💾 Data

**Source**: Constructed datasets based on resume templates from real job positions and essays from the International Corpus Network of Asian Learners of English (ICNALE).

**Size**: 5,600 essays and multiple resume templates for various job positions.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Predictive Validity Evaluation
- Compare Bias Metrics

**Metrics**:
- Correlation with Allocation Outcomes

**Calculation**: Metrics compared against demographic parity and equal opportunity fairness criteria.

**Interpretation**: Higher scores indicate stronger correlation with allocation disparities.

**Baseline Results**: Comparison with average performance gap metrics and distribution-based metrics.

**Validation**: Extensive evaluation across ten LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Analysis includes gender and racial groups.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
