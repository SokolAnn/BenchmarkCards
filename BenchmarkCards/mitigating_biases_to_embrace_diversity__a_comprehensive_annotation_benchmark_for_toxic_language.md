# Mitigating Biases to Embrace Diversity: A Comprehensive Annotation Benchmark for Toxic Language

## 📊 Benchmark Details

**Name**: Mitigating Biases to Embrace Diversity: A Comprehensive Annotation Benchmark for Toxic Language

**Overview**: This study introduces a prescriptive annotation benchmark grounded in humanities research to ensure consistent, unbiased labeling of offensive language, particularly for casual and non-mainstream language uses. It contributes two newly annotated datasets to achieve higher inter-annotator agreement between human and language model annotations compared to original datasets based on descriptive instructions.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Paparare/toxic_benchmark_2024)

## 🎯 Purpose and Intended Users

**Goal**: To enable consistent offensive language data labeling with high reliability while preventing biases against language minorities, hence protecting natural language diversity.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Offensive Language Detection

**Limitations**: The classifications of aggressive expressions are not definitive and may shift over time with evolving cultural norms.

## 💾 Data

**Source**: Two newly annotated datasets based on the proposed annotation benchmark, including various social media platforms.

**Size**: 1,942 pieces

**Format**: N/A

**Annotation**: Annotated based on prescriptive criteria to ensure high inter-rater reliability.

## 🔬 Methodology

**Methods**:
- Statistical analysis
- LLM-based annotation
- Human annotation

**Metrics**:
- Inter-Annotator Reliability
- Accuracy of Annotation

**Calculation**: Inter-Annotator reliability was calculated using Cohen’s Kappa and Gwet’s AC1.

**Interpretation**: Higher scores indicate better agreement among annotators, reflecting consistency in labeling.

**Validation**: Validation was conducted through inter-rater reliability checks using multiple annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: Analysis of bias in relation to different language varieties including casual and non-mainstream uses.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
