# CoCoHD (Congress Committee Hearing Dataset)

## 📊 Benchmark Details

**Name**: CoCoHD (Congress Committee Hearing Dataset)

**Overview**: The Congress Committee Hearing Dataset (CoCoHD) is the first and largest open-source dataset of congressional hearings, containing 32,697 curated transcripts and metadata from 1997 to 2024, covering 86 congressional committees, designed to facilitate research and natural language processing applications in analyzing congressional discourses.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/gtfintechlab/CoCoHD)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for analyzing U.S. congressional hearings and their impact on policy language concerning critical issues.

**Target Audience**:
- ML Researchers
- Policymakers
- Political Analysts

**Tasks**:
- Text Classification

**Limitations**: Annotation process complexity and potential biases due to focus on U.S. Congress.

## 💾 Data

**Source**: U.S. Congressional hearings from GovInfo, compiled and curated.

**Size**: 32,697 records

**Format**: JSON

**Annotation**: Manually annotated by authors with relevant and irrelevant labels for exploring sentiments on energy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Model-based evaluation

**Metrics**:
- F1 Score

**Calculation**: Calculated based on the proportion of relevant sentences categorized as supportive or opposing fossil fuel production.

**Interpretation**: Positive values indicate pro-fossil fuel sentiment, while negative values indicate pro-clean energy sentiment.

**Validation**: Case study demonstrating effectiveness in correlating congressional sentiment with market trends.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Bias

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
