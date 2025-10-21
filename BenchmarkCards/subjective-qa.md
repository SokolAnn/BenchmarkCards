# SubjECTive-QA

## 📊 Benchmark Details

**Name**: SubjECTive-QA

**Overview**: SubjECTive-QA is a human annotated dataset on Earnings Call Transcripts’ QA sessions, focusing on subjective features such as assertiveness, cautiousness, optimism, specificity, clarity, and relevance.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/gtfintechlab/SubjECTive-QA)
- [Resource](https://huggingface.co/datasets/gtfintechlab/SubjECTive-QA)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive resource for analyzing subjectivity in QA responses during Earnings Calls, and to aid in detecting misinformation across various domains.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The dataset is limited to Earnings Calls of companies listed on the New York Stock Exchange from 2007 to 2021.

## 💾 Data

**Source**: Earnings Call Transcripts collected from company websites and related resources.

**Size**: 35,711 annotations

**Format**: CSV

**Annotation**: Manual annotation by a team of annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Weighted F1 Score

**Calculation**: F1 scores were calculated based on model predictions against the annotated features.

**Interpretation**: Higher F1 scores indicate better model performance in capturing the specified subjective features.

**Baseline Results**: RoBERTa-base had the highest average weighted F1 score of 63.95%.

**Validation**: Models were validated using a subset of QA pairs from White House Press Briefings and Gaggles.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Output bias

**Demographic Analysis**: Annotator demographics may introduce biases related to educational background and gender.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution 4.0 International (CC BY 4.0)

**Consent Procedures**: Consent was obtained from annotators as they are the authors of the paper.

**Compliance With Regulations**: Not Applicable
