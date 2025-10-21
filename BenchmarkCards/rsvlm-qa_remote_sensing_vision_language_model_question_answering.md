# RSVLM-QA (Remote Sensing Vision Language Model Question Answering)

## 📊 Benchmark Details

**Name**: RSVLM-QA (Remote Sensing Vision Language Model Question Answering)

**Overview**: RSVLM-QA is a new large-scale, content-rich Visual Question Answering dataset for the remote sensing domain, constructed by integrating data from several prominent RS segmentation and detection datasets. It aims to address existing limitations in annotation richness, question diversity, and assessment of reasoning capabilities.

**Data Type**: Visual Question Answering pairs

**Domains**:
- Natural Language Processing
- Earth and Atmospheric Sciences

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/StarZi0213/RSVLM-QA)

## 🎯 Purpose and Intended Users

**Goal**: To advance Remote Sensing Visual Question Answering (RSVQA) through a large-scale, richly annotated dataset.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Visual Question Answering
- Image Captioning

**Limitations**: N/A

## 💾 Data

**Source**: Data constructed by integrating WHU, LoveDA, INRIA, and iSAID datasets.

**Size**: 13,820 images and 162,373 Visual Question Answering pairs

**Format**: N/A

**Annotation**: Generated using large language models and a dual-track annotation generation pipeline.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- BLEU Score
- ROUGE-L
- METEOR

**Calculation**: VQA accuracy is calculated as the percentage of correct judgments per category.

**Interpretation**: Higher accuracy indicates better understanding and reasoning capabilities of VLMs.

**Baseline Results**: Ovis2 achieved an average accuracy of 66.96% in the VQA task.

**Validation**: Stringent quality assurance protocol with both automated screening and manual verification.

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

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
