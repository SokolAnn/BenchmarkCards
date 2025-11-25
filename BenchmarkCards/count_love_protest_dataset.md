# Count Love Protest Dataset

## 📊 Benchmark Details

**Name**: Count Love Protest Dataset

**Overview**: The dataset documents 42,347 protest events reported in local news sources in the United States between January 2017 and January 2021, including metadata such as dates, locations, crowd size estimates, and descriptive tags.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/count-love/protest-data)

## 🎯 Purpose and Intended Users

**Goal**: To provide structured data for understanding temporal and geographic trends in protest events reported in news articles.

**Target Audience**:
- Researchers
- Journalists
- Policymakers
- Activists

**Tasks**:
- Event Extraction
- Data Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Manual labeling and semi-automated crawling of news articles from 3,410 news sources in the United States.

**Size**: 138,826 URLs

**Format**: N/A

**Annotation**: Manual annotation by researchers

## 🔬 Methodology

**Methods**:
- Crawling
- Manual Review
- LSTM Classifier

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated based on predictions of the classifier compared to manually labeled data.

**Interpretation**: Higher precision and recall indicate better performance in identifying protest events from news articles.

**Baseline Results**: Not specified

**Validation**: Dataset split into training (70%), validation (15%), and testing (15%) sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
