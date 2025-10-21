# Big City Bias: Evaluating the Impact of Metropolitan Size on Computational Job Market Abilities of Language Models

## 📊 Benchmark Details

**Name**: Big City Bias: Evaluating the Impact of Metropolitan Size on Computational Job Market Abilities of Language Models

**Overview**: This paper quantifies the metropolitan size bias encoded within large language models by evaluating salary, employer presence, and commute duration predictions in 384 of the United States’ metropolitan regions. The results show that smaller regions are underrepresented, with performance disparities evident across models.

**Data Type**: tabular

**Domains**:
- Natural Language Processing
- Human Resources

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/charlie-campanella/big-city-bias)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and quantify the impact of metropolitan size on the performance of language models in job market predictions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Salary Prediction
- Employer Presence Prediction
- Commute Duration Prediction

**Limitations**: Our research was predominantly U.S.-centric, limiting its applicability to other geographical contexts.

## 💾 Data

**Source**: Data collected from various reputable sources including Indeed.com and People Data Labs.

**Size**: 384 metropolitan areas

**Format**: N/A

**Annotation**: Data sourced from proprietary and public datasets.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Percentage error
- Coefficient of determination (r2)

**Calculation**: Metrics are calculated by comparing the predictions from language models against gold labels for each task.

**Interpretation**: Lower error percentages indicate better model performance; higher r2 values suggest stronger correlation between population size and prediction accuracy.

**Validation**: Validation is conducted through evaluation of predictive accuracy across the 384 metropolitan regions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
