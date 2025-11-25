# FinGen: A Dataset for Argument Generation in Finance

## 📊 Benchmark Details

**Name**: FinGen: A Dataset for Argument Generation in Finance

**Overview**: FinGen introduces three tasks centered on forward-looking argument generation in finance: Evidence2Claim, Chart2Argument, and News2Argument.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- English
- Chinese

**Resources**:
- [Resource](https://arxiv.org/abs/2405.20708)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the generation of forward-looking arguments in the financial sector.

**Target Audience**:
- ML Researchers
- Financial Analysts

**Tasks**:
- Evidence2Claim
- Chart2Argument
- News2Argument

**Limitations**: The dataset sizes for Chart2Argument and News2Argument are small and do not cover multilingual data from the same source.

## 💾 Data

**Source**: Collected earnings conference calls, trading blogs, and professional analyst reports.

**Size**: 44,924 instances

**Format**: CSV

**Annotation**: Manually annotated with forward-looking claims and arguments.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- ROUGE
- BERT Score

**Calculation**: Metrics are calculated comparing model outputs to human-generated references.

**Interpretation**: Higher scores indicate better alignment with human-like forward-looking claims.

**Validation**: Used a training-evaluation split of 80-20 for instance selection.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset includes both English and Chinese texts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
