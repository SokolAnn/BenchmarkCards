# Trident-Bench

## 📊 Benchmark Details

**Name**: Trident-Bench

**Overview**: Trident-Bench is a benchmark specifically targeting LLM safety in the legal, financial, and medical domains, designed to systematically assess LLMs' adherence to domain-specific safety standards.

**Data Type**: harmful prompts and safe responses

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MedSafetyBench

**Resources**:
- [GitHub Repository](https://github.com/zackhuiiiii/TRIDENT)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate LLM safety in high-stakes domains through alignment with professional codes.

**Target Audience**:
- Regulators
- Developers
- Practitioners

**Tasks**:
- Safety Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Realistic, scenario-driven examples grounded in professional guidelines from domains such as finance, law, and medicine.

**Size**: 2,652 harmful prompts

**Format**: N/A

**Annotation**: Annotated by domain experts

## 🔬 Methodology

**Methods**:
- Harmful prompt generation
- Response evaluation by domain experts

**Metrics**:
- Harmfulness score

**Calculation**: Combining multiple jurors for stable ratings

**Interpretation**: Scores closer to 1 indicate safer behavior, while closer to 5 indicate unsafe behavior.

**Baseline Results**: Evaluated against general-purpose, domain-specialized, and safety-aligned models.

**Validation**: Expert-reviewed and annotated by qualified domain professionals.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Ethics

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias
- **Privacy**: Data privacy rights alignment

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The project received IRB approval.
