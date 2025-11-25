# SocialDF (Benchmark Dataset and Detection Model for Mitigating Harmful Deepfake Content on Social Media Platforms)

## 📊 Benchmark Details

**Name**: SocialDF (Benchmark Dataset and Detection Model for Mitigating Harmful Deepfake Content on Social Media Platforms)

**Overview**: SocialDF is a curated dataset reflecting real-world deepfake challenges on social media platforms, encompassing high-fidelity deepfakes sourced from various online ecosystems. It also proposes a novel LLM-based multi-factor detection approach that integrates facial recognition and automated speech transcription.

**Data Type**: video

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/arnesh2212/SocialDF/tree/main)

## 🎯 Purpose and Intended Users

**Goal**: To enhance deepfake detection, combat misinformation effectively, and contribute to the development of secure and transparent digital media ecosystems.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Social Media Platforms

**Tasks**:
- Deepfake Detection
- Fact Checking

**Limitations**: The focus on celebrities and high-profile individuals may restrict the generalization of detection models to less-public figures.

## 💾 Data

**Source**: Videos sourced from social media platforms, specifically Instagram Reels and Stories.

**Size**: 2,126 videos (1,071 real, 1,055 deepfake)

**Format**: Video

**Annotation**: Annotations were made based on uploader disclosures, comments, and consensus review for label reliability.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on model performance in detecting deepfakes through the proposed framework.

**Interpretation**: Higher accuracy and F1 scores indicate more effective detection of deepfake content.

**Baseline Results**: LipFD achieved an accuracy of 51.24% on the dataset.

**Validation**: Evaluated using a stratified 90/10 train-test split maintaining equal proportions of real and fake videos.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: Acknowledges demographic skew due to platform trends.

**Potential Harm**: The dataset aims to mitigate misinformation and protects individuals from reputational harm.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Content sourced from public social media platforms; no copyrighted content is redistributed.

**Data Licensing**: CC BY-NC 4.0 license, ensuring use only for non-commercial, ethically sound purposes.

**Consent Procedures**: Videos were selected based on uploader intent and public availability; no private individuals involved.

**Compliance With Regulations**: Aligned with practices of fair use in U.S. Code (2023).
