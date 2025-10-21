# Guesstimation Datasets: MARBLES, FUTURE, ELECPRED

## 📊 Benchmark Details

**Name**: Guesstimation Datasets: MARBLES, FUTURE, ELECPRED

**Overview**: The paper introduces three datasets for guesstimation tasks: MARBLES, which involves physical estimation of objects, FUTURE for predicting future events, and ELECPRED focused on predicting U.S. presidential election outcomes.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To assess the capabilities of large language models in guesstimation tasks and demonstrate the effectiveness of wisdom of crowds decoding.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Guesstimation

**Limitations**: The scope of the guesstimation questions is U.S.-centric.

## 💾 Data

**Source**: Three guesstimation datasets created for evaluation: MARBLES, FUTURE, and ELECPRED.

**Size**: 15 guesstimation questions for MARBLES, 15 questions for FUTURE, 51 questions for ELECPRED.

**Format**: N/A

**Annotation**: Questions were created based on manual measurements or credible information sources.

## 🔬 Methodology

**Methods**:
- Wisdom of Crowds Decoding
- Self-Consistency Decoding
- Greedy Decoding
- Mean Baseline Decoding

**Metrics**:
- Normalized Error

**Calculation**: Normalized error is calculated as the absolute difference between the median estimate and the ground truth divided by the ground truth.

**Interpretation**: Lower normalized error indicates greater accuracy in guesstimation.

**Baseline Results**: N/A

**Validation**: Performance comparison across different guesstimation strategies via statistical tests.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Human experiment approved by the Institutional Review Board.

**Compliance With Regulations**: Not Applicable
