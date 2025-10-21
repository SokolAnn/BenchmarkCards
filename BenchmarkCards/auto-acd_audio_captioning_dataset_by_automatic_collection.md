# Auto-ACD (Audio Captioning Dataset by Automatic Collection)

## 📊 Benchmark Details

**Name**: Auto-ACD (Audio Captioning Dataset by Automatic Collection)

**Overview**: Auto-ACD is a large-scale audio-language dataset comprising over 1.5M audio-text pairs, generated through an automatic pipeline that leverages audio-visual correspondence to create rich and descriptive captions for audio streams.

**Data Type**: audio-text pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AudioCaps
- Clotho
- LAION-Audio-630K
- WavCaps

**Resources**:
- [Resource](https://doi.org/10.1145/3664647.3681472)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for audio-language representation learning, improving the performance of models on audio-text tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Audio Captioning
- Audio-Text Retrieval
- Zero-shot Classification

**Limitations**: N/A

## 💾 Data

**Source**: Auto-ACD is constructed from AudioSet and VGGSound, employing an automatic data collection process that utilizes publicly available tools and APIs.

**Size**: 1.5 million audio-text pairs

**Format**: N/A

**Annotation**: Automatic caption generation through a series of audio-visual models and a language model.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Recall@k
- Meteor
- RougeL
- Spider

**Calculation**: Metrics are calculated based on performance in retrieval tasks and captioning tasks across various datasets.

**Interpretation**: Higher Recall@k values indicate better performance in audio-text retrieval, while improvements in Meteor and RougeL demonstrate superior captioning quality.

**Baseline Results**: N/A

**Validation**: Manual verification of the test set to ensure the accuracy and relevance of generated captions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
