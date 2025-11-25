# AudioCodecBench

## 📊 Benchmark Details

**Name**: AudioCodecBench

**Overview**: AudioCodecBench is a comprehensive benchmark that systematically evaluates codec capabilities across audio reconstruction, codebook ID stability, decoder-only transformer perplexity, and downstream probe task performance.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- SUPERB
- MARBLE
- HEAR

**Resources**:
- [GitHub Repository](https://github.com/wuzhiyue111/Codec-Evaluation)
- [Resource](https://huggingface.co/datasets/LeBeGut/AudioCodecBench)

## 🎯 Purpose and Intended Users

**Goal**: The main goal of the AudioCodecBench is to provide a unified framework for evaluating audio codecs in terms of their performance across various audio representation tasks.

**Target Audience**:
- ML Researchers
- Audio Engineers
- Model Developers

**Tasks**:
- Audio Reconstruction
- Codebook ID Stability Evaluation
- Perplexity Measurement
- Downstream Task Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Comprehensive dataset consisting of 17 sub-datasets covering major audio categories of speech, environmental sound, and music.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Word Error Rate (WER)
- Character Error Rate (CER)
- PESQ
- STOI
- Accuracy
- ROC-AUC

**Calculation**: Calculation of metrics is based on established evaluation criteria appropriate for various audio tasks.

**Interpretation**: Higher scores in PESQ and STOI indicate better audio quality in reconstruction tasks. Accuracy metrics reflect effective model performance in classification tasks.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Robustness**: Prompt injection attack, Evasion attack
- **Accuracy**: Data contamination, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
