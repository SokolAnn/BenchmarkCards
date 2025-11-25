# KuaiComt

## 📊 Benchmark Details

**Name**: KuaiComt

**Overview**: KuaiComt is a real-world dataset constructed to study staytime prediction in the comments section of micro-videos. It includes comprehensive user interaction data with both videos and comments, as well as rich textual information associated with these videos and comments.

**Data Type**: user interaction data with videos and comments

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/lyingCS/KuaiComt.github.io)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of KuaiComt is to serve as a benchmark for predicting user staytime in the comments section of videos on short-video platforms.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Staytime Prediction

**Limitations**: N/A

## 💾 Data

**Source**: User interaction logs collected from the Kuaishou app.

**Size**: 16,352,904 comments

**Format**: N/A

**Annotation**: Data includes user interactions (likes and replies) with comments.

## 🔬 Methodology

**Methods**:
- Fine-tuning large language models
- Empirical analysis

**Metrics**:
- Root Mean Square Error (RMSE)
- Mean Absolute Error (MAE)
- GAUC
- NDCG

**Calculation**: Metrics calculated based on the actual staytime compared to model predictions.

**Interpretation**: Lower RMSE and MAE indicate better performance in predicting user staytime.

**Baseline Results**: The dataset has been evaluated against various base models including VR, WLR, and D2Q.

**Validation**: The dataset's effectiveness was validated through extensive experiments and online A/B testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data has been anonymized to protect user privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
