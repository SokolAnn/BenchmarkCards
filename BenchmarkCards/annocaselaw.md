# AnnoCaseLaw

## 📊 Benchmark Details

**Name**: AnnoCaseLaw

**Overview**: AnnoCaseLaw is a dataset of 471 meticulously annotated U.S. Appeals Court negligence cases designed for Legal Judgment Prediction (LJP). It includes expert-labeled annotations that highlight key components of judicial decision making, as well as relevant legal concepts. The dataset aims to improve explainability in LJP models and establish a performance baseline using leading large language models.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/anonymouspolar1/annocaselaw)

## 🎯 Purpose and Intended Users

**Goal**: To enhance reasoning and explanation in legal judgment prediction through a richly annotated dataset.

**Target Audience**:
- ML Researchers
- Legal Practitioners
- Data Scientists

**Tasks**:
- Judgment Prediction
- Concept Identification
- Automated Case Annotation

**Limitations**: The complexity and subjectivity of legal decision-making, the potential for biases in case texts and annotations.

## 💾 Data

**Source**: Caselaw Access Project (CAP), the largest publicly accessible repository of U.S. court decisions.

**Size**: 471 cases

**Format**: JSON

**Annotation**: Manual annotation by legal scholars

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Class-weighted F1 Score

**Calculation**: F1 Score calculated for each task based on model predictions compared to ground truth annotations.

**Interpretation**: Higher F1 Scores indicate better model performance in predicting outcomes and identifying concepts.

**Baseline Results**: F1 Scores ranged from 0.40 to 0.70 across various subtasks.

**Validation**: Performance evaluated through bootstrapping to calculate 95% confidence intervals.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All cases are publicly available; names are maintained as in original sources due to the minimal benefits of anonymization.

**Data Licensing**: MIT License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Legal review conducted to ensure compliance with state and federal laws.
