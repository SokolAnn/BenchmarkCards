# M2H2 (Multimodal Multiparty Hindi Humor)

## 📊 Benchmark Details

**Name**: M2H2 (Multimodal Multiparty Hindi Humor)

**Overview**: We propose a dataset for Multimodal Multiparty Hindi Humor recognition in conversations containing 6,191 utterances annotated with humor/non-humor labels, encompassing acoustic, visual, and textual modalities.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Hindi

**Resources**:
- [Resource](http://www.iitp.ac.in/~ai-nlp-ml/resources.html)
- [GitHub Repository](https://github.com/declare-lab/M2H2-dataset)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for humor recognition in Hindi conversations, facilitating research in multimodal and dialogue understanding.

**Target Audience**:
- ML Researchers
- Natural Language Processing Practitioners

**Tasks**:
- Humor Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Samples gathered from the TV show 'Shrimaan Shrimati Phir Se' and manually annotated.

**Size**: 6,191 utterances

**Format**: N/A

**Annotation**: Manually annotated with humor/non-humor labels by experts proficient in Hindi.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: F1 Score calculated based on the standard formula using precision and recall values.

**Interpretation**: Higher precision, recall, and F1 Score indicate better humor recognition performance.

**Baseline Results**: MISA+DialogueRNN: Precision 71.21%, Recall 72.11%, F1 Score 71.67%. MISA+bcLSTM: Precision 69.04%, Recall 69.83%, F1 Score 69.43%.

**Validation**: Five-fold cross-validation was performed for assessing the model performance.

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
