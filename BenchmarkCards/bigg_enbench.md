# BIGG ENBENCH

## 📊 Benchmark Details

**Name**: BIGG ENBENCH

**Overview**: BIGG ENBENCH is a principled generation benchmark designed to evaluate nine distinct capabilities of language models (LMs) across 77 diverse tasks with instance-specific evaluation criteria.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/prometheus-eval/prometheus-eval)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate language models' proficiency in a specific capability.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Instruction Following
- Grounding
- Reasoning
- Planning
- Refinement
- Safety
- Theory of Mind
- Tool Usage
- Multilingual

**Limitations**: N/A

## 💾 Data

**Source**: Crafted through a human-in-the-loop approach, validated by multiple annotators.

**Size**: 765 instances across 77 tasks

**Format**: N/A

**Annotation**: Annotated manually by annotators with expertise in the relevant field.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Pearson correlation

**Calculation**: Correlation coefficients were computed to assess the relationship between responses from evaluator language models and human judgments.

**Interpretation**: High values indicate strong correlation with human evaluators, reflecting reliability in assessment.

**Baseline Results**: N/A

**Validation**: Performance comparisons to human evaluators indicate strong correlations across different capabilities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Instances were created through a human-in-the-loop process to ensure ethical considerations in data usage.

**Data Licensing**: The BIGG ENBENCH is distributed under the CC-BY-SA license.

**Consent Procedures**: Participants were informed of potential risks and had the right to opt-out during studies.

**Compliance With Regulations**: Not Applicable
