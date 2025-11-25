# Official-NV

## 📊 Benchmark Details

**Name**: Official-NV

**Overview**: Official-NV is a dataset comprised of officially published English news videos for multimodal fake news detection, containing 10,000 videos evenly distributed between 5,000 authentic and 5,000 fabricated videos, enhanced through LLM-based generation and manual verification.

**Data Type**: video

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- COVID-VTS
- FakeNewsNet
- FakeSV
- Liar
- MCFEND

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the Official-NV dataset is to provide a high-quality dataset for effective multimodal fake news detection.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Multimodal Fake News Detection

**Limitations**: N/A

## 💾 Data

**Source**: Videos collected from official news websites such as ChinaNews, CCTV, and Xinhua between 2021 and 2024.

**Size**: 10,000 videos

**Format**: N/A

**Annotation**: Videos were manually verified and labeled as true or fake based on the consistency between titles and video frames.

## 🔬 Methodology

**Methods**:
- Grouped experiments
- Ablation studies
- 5-fold cross-validation

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall

**Calculation**: Metrics were calculated using traditional methods based on model predictions versus ground truth labels.

**Interpretation**: Higher metrics indicate better performance of the model in detecting fake news.

**Validation**: Validation included testing the dataset with existing models and the proposed baseline model OFNVD.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**
- **Fairness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
