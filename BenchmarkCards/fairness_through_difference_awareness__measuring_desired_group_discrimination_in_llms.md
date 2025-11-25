# Fairness through Difference Awareness: Measuring Desired Group Discrimination in LLMs

## 📊 Benchmark Details

**Name**: Fairness through Difference Awareness: Measuring Desired Group Discrimination in LLMs

**Overview**: This paper introduces a benchmark suite composed of eight different scenarios for a total of 16,000 questions that enables assessment of difference awareness, demonstrating that treating people differently may be contextually appropriate in certain settings.

**Data Type**: multiple choice questions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Angelina-Wang/difference_awareness)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark suite designed to measure difference awareness and contextual awareness in language models.

**Target Audience**:
- ML Researchers
- Fairness Researchers
- AI Practitioners

**Tasks**:
- Fairness Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Generated based on contextual questions covering descriptive and normative aspects of group awareness.

**Size**: 16,000 questions

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Evaluation of language models

**Metrics**:
- Difference Awareness (DiffAware)
- Contextual Awareness (CtxtAware)

**Calculation**: DiffAware = A / (A + B + C); CtxtAware = A / (A + D + E)

**Interpretation**: Values indicate model's ability to distinguish group differences and contextual appropriateness of these differences.

**Baseline Results**: N/A

**Validation**: Empirical results based on performance across ten models

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
