# MedDialog: Two Large-scale Medical Dialogue Datasets

## 📊 Benchmark Details

**Name**: MedDialog: Two Large-scale Medical Dialogue Datasets

**Overview**: To facilitate the research and development of medical dialogue systems, we build two large-scale medical dialogue datasets: MedDialog-EN and MedDialog-CN. MedDialog-EN is an English dataset containing 0.3 million conversations between patients and doctors and 0.5 million utterances. MedDialog-CN is a Chinese dataset containing 1.1 million conversations and 4 million utterances. To our best knowledge, MedDialog-(EN,CN) are the largest medical dialogue datasets to date. The dataset is available at https://github.com/UCSD-AI4H/Medical-Dialogue-System

**Data Type**: text (patient-doctor conversations / dialogues)

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- Muzhi
- Dxy
- COVID-EN
- COVID-CN

**Resources**:
- [GitHub Repository](https://github.com/UCSD-AI4H/Medical-Dialogue-System)
- [Resource](https://www.icliniq.com/)
- [Resource](https://www.healthcaremagic.com/)
- [Resource](https://www.haodf.com/)
- [Resource](https://arxiv.org/abs/2004.03329)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the research and development of medical dialogue systems by providing two large-scale medical dialogue datasets (MedDialog-EN and MedDialog-CN).

**Target Audience**:
- Researchers
- Model Developers

**Tasks**:
- Dialogue Generation

**Limitations**: N/A

## 💾 Data

**Source**: MedDialog-EN data crawled from iclinic.com and healthcaremagic.com. MedDialog-CN data crawled from haodf.com.

**Size**: MedDialog-EN: 257,454 consultations and 514,908 utterances (approximately 0.3 million conversations and 0.5 million utterances). MedDialog-CN: 1,145,231 consultations and 3,959,333 utterances (approximately 1.1 million conversations and 4 million utterances). When combining consecutive utterances in MedDialog-CN there are 3,209,660 utterances (1,981,844 from doctors and 1,227,816 from patients).

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Web crawling from online healthcare platforms (icliniq.com, healthcaremagic.com, haodf.com)

**Calculation**: N/A

**Interpretation**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias

**Demographic Analysis**: The patients in MedDialog-EN are from all over the world, with different nationalities, ethics, age, gender, occupation, education, income, etc. The patients in MedDialog-CN are from 31 provincial-level administrative divisions in China, with different ethics, age, gender, occupation, education, income, etc.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
