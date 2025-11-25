# वाक् सञ्चयः (/Vāksañcayah ̣/)

## 📊 Benchmark Details

**Name**: वाक् सञ्चयः (/Vāksañcayah ̣/)

**Overview**: We present a new, large vocabulary Sanskrit ASR system and the first ever ASR-based study for Sanskrit using a new, large and diverse, labeled speech corpus वाक् सञ्चयः (/Vāksañcayah ̣/).

**Data Type**: speech recordings

**Domains**:
- Natural Language Processing

**Languages**:
- Sanskrit

**Resources**:
- [GitHub Repository](https://github.com/cyfer0618/Vaksanca.git)
- [Resource](http://www.cse.iitb.ac.in/~asr)

## 🎯 Purpose and Intended Users

**Goal**: To introduce a large vocabulary ASR system for Sanskrit and analyze different modeling choices for acoustic and language models in ASR systems.

**Target Audience**:
- ML Researchers
- Speech Recognition Developers
- Linguists

**Tasks**:
- Automatic Speech Recognition

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is collected from various sources including volunteer recordings and online resources.

**Size**: 78 hours of speech covering about 46,000 sentences

**Format**: Audio files

**Annotation**: Transcribed by volunteers using oTranscribe and other tools.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Word Error Rate (WER)
- Character Error Rate (CER)

**Calculation**: WER and CER are computed based on the ASR output compared to the ground truth transcripts.

**Interpretation**: Lower WER/CER indicates better performance of the ASR system.

**Validation**: The ASR system was validated using separate validation and test datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: Analysis includes variances from multiple native language speakers.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent obtained from all speakers involved in recordings.

**Compliance With Regulations**: Not Applicable
