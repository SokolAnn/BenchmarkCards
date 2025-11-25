# ChartGaze

## 📊 Benchmark Details

**Name**: ChartGaze

**Overview**: ChartGaze is a new eye-tracking dataset that captures human gaze patterns during chart reasoning tasks, designed to improve attention alignment in Large Vision-Language Models (LVLMs) and enhance interpretability and accuracy of chart Question Answering (CQA).

**Data Type**: attention maps

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- ChartQA
- VisText

**Resources**:
- [GitHub Repository](https://github.com/user/repo)
- [Resource](https://huggingface.co/datasets/chartgaze)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for improving attention alignment in LVLMs used for chart understanding, thereby enhancing model interpretability and accuracy.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Chart Question Answering

**Limitations**: The study focuses on Yes/No questions and relatively simple chart types, which may limit generalizability to more complex visualizations and open-ended questions.

## 💾 Data

**Source**: Constructed from chart images sourced from ChartQA and VisText datasets, combined with human gaze data collected during chart reasoning tasks.

**Size**: 4,638 attention maps from 1,620 unique chart images

**Format**: JSON

**Annotation**: Eye-tracking data captured using Tobii Pro Fusion for detailed human gaze mapping during the task.

## 🔬 Methodology

**Methods**:
- Gaze-guided attention refinement
- Human evaluation of attention alignment

**Metrics**:
- Accuracy
- Pearson's Correlation Coefficient (CC)
- Kullback–Leibler (KL) divergence
- Histogram intersection (SIM)

**Calculation**: Metrics calculated based on the alignment of model-derived attention maps with human gaze data and the percentage of questions answered correctly.

**Interpretation**: Higher scores in CC and SIM indicate better alignment of model attention with human gaze and higher accuracy reflects improved understanding.

**Baseline Results**: LVLMs fine-tuned with gaze-guided attention refinement improved accuracy by up to 2.56 percentage points over those trained with language loss alone.

**Validation**: The dataset was validated through human annotation and gaze data quality controls including filtering for accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Data privacy rights alignment
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Demographics of participants involved in the eye-tracking data collection were balanced across gender and academic fields.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All collected gaze data were de-identified and securely stored on encrypted devices to protect participant privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants provided informed consent and were compensated for their participation.

**Compliance With Regulations**: The study was reviewed and approved by the University of British Columbia behavioural research ethics board.
