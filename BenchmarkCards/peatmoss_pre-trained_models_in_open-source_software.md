# PeaTMOSS (Pre-Trained Models in Open-Source Software)

## 📊 Benchmark Details

**Name**: PeaTMOSS (Pre-Trained Models in Open-Source Software)

**Overview**: PeaTMOSS dataset comprises metadata for 281,638 pre-trained models, snapshots for 14,296 models with over 50 monthly downloads, and 28,575 open-source software repositories from GitHub that utilize these models, providing a foundational dataset for exploring the PTM supply chain.

**Data Type**: metadata and repository information

**Domains**:
- Natural Language Processing
- Computer Vision
- Audio
- Multimodal

**Languages**:
- English

**Similar Benchmarks**:
- PTMTorrent
- HF-Community

**Resources**:
- [GitHub Repository](https://github.com/PurdueDualityLab/PeaTMOSS-Artifact)
- [Resource](https://transfer.rcac.purdue.edu/file-manager?origin_id=ff978999-16c2-4b50-ac7a-947ffdc3eb1d&origin_path=%2F)

## 🎯 Purpose and Intended Users

**Goal**: To enable the mining of pre-trained models (PTMs) and open-source software that utilizes these models, along with relationships between them.

**Target Audience**:
- Researchers
- Software Engineers
- Data Scientists

**Tasks**:
- Mining Software Repositories
- Model Evaluation
- Software License Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Collected from Hugging Face and PyTorch Hub APIs, along with linked GitHub repositories.

**Size**: 7.12 GB (metadata version) and 48.2 TB (full version)

**Format**: SQLite Database

**Annotation**: Automatically extracted metadata using large language models.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Data collection via APIs
- Static code analysis

**Metrics**:
- Data completeness
- Metadata accuracy

**Calculation**: Calculated accuracy of metadata extraction based on manual checks.

**Interpretation**: Higher accuracy indicates better quality of metadata extraction.

**Baseline Results**: GPT-3.5-turbo achieved 67.46% accuracy on a sample, improved to 94.39% with GPT-4-turbo.

**Validation**: Employing stratified sampling to evaluate and enhance data quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Legal Compliance

**Atlas Risks**:
- **Fairness**: Data bias
- **Legal Compliance**: Model usage rights restrictions

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
