# ArCOV19- Rumors

## 📊 Benchmark Details

**Name**: ArCOV19- Rumors

**Overview**: ArCOV19- Rumors is an Arabic COVID-19 Twitter dataset for misinformation detection comprising tweets from January 27th to April 2020, including 138 verified claims and 9.4K annotated tweets for both claim-level and tweet-level verification tasks.

**Data Type**: tweets

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic

**Similar Benchmarks**:
- ArCOV-19

**Resources**:
- [Resource](https://gitlab.com/bigirqu/ArCOV-19/-/tree/master/ArCOV19-Rumorstweets)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research on misinformation detection on social media during the COVID-19 pandemic through a manually-annotated Arabic dataset.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Claim Verification
- Tweet Verification

**Limitations**: N/A

## 💾 Data

**Source**: Tweets collected from Twitter containing claims related to COVID-19.

**Size**: 9,414 tweets

**Format**: N/A

**Annotation**: Manual annotation for tweets to determine veracity.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated according to standard practices in classification tasks.

**Interpretation**: Accuracy measures the correctness of predictions; F1 Score balances precision and recall.

**Baseline Results**: Bi-GCN model achieved 0.669 accuracy, MARBERT achieved 0.757 accuracy.

**Validation**: Data was split into folds for cross-validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
