# ResponseNet

## 📊 Benchmark Details

**Name**: ResponseNet

**Overview**: ResponseNet is a new dataset comprising 696 high-quality dyadic interactions featuring synchronized split-screen videos, multichannel audio, transcripts, and facial behavior annotations. It supports the Online Multimodal Conversational Response Generation (OMCRG) task by providing multimodal data suitable for generating synchronized verbal and non-verbal listener responses.

**Data Type**: synchronized split-screen videos, multichannel audio, transcripts, facial behavior annotations

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://omniresponse.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To establish a standardized evaluation for the Online Multimodal Conversational Response Generation (OMCRG) task.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Multimodal Response Generation

**Limitations**: N/A

## 💾 Data

**Source**: Automated sourcing from YouTube and manual curation for quality assurance.

**Size**: 696 dyadic conversation pairs

**Format**: synchronized video files, transcriptions in text format

**Annotation**: Manual annotation by experts for facial behavior and speech transcriptions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- METEOR
- BERTScore F1
- ROUGE-L
- Distinct-2
- UTMOSv2
- LSE-D
- Fréchet Distance (FD)
- Fréchet Video Distance (FVD)

**Calculation**: Metrics calculated based on comparisons between generated outputs and reference responses.

**Interpretation**: Performance interpreted based on scores, with higher values indicating better generation quality and synchronization.

**Baseline Results**: Comparative results against several established baselines are provided in the paper.

**Validation**: Extensive evaluations against baseline models to ensure accuracy and consistency of the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Safety

**Atlas Risks**:
- **Fairness**
- **Privacy**: Personal information in data
- **Societal Impact**: Impact on education: plagiarism, Impact on Jobs

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Privacy measures are in place due to the collection of multimodal data involving human participants.

**Data Licensing**: CC BY-NC-SA license for non-commercial use with attribution required.

**Consent Procedures**: Informed consent obtained from participants involved in data collection.

**Compliance With Regulations**: Not Applicable
