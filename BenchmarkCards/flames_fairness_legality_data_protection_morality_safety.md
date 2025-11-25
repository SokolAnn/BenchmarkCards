# FLAMES (Fairness, Legality, Data protection, Morality, Safety)

## 📊 Benchmark Details

**Name**: FLAMES (Fairness, Legality, Data protection, Morality, Safety)

**Overview**: FLAMES is a highly adversarial benchmark developed to evaluate the value alignment of large language models (LLMs) specifically in the context of Chinese culture and values, utilizing complex prompts designed to test safety, fairness, morality, and other ethical considerations.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/AIFlames/Flames)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for assessing the value alignment of large language models with human values, particularly focusing on safety and ethical behavior.

**Target Audience**:
- ML Researchers
- AI Developers

**Tasks**:
- Ethical Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: FLAMES-prompt dataset created through manual crafting and testing of prompts on various LLMs.

**Size**: 2,251 prompts

**Format**: JSON

**Annotation**: Responses from 17 LLMs were rigorously annotated by human evaluators for safety, fairness, and alignment with Chinese values.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Harmless Rate
- Harmless Score

**Calculation**: Harmless Rate is calculated as the percentage of completely harmless responses out of total responses for each dimension. Harmless Score is calculated based on the overall scores assigned to the responses.

**Interpretation**: Higher scores indicate better alignment with human values, while lower scores reveal potential safety vulnerabilities or ethical shortcomings.

**Validation**: The benchmark was validated through consistent evaluation processes across different LLMs using a specified scoring method.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Fairness

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All prompts and responses are anonymized, ensuring individual privacy is maintained.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: All data collection and annotations comply with necessary ethical guidelines.
