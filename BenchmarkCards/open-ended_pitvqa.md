# Open-Ended PitVQA

## 📊 Benchmark Details

**Name**: Open-Ended PitVQA

**Overview**: A specialized open-ended VQA dataset for endonasal pituitary surgery, capturing intraoperative decisions, procedural steps, and instrument interactions, comprising 101,803 frames and 745,972 question-answer pairs.

**Data Type**: question-answer pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- EndoVis18-VQA

**Resources**:
- [GitHub Repository](https://github.com/HRL-Mike/PitVQA-Plus)

## 🎯 Purpose and Intended Users

**Goal**: To advance visual question answering capabilities in endonasal pituitary surgery by providing a comprehensive dataset and innovative adaptation methodology.

**Target Audience**:
- ML Researchers
- Medical Professionals

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: 25 procedural videos of endoscopic pituitary surgery recorded at the National Hospital of Neurology and Neurosurgery in London, UK.

**Size**: 101,803 frames, 745,972 question-answer pairs

**Format**: MP4

**Annotation**: Annotated by experienced neurosurgery residents with validation by an attending neurosurgeon.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU Score
- ROUGE-L
- METEOR

**Calculation**: Metrics are calculated as the average scores on generated responses compared to reference answers.

**Interpretation**: Higher scores indicate better performance in generating contextually relevant and precise answers.

**Baseline Results**: Compared against state-of-the-art VQA models like VisualBert and MoRA.

**Validation**: Performance validated on both Open-Ended PitVQA and EndoVis18-VQA datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Patient informed consent obtained and local governance committee approval received.

**Compliance With Regulations**: Not Applicable
