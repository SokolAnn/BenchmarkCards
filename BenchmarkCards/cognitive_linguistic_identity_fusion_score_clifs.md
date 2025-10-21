# Cognitive Linguistic Identity Fusion Score (CLIFS)

## 📊 Benchmark Details

**Name**: Cognitive Linguistic Identity Fusion Score (CLIFS)

**Overview**: The CLIFS is a metric that quantifies identity fusion—the psychological merging of an individual's identity with another entity—from natural language text. It utilizes large language models for automated, scalable assessments and has been validated against established measures.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Cognitive Science

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/DevinW-sudo/CLIFS)

## 🎯 Purpose and Intended Users

**Goal**: To provide a scalable, quantitative measure of identity fusion for research and applications in understanding group dynamics and behaviors.

**Target Audience**:
- ML Researchers
- Cognitive Scientists
- Social Psychologists

**Tasks**:
- Identity Fusion Prediction
- Violence Risk Prediction

**Limitations**: Limited to texts in English and the specific contexts of identity fusion explored; may not generalize across diverse cultural settings.

## 💾 Data

**Source**: Combination of datasets repurposed for identity fusion and violence risk prediction tasks.

**Size**: 1,971 samples

**Format**: JSON

**Annotation**: Annotated based on Verbal Identity Fusion Scale (VIFS) scores and additional metrics derived from prior studies.

## 🔬 Methodology

**Methods**:
- Random Forest
- Support Vector Machine
- XGBoost
- Fine-Tuning Language Models

**Metrics**:
- F1 Score
- Mean Absolute Error (MAE)
- Spearman Correlation (rs)

**Calculation**: Calculated using specified models with hyperparameter tuning and evaluation metrics such as F1 scores and MAE.

**Interpretation**: Higher F1 scores and lower MAE indicate better model performance in predicting identity fusion and associated risks.

**Baseline Results**: CLIFS models exhibited a 6-154% improvement over existing methods in classification tasks.

**Validation**: Validated against human annotations and established scoring scales.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Future work will explore demographic factors in identity fusion among various groups.

**Potential Harm**: ['There are potential risks if the metric is misused in high-stakes contexts.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data anonymization techniques were applied to comply with ethical guidelines.

**Data Licensing**: The data is shared under a CC BY 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
