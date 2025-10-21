# BanglaBait: Semi-Supervised Adversarial Approach for Clickbait Detection on Bangla Clickbait Dataset

## 📊 Benchmark Details

**Name**: BanglaBait: Semi-Supervised Adversarial Approach for Clickbait Detection on Bangla Clickbait Dataset

**Overview**: This paper presents the first Bangla Clickbait dataset created for detecting clickbait titles in Bangla articles, containing 15,056 labeled and 65,406 unlabeled articles, and uses Semi-Supervised Generative Adversarial Networks (SS-GANs) to improve clickbait detection.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Bengali

**Similar Benchmarks**:
- Webis Clickbait Corpus 2017

**Resources**:
- [GitHub Repository](https://github.com/mdmotaharmahtab/BanglaBait)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset and a model for clickbait detection specifically for Bangla articles, enabling further research in this area.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Clickbait-dense news sites and own dataset compilation.

**Size**: 15,056 labeled articles, 65,406 unlabeled articles

**Format**: N/A

**Annotation**: Annotated by three expert linguists based on a majority vote.

## 🔬 Methodology

**Methods**:
- Semi-Supervised Generative Adversarial Networks

**Metrics**:
- F1 Score
- Precision
- Recall
- Accuracy

**Calculation**: Standard classification metrics are calculated based on predictions of the model.

**Interpretation**: Higher F1 Score indicates better performance in distinguishing clickbait from non-clickbait articles.

**Baseline Results**: Human Baseline: F1 Score of 76.81%

**Validation**: Cross-validation with test set curated.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
