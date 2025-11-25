# ACETADA (A Comprehensive Evaluation of Nutrition via Advanced Dietary Assessment)

## 📊 Benchmark Details

**Name**: ACETADA (A Comprehensive Evaluation of Nutrition via Advanced Dietary Assessment)

**Overview**: This study introduces ACETADA, the first publicly available food-image dataset that pairs dietitian-verified nutrition labels with GPS coordinates, timestamps, and ground-truth food lists.

**Data Type**: meal images with nutrition information

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2507.07048)

## 🎯 Purpose and Intended Users

**Goal**: The goal is to provide an open dataset to improve nutrition analysis through the integration of contextual metadata with meal images.

**Target Audience**:
- ML Researchers
- Nutritionists
- Dietitians

**Tasks**:
- Nutritional analysis
- Image-based dietary assessment

**Limitations**: N/A

## 💾 Data

**Source**: ACETADA dietary study conducted with 152 adults to collect meal images and nutrition data.

**Size**: 806 images

**Format**: N/A

**Annotation**: Nutrition information verified by dietitians.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Mean Absolute Error (MAE)
- Mean Absolute Percentage Error (MAPE)

**Calculation**: MAE is calculated as the average of absolute deviations from dietitian-verified values.

**Interpretation**: Lower MAE and MAPE indicate improved accuracy in estimating nutritional values.

**Baseline Results**: N/A

**Validation**: Empirical results show integration of contextual metadata reduces MAE and MAPE.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The dataset includes demographic information about participants.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Consent was obtained from participants in the dietary study.

**Compliance With Regulations**: Not Applicable
