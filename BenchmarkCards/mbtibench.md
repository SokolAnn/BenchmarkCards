# MBTIBENCH

## 📊 Benchmark Details

**Name**: MBTIBENCH

**Overview**: MBTIBENCH is the first manually annotated high-quality MBTI personality detection dataset with soft labels, constructed to address incorrect labeling issues in existing datasets and to better align with population traits.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/Personality-NLP/MbtiBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality dataset for MBTI personality detection that aligns better with actual population traits by implementing soft labeling techniques.

**Target Audience**:
- ML Researchers
- Psychologists
- Data Scientists

**Tasks**:
- Personality Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Re-analyzed existing datasets (Twitter, Kaggle, and PANDORA) with new manual annotations under psychological expert guidance.

**Size**: N/A

**Format**: N/A

**Annotation**: Manually annotated under guidance from psychology PhD students, following newly established annotation guidelines.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- RMSE
- MAE

**Calculation**: Root Mean Square Error (RMSE) and Mean Absolute Error (MAE) calculated between predicted soft labels and the annotated labels.

**Interpretation**: Lower scores indicate better model performance in predicting personality traits.

**Baseline Results**: N/A

**Validation**: Validation included multiple rounds of trial annotations to ensure consistency and reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The study does not collect personal data from users; it relies on publicly available datasets.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
