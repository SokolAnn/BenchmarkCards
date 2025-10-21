# Intent Detection and Slot Filling for Home Assistants: Dataset and Analysis for Bangla and Sylheti

## 📊 Benchmark Details

**Name**: Intent Detection and Slot Filling for Home Assistants: Dataset and Analysis for Bangla and Sylheti

**Overview**: This paper introduces the first-ever comprehensive dataset for intent detection and slot filling in formal Bangla, colloquial Bangla, and Sylheti languages, totaling 984 samples across 10 unique intents.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Bangla
- Sylheti

**Resources**:
- [GitHub Repository](https://github.com/mushfiqur11/bangla-sylheti-snips.git)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality benchmark dataset for intent detection and slot filling that caters to the linguistic nuances of Bangla and Sylheti.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Intent Detection
- Slot Filling

**Limitations**: The dataset is smaller compared to established benchmarks, limiting its generalizability.

## 💾 Data

**Source**: Manually curated dataset inspired by the SNIPS dataset.

**Size**: 984 samples

**Format**: N/A

**Annotation**: Manual annotation by a team of annotators fluent in Bangla and Sylheti.

## 🔬 Methodology

**Methods**:
- Evaluation with Large Language Models (GPT-3.5, JointBERT)

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Calculating F1 scores for intent detection and slot filling tasks.

**Interpretation**: F1 scores represent the harmonic mean of precision and recall, indicating model performance.

**Baseline Results**: GPT-3.5 achieved an F1 score of 0.94 in intent detection and 0.51 in slot filling for colloquial Bangla.

**Validation**: Evaluated using an 80-10-10 split for training, development, and testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
