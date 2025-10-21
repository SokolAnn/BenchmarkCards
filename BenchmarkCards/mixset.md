# MIXSET

## 📊 Benchmark Details

**Name**: MIXSET

**Overview**: MIXSET is the first dataset dedicated to studying mixed text scenarios, which involve both AI-generated and human-written content, addressing gaps in existing research on the detection of mixed scenarios.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Dongping-Chen/MixSet)

## 🎯 Purpose and Intended Users

**Goal**: To analyze and evaluate the performance of mainstream MGT detectors on mixed text scenarios.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Classification
- Machine Generated Text Detection

**Limitations**: The dataset's overall scale is relatively small which could limit the comprehensiveness of model training and evaluation.

## 💾 Data

**Source**: Generated from a combination of existing datasets featuring Human Written Text (HWT) and Machine Generated Text (MGT).

**Size**: 3,600 mixtext instances

**Format**: JSON

**Annotation**: Annotated by human experts for quality and consistency.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- AUC

**Calculation**: Metrics calculated based on the classification performance of detectors on the MIXSET dataset.

**Interpretation**: F1 Score and AUC are used to assess the efficacy of the detection methods.

**Baseline Results**: Radar performed best, achieving high F1 Scores and AUC metrics across different detector models.

**Validation**: Tested with zero-shot and retraining scenarios on various MGT detectors.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: The dataset may introduce biases from human annotation and its limited size.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data derived from publicly available sources.

**Data Licensing**: Adheres to the licensing terms of original datasets.

**Consent Procedures**: Not applicable, as the data is publicly available.

**Compliance With Regulations**: Not Applicable
