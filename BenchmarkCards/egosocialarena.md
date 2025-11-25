# EgoSocialArena

## 📊 Benchmark Details

**Name**: EgoSocialArena

**Overview**: EgoSocialArena is a novel framework designed to systematically evaluate the social intelligence of LLMs from a first-person perspective, grounded in cognitive, situational, and behavioral intelligence.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ToMI
- BigToM
- FanToM
- HI-ToM
- OpenToM
- ToMBench
- SocialIQa
- NormBank
- SOTOPIA
- LLMArena

**Resources**:
- [GitHub Repository](https://github.com/gyhou123/EgoSocialArena)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the social intelligence of large language models from a first-person perspective.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- ToM Reasoning
- Behavioral Evaluation
- Situational Understanding

**Limitations**: Our study only involves the text modality and does not utilize ego-centric images and videos; the evaluation is limited to eight prominent foundation LLMs.

## 💾 Data

**Source**: Constructed from static ToM benchmarks, dynamic interaction scenarios, and situational assessments.

**Size**: 2,245 data entries

**Format**: JSON

**Annotation**: Manually verified and corrected after generation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Win rate
- Goal completion

**Calculation**: Metrics are calculated based on LLM performance in various tasks compared to a human baseline.

**Interpretation**: Higher scores indicate better performance in social intelligence tasks evaluated from a first-person perspective.

**Baseline Results**: Human performance serves as a baseline, with average scores across various scenarios.

**Validation**: Two rounds of validation for data integrity and quality, leading to an average agreement of 97.6%.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
