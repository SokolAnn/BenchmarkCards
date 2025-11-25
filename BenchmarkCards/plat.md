# PLAT

## 📊 Benchmark Details

**Name**: PLAT

**Overview**: PLAT is a new benchmark designed to assess the ability of LLMs to predict the legitimacy of additional tax penalties, constructed to evaluate LLMs’ understanding of tax law, particularly in complex cases requiring more than just statute application.

**Data Type**: question-answering pairs

**Domains**:
- Legal

**Languages**:
- Korean
- English

**Resources**:
- [Resource](https://elaw.klri.re.kr/kor_service/lawTwoView.do?hseq=28738)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs’ capability in understanding tax law concerning the legitimacy of additional tax penalties.

**Target Audience**:
- Researchers in Tax Law
- AI/ML Researchers
- Legal Practitioners

**Tasks**:
- Legal Reasoning
- Tax Law Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Derived from 50 questions based on Korean precedents related to additional tax penalties.

**Size**: 50 examples

**Format**: N/A

**Annotation**: Manually evaluated by tax professionals.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: F1 Score is computed as 2*(Precision*Recall)/(Precision + Recall).

**Interpretation**: High F1 Score indicates better performance of LLMs in predicting tax penalty legitimacy.

**Baseline Results**: The strongest commercial model achieved an F1 score of 75%.

**Validation**: Evaluated using six LLMs across various cases.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Societal Impact

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Output bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-NC license will be used for the dataset release.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
