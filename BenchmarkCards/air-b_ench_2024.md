# AIR-B ENCH 2024

## 📊 Benchmark Details

**Name**: AIR-B ENCH 2024

**Overview**: AIR-B ENCH 2024 is the first AI safety benchmark aligned with emerging government regulations and company policies, providing a foundation for assessing model safety across jurisdictions.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/stanford-crfm/air-bench-2024)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and relevant evaluation tool for assessing AI model safety based on regulatory frameworks.

**Target Audience**:
- AI Researchers
- Policymakers
- Industry Practitioners

**Tasks**:
- Model Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Manually curated prompts derived from AI risks specified in 8 government regulations and 16 company policies.

**Size**: 5,694 examples

**Format**: N/A

**Annotation**: Manual curation and human auditing to ensure quality.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Refusal rate

**Calculation**: The refusal rate is calculated as the percentage of scores that indicate a refusal to generate risky content.

**Interpretation**: Higher refusal rates indicate better alignment with safety guidelines.

**Baseline Results**: N/A

**Validation**: Category-specific evaluation using manually crafted and model-generated judge prompts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Privacy**: Personal information in prompt
- **Robustness**: Evasion attack, Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
