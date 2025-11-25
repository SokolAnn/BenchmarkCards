# WiserUI-Bench (Pairwise UI/UX Design Understanding Benchmark)

## 📊 Benchmark Details

**Name**: WiserUI-Bench (Pairwise UI/UX Design Understanding Benchmark)

**Overview**: WiserUI-Bench is a novel benchmark for assessing models’ multimodal understanding of UI/UX design, featuring 300 real-world UI image pairs along with expert-curated rationales to evaluate models' effectiveness in predicting user engagement and explaining design choices.

**Data Type**: image pairs with expert rationales

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/jeochris/wiserui-bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate multimodal understanding of how UI/UX design influences user behavior and decision-making.

**Target Audience**:
- ML Researchers
- UI/UX Designers
- Industry Practitioners

**Tasks**:
- UI/UX Design Selection
- UI/UX Design Rationale Alignment

**Limitations**: N/A

## 💾 Data

**Source**: 300 UI image pairs sourced from industry-validated A/B testing data, collected from widely recognized testing platforms.

**Size**: 300 pairs

**Format**: Image pairs

**Annotation**: Expert-curated rationales created by UI/UX professionals through a multi-stage review process.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Model performance is calculated based on selecting the correct UI/UX design that drives user behavior.

**Interpretation**: Performance indicates the model's ability to reason about design effectiveness based on user behavior indicators.

**Baseline Results**: N/A

**Validation**: The benchmark is validated against real-world A/B testing data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data was used under ethical guidelines, ensuring anonymization of participants and expert annotations.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent was obtained from all expert annotators and survey participants.

**Compliance With Regulations**: Not Applicable
