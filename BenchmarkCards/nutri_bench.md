# NUTRI BENCH

## 📊 Benchmark Details

**Name**: NUTRI BENCH

**Overview**: NUTRI BENCH is the first publicly available natural language meal description nutrition benchmark consisting of 11,857 human-verified meal descriptions annotated with macronutrient labels, including carbohydrates, proteins, fats, and calories.

**Data Type**: natural language meal descriptions

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://mehak126.github.io/nutribench.html)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of large language models (LLMs) on nutrition estimation from natural language meal descriptions.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Nutritionists

**Tasks**:
- Nutrition Estimation

**Limitations**: N/A

## 💾 Data

**Source**: Derived from real-world dietary intake data from the What We Eat in America survey and FAO/WHO GIFT.

**Size**: 11,857 meal descriptions

**Format**: N/A

**Annotation**: Human-verified and annotated with macro-nutrient labels.

## 🔬 Methodology

**Methods**:
- Evaluation of Large Language Models (LLMs)
- Human Evaluation

**Metrics**:
- Accuracy
- Mean Absolute Error (MAE)

**Calculation**: Mean Absolute Error is calculated based on the deviation of the model responses from the true meal carbohydrates.

**Interpretation**: A lower MAE indicates better performance in correctly estimating carbohydrates from meal descriptions.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
