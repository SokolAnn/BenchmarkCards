# DRIVING VQA

## 📊 Benchmark Details

**Name**: DRIVING VQA

**Overview**: DRIVING VQA is a visual question answering dataset derived from driving theory exams, containing 3,931 multiple-choice problems with expert-written explanations and grounded entities relevant to the reasoning process.

**Data Type**: multiple-choice questions with visual context

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- French

**Similar Benchmarks**:
- A-OKVQA
- PuzzleQA
- ScienceQA

**Resources**:
- [Resource](https://vita-epfl.github.io/DrivingVQA)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark and enhance the visual reasoning capabilities of vision-language models in real-world driving scenarios.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Derived from publicly available French driving theory exams.

**Size**: 3,931 samples

**Format**: JSON

**Annotation**: Expert-written explanations and human annotations of relevant entities with bounding box coordinates.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Exact match ratio
- F1 Score

**Calculation**: Performance is measured with the exam score, analogous to the real driving theory score used to evaluate candidates.

**Interpretation**: A higher score indicates better performance in correctly answering questions based on visual reasoning.

**Validation**: Inter-annotator agreement achieved a score of 0.95.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data used is derived from publicly available sources and anonymization measures are employed during the data collection process.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
