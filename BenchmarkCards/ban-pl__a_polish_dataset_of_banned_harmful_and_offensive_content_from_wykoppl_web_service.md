# BAN-PL: a Polish Dataset of Banned Harmful and Offensive Content from Wykop.pl web service

## 📊 Benchmark Details

**Name**: BAN-PL: a Polish Dataset of Banned Harmful and Offensive Content from Wykop.pl web service

**Overview**: The paper presents a new open dataset of offensive social media content for the Polish language, titled BAN-PL, which consists of content from Wykop.pl that was reported by users and banned in the internal moderation process. The dataset includes a total of 691,662 posts and comments, evenly divided into harmful and neutral categories.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Polish

**Similar Benchmarks**:
- KLEJ

**Resources**:
- [GitHub Repository](https://github.com/ZILiAT-NASK/BAN-PL)

## 🎯 Purpose and Intended Users

**Goal**: To provide a publicly available dataset for training models in automated online content moderation for offensive language detection in the Polish language.

**Target Audience**:
- NLP Researchers
- Content Moderation Practitioners

**Tasks**:
- Offensive Language Detection
- Hate Speech Detection

**Limitations**: N/A

## 💾 Data

**Source**: Wykop.pl web service

**Size**: 691,662 posts and comments

**Format**: N/A

**Annotation**: Content labeled and moderated by professional moderators based on community reports.

## 🔬 Methodology

**Methods**:
- Moderation review
- Annotation by professionals

**Metrics**:
- F1 Score

**Calculation**: The F1 Score is calculated to evaluate the performance of models trained on the dataset.

**Interpretation**: A higher F1 Score indicates better performance in detecting harmful content.

**Baseline Results**: F1 score = 0.92 achieved in preliminary experiments applying models on the dataset.

**Validation**: Dataset undergoes continuous moderation and review by trained moderators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Comprehensive anonymization procedures applied to protect personal data in accordance with ethical guidelines.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
