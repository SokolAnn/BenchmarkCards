# TRIALQA

## 📊 Benchmark Details

**Name**: TRIALQA

**Overview**: TRIALQA is a novel dataset comprising two social media collections from the subreddits on colon cancer and prostate cancer, designed specifically to evaluate the ability of LLMs to identify potential clinical trial participants from social media posts.

**Data Type**: social media posts

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the use of large language models for efficiently recruiting clinical trial participants via social media by evaluating their ability to align user posts with trial eligibility criteria.

**Target Audience**:
- ML Researchers
- Clinical Researchers
- Healthcare Professionals

**Tasks**:
- Classification of eligibility criteria
- Identification of interest reasons

**Limitations**: N/A

## 💾 Data

**Source**: Collected from the r/coloncancer and r/prostatecancer subreddits on Reddit.

**Size**: 1,361 posts from 1,301 Reddit users

**Format**: N/A

**Annotation**: Annotated by experienced annotators based on eligibility criteria and interest reasons.

## 🔬 Methodology

**Methods**:
- Direct LLM inference
- Few-shot prompting
- Chain-of-thought reasoning

**Metrics**:
- Accuracy
- Macro F1 Score
- Weighted F1 Score

**Calculation**: Metrics reflect the proportion of correct predictions made by the LLMs on eligibility criteria and interest reasons.

**Interpretation**: Higher scores indicate better performance in identifying eligible clinical trial participants based on user-generated content.

**Baseline Results**: Comparison with RoBERTa and various LLM architectures to assess performance.

**Validation**: Performance evaluated on the TRIALQA dataset using various LLM architectures.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
