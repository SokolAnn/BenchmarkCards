# PodSarc (Podcast Sarcasm)

## 📊 Benchmark Details

**Name**: PodSarc (Podcast Sarcasm)

**Overview**: PodSarc is a large-scale sarcastic speech dataset created using an annotation pipeline that leverages large language models (LLMs) for sarcasm detection in speech.

**Data Type**: speech-transcript pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MUStARD
- MUStARD++

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale annotated dataset for sarcasm detection in speech, enabling the development of models that can accurately identify sarcastic intent without visual context.

**Target Audience**:
- ML Researchers
- Speech Technology Developers

**Tasks**:
- Sarcasm Detection

**Limitations**: Although the dataset reduces manual annotation effort, some discrepancies may still exist in the annotations.

## 💾 Data

**Source**: Overly Sarcastic Podcast (OSPod)

**Size**: 11,024 segments

**Format**: N/A

**Annotation**: LLM-based annotations followed by human verification

## 🔬 Methodology

**Methods**:
- LLM annotation
- Human verification

**Metrics**:
- F1 Score

**Calculation**: F1 Score calculated based on model predictions and ground truth labels.

**Interpretation**: Higher F1 scores indicate better performance in sarcasm detection.

**Baseline Results**: Achieved an F1 score of 73.63% using human-verified LLM annotations.

**Validation**: Compared annotation quality and detection performance using the MUStARD++ dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
