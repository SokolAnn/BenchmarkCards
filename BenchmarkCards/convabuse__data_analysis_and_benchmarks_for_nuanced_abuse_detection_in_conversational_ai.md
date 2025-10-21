# ConvAbuse: Data, Analysis, and Benchmarks for Nuanced Abuse Detection in Conversational AI

## 📊 Benchmark Details

**Name**: ConvAbuse: Data, Analysis, and Benchmarks for Nuanced Abuse Detection in Conversational AI

**Overview**: We present the first English corpus study on abusive language towards three conversational AI systems gathered ‘in the wild’. Our ConvAI dataset reflects fine-grained notions of abuse, as well as views from multiple expert annotators, identifying substantial differences in the distribution of abuse compared to other commonly used datasets.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/amandacurry/convabuse)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research into nuanced abuse detection in conversational AI and improve detection models by providing a detailed dataset and analysis.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Abusive Language Detection

**Limitations**: N/A

## 💾 Data

**Source**: Collected from conversations with three different conversational AI systems: Alana v2, CarbonBot, and ELIZA.

**Size**: 20,710 ratings on 6,837 examples

**Format**: N/A

**Annotation**: Annotated with a detailed scheme by expert annotators focusing on different types of abuse.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: Calculated using aggregated labels based on the majority vote of annotators.

**Interpretation**: Higher F1 scores indicate better performance in detecting abusive language.

**Validation**: The dataset was validated through multiple iterations of annotation and adjustment based on expert feedback.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The dataset includes responses from diverse demographic backgrounds although not explicitly stated in the details.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data collected followed GDPR guidelines with implied consent.

**Data Licensing**: Not Applicable

**Consent Procedures**: Data collection followed institutional ethics approval.

**Compliance With Regulations**: Complied with GDPR requirements.
