# LLM-GLOBE

## 📊 Benchmark Details

**Name**: LLM-GLOBE

**Overview**: The LLM-GLOBE benchmark evaluates the cultural value systems of large language models (LLMs) by utilizing cultural psychology theory and the empirically-validated GLOBE framework, comparing the values of Chinese and US LLMs using a novel evaluation methodology.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- CulturalBench

**Resources**:
- [GitHub Repository](https://github.com/raovish6/LLM-GLOBE)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of the cultural values embedded in LLM outputs and to enhance the understanding of cultural alignment in AI systems.

**Target Audience**:
- ML Researchers
- AI Developers

**Tasks**:
- Cultural Competency Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Evaluated outputs from Chinese and US LLMs using the GLOBE framework.

**Size**: 36,675 closed-ended prompts and 900 open-ended prompts

**Format**: JSON

**Annotation**: Responses scored based on cultural dimensions via a panel of LLM jurors.

## 🔬 Methodology

**Methods**:
- Automated scoring
- Survey methodology

**Metrics**:
- Cultural dimension scores based on GLOBE framework

**Calculation**: Scores calculated using least squares regression for juror assessments.

**Interpretation**: Scores reflect the cultural values embedded in model outputs as analyzed through two distinct prompt types (closed-ended and open-ended).

**Baseline Results**: Cultural dimension scores from the 2004 GLOBE survey serve as baseline comparisons.

**Validation**: The scores were validated against human ratings for consistency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Cultural Sensitivity

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**

**Demographic Analysis**: The benchmark compares cultural values between models trained in the US and China, with potential demographic implications for cultural representation.

**Potential Harm**: Potential cultural misrepresentation and bias in AI outputs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
