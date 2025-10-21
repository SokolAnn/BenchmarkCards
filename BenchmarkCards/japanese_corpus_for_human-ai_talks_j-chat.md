# Japanese Corpus for Human-AI Talks (J-CHAT)

## 📊 Benchmark Details

**Name**: Japanese Corpus for Human-AI Talks (J-CHAT)

**Overview**: This study addresses the lack of large-scale and diverse speech datasets by constructing and releasing a new open-source corpus, J-CHAT, which provides spontaneous and acoustically clean dialogue speech data for training spoken language models.

**Data Type**: dialogue speech data

**Domains**:
- Natural Language Processing

**Languages**:
- Japanese

**Similar Benchmarks**:
- STUDIES
- DailyTalk
- GigaSpeech

**Resources**:
- [Resource](https://huggingface.co/datasets/sarulab-speech/J-CHAT)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the development of spoken dialogue systems by providing a diverse and large-scale spoken dialogue corpus for training and evaluating spoken language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Dialogue Generation

**Limitations**: The range of speech covered may be limited due to the nature of the data sources.

## 💾 Data

**Source**: Data collected from YouTube and podcasts, filtered for Japanese dialogue speech.

**Size**: 69,000 hours

**Format**: N/A

**Annotation**: Automatically identified dialogue segments with speaker diarization.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Subjective listening tests

**Metrics**:
- Mean Opinion Score (MOS)

**Calculation**: Mean Opinion Score calculated from user evaluations on naturalness and meaningfulness.

**Interpretation**: Higher MOS indicates better perceived quality of generated dialogues.

**Baseline Results**: Comparative results of different models evaluated for naturalness and meaningfulness.

**Validation**: Experimental results validate the effectiveness of the corpus for training dialogue models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Misuse**: Nonconsensual use

**Demographic Analysis**: N/A

**Potential Harm**: Risk of misuse of voice synthesis technology for unauthorized voice cloning.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Speech data was anonymized before use to mitigate privacy risks.

**Data Licensing**: Not Applicable

**Consent Procedures**: Speech was collected with consent from individuals whose voices were used.

**Compliance With Regulations**: Not Applicable
