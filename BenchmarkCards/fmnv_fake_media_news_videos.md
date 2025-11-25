# FMNV (Fake Media News Videos)

## 📊 Benchmark Details

**Name**: FMNV (Fake Media News Videos)

**Overview**: FMNV is a dataset of 2,393 professionally produced news videos sourced from verified YouTube and Twitter accounts, aimed at addressing the gap in the detection of multimodal fake news videos and providing a basis for robust fake news detection systems.

**Data Type**: video

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- FakeSV
- FakeTT

**Resources**:
- [GitHub Repository](https://github.com/DennisIW/FMNV)

## 🎯 Purpose and Intended Users

**Goal**: To construct a dataset of media-published news videos for effective fake news detection and to establish benchmarks for the methodologies involved in detecting high-impact fake news.

**Target Audience**:
- Researchers
- Developers

**Tasks**:
- Fake News Detection

**Limitations**: N/A

## 💾 Data

**Source**: Collected from verified YouTube and Twitter accounts of news media organizations.

**Size**: 2,393 videos

**Format**: N/A

**Annotation**: Manual review and LLM-assisted modification for the generation of fake news videos.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated based on the classification performance of models tested on FMNV.

**Interpretation**: Higher scores in accuracy, F1, precision, and recall indicate better performance in detecting fake news.

**Baseline Results**: FMNVD achieved an accuracy of 74.17 on the dataset.

**Validation**: Models were validated through comparative experiments with established baselines.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
