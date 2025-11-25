# FEC-Bench

## 📊 Benchmark Details

**Name**: FEC-Bench

**Overview**: FEC-Bench is designed to assess the performance of video Multimodal Large Language Models (MLLMs) in dynamic facial expression captioning tasks using a newly constructed dataset of 5,033 videos and a novel evaluation metric called Temporal Event Matching (TEM).

**Data Type**: video

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Jiaxing-star/FacialDynamic)

## 🎯 Purpose and Intended Users

**Goal**: To improve the ability of video MLLMs to discern and describe dynamic facial expressions in videos.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Dynamic Facial Expression Captioning
- Video Captioning

**Limitations**: N/A

## 💾 Data

**Source**: Self-collected from web scraping and extracted from existing datasets including MAFW, DFEW, AFEW, MER, CAER, FERV39K, and RAVDESS, along with additional video clips from Pexels.

**Size**: 5,033 videos

**Format**: N/A

**Annotation**: Manually annotated by experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- CIDEr
- ROUGE-L
- TEM (Temporal Event Matching)

**Calculation**: Metrics are calculated based on event extraction, relation classification, and LCS algorithm.

**Interpretation**: Higher scores indicate better performance in recognizing and describing facial expression dynamics in videos.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: ['Impact on affected communities']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
