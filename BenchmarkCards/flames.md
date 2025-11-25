# FLAMES

## 📊 Benchmark Details

**Name**: FLAMES

**Overview**: FLAMES is a benchmark designed to evaluate the value alignment of large language models (LLMs) in Chinese, incorporating various dimensions of human values including safety, fairness, morality, legality, and data protection. It consists of adversarial prompts crafted to uncover vulnerabilities in model responses, emphasizing the need for deeper alignment with human values.

**Data Type**: Adversarial prompts

**Domains**:
- Natural Language Processing
- Ethics in AI

**Languages**:
- Chinese

**Similar Benchmarks**:
- HHH dataset
- Do-Not-Answer dataset

**Resources**:
- [GitHub Repository](https://github.com/AIFlames/Flames)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the alignment of LLMs with human values, specifically designed for the Chinese context.

**Target Audience**:
- Researchers
- AI developers
- Ethicists

**Tasks**:
- Assessing LLM responses to prompts
- Generating detailed evaluations based on model performance

**Limitations**: None

## 💾 Data

**Source**: FLAMES - Prompts Dataset

**Size**: 2,251 prompts

**Format**: Manual annotations

**Annotation**: Each response from 17 LLMs is annotated for evaluation.

## 🔬 Methodology

**Methods**:
- Prompt testing
- Human evaluation of model responses
- Development of a specified scoring model

**Metrics**:
- Harmless rate
- Harmless score

**Calculation**: Harmless rate is calculated as the percentage of harmless responses out of total responses.

**Interpretation**: Higher scores indicate better alignment with human values, revealing vulnerabilities in model responses.

**Baseline Results**: Claude achieved the highest harmless rate of 63.77%.

**Validation**: Responses were annotated by experts across various fields to ensure quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Fairness
- Legality
- Data Protection
- Morality

**Atlas Risks**:
- **Accuracy**

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset is designed to respect privacy by not incorporating identifiable personal data.

**Data Licensing**: The FLAMES dataset is publicly available for research purposes.

**Consent Procedures**: Data collection follows ethical guidelines to minimize harm.

**Compliance With Regulations**: The benchmark aims to comply with relevant laws around data privacy and use.
