# January Food Benchmark (JFB)

## 📊 Benchmark Details

**Name**: January Food Benchmark (JFB)

**Overview**: The January Food Benchmark (JFB) is a publicly available dataset consisting of 1,000 food images with human-validated annotations for meal names, ingredients, and macronutrients, designed to facilitate automated nutritional analysis and improve evaluation methodologies in AI.

**Data Type**: image

**Domains**:
- Computer Vision
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/January-ai/food-scan-benchmarks)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality, publicly available dataset for benchmarking and evaluating models in automated food analysis.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Meal Identification
- Ingredient Recognition
- Nutritional Estimation

**Limitations**: N/A

## 💾 Data

**Source**: Sourced from users of a mobile health application who consented to data use for research, featuring real-world images logged by users.

**Size**: 1,000 images

**Format**: JSON with image annotations

**Annotation**: Human validation and correction for all annotations including meal name, ingredients, quantities, and macronutrients.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Overall Score
- Precision
- Recall
- F1 Score
- Weighted Mean Absolute Percentage Error (WMAPE)

**Calculation**: Overall Score is calculated using a weighted geometric mean of performance metrics reflecting the application-oriented needs.

**Interpretation**: Higher scores indicate better model performance across the assessed metrics.

**Baseline Results**: january/food-vision-v1 achieved an Overall Score of 86.2.

**Validation**: Rigorous, multi-stage validation process ensures high-quality annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All images were collected with informed consent, and identifying information was removed.

**Data Licensing**: Released under a CC-BY-4.0 license to encourage reproducibility and downstream research.

**Consent Procedures**: Users consented to data use for research as part of the mobile app's Terms of Service.

**Compliance With Regulations**: Not Applicable
