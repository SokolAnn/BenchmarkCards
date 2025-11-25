# ITDR (Instruction Tuning Dataset for Recommendations)

## 📊 Benchmark Details

**Name**: ITDR (Instruction Tuning Dataset for Recommendations)

**Overview**: ITDR is a dataset constructed to enhance the performance of large language models in recommendation systems by providing a comprehensive instruction tuning dataset that includes various user-item interaction and understanding tasks.

**Data Type**: instruction pairs

**Domains**:
- Natural Language Processing
- Recommender Systems

**Languages**:
- English

**Similar Benchmarks**:
- MovieLens
- Amazon Reviews

**Resources**:
- [GitHub Repository](https://github.com/hellolzk/ITDR)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale instruction tuning dataset for enhancing the recommendation capabilities of large language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Rating Prediction
- Top-K Recommendation
- Cross-Domain Recommendation
- Next Item Recommendation
- User Attribute Prediction
- Interest Recognition
- Target User Identification

**Limitations**: The dataset may not include all possible recommendation tasks and could further benefit from more diverse data incorporation.

## 💾 Data

**Source**: Integrated data from 13 public recommendation datasets.

**Size**: 200,000 instances

**Format**: N/A

**Annotation**: Manually crafted standardized templates.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Root Mean Squared Error (RMSE)
- Accuracy (ACC)
- N@10
- Hit Ratio (H@1)
- Precision (P@5)
- BLEU-1
- ROUGE-1

**Calculation**: Evaluation metrics are calculated based on the predicted outputs compared to the ground truth.

**Interpretation**: Higher accuracy and lower RMSE indicate better model performance.

**Baseline Results**: Results demonstrate performance improvements for models fine-tuned on ITDR compared to those not fine-tuned.

**Validation**: Ablation studies conducted to validate the effectiveness of ITDR in multiple recommendation tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset has undergone various privacy measures during data collection.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
