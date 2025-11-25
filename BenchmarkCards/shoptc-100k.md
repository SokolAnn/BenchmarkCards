# ShopTC-100K

## 📊 Benchmark Details

**Name**: ShopTC-100K

**Overview**: ShopTC-100K is a dataset of terms and conditions from shopping websites in the Tranco top 100K list, comprising 1.8 million terms from 8,251 websites. It helps systematically identify and categorize unfavorable financial terms.

**Data Type**: text

**Domains**:
- Consumer Protection

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/eltsai/ShopTC-100K)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to provide a comprehensive dataset for identifying unfavorable financial terms on shopping websites to enhance consumer protection.

**Target Audience**:
- Researchers
- Consumer Protection Advocates
- Legal Analysts

**Tasks**:
- Text Classification

**Limitations**: The dataset focuses on unfavorable financial terms but does not exhaustively cover all potential deceptive practices.

## 💾 Data

**Source**: Terms and conditions collected from 8,251 shopping websites in the Tranco top 100K list.

**Size**: 1.8 million terms

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated data collection
- Topic modeling
- Large Language Model classification

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: F1 score was calculated based on the identification of unfavorable financial terms using a fine-tuned GPT-4o model.

**Interpretation**: An F1 score of 94.6% indicates high performance in detecting unfavorable terms.

**Baseline Results**: Fine-tuned GPT-4o achieved 94.6% F1 score and 2.3% false positive rate.

**Validation**: The dataset underwent validation through manual annotation and testing of the detection system accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution 4.0 International License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
