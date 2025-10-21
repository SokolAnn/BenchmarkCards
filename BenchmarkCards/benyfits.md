# BeNYfits

## 📊 Benchmark Details

**Name**: BeNYfits

**Overview**: BeNYfits is a benchmark for determining user eligibility for multiple overlapping social benefits opportunities through interactive decision-making.

**Data Type**: dialog interaction data

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/mtoles/BeNYfits-ProADA)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate agent performance in determining user eligibility for public benefits using an interactive dialog system.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- User Eligibility Determination

**Limitations**: The eligibility requirements for this benchmark were derived from plain English summaries rather than official documents.

## 💾 Data

**Source**: NYC Open Data

**Size**: 10,000 simulated users

**Format**: Structured dialog data

**Annotation**: Manually curated eligibility requirements minimally edited to remove ambiguity.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: The F1 score is calculated based on model predictions versus ground truth eligibility.

**Interpretation**: Higher F1 scores indicate better model performance in determining eligibility with fewer dialog turns.

**Baseline Results**: Current language models score significantly lower, with GPT-4o achieving 35.7 F1, while ProADA achieves 55.6 F1.

**Validation**: ProADA’s performance is evaluated against simulated user interactions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The datasets are constructed to ensure a diverse representation of user features.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
