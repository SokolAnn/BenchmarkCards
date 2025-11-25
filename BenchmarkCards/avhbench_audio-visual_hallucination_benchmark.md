# AVHBench (Audio-Visual Hallucination Benchmark)

## 📊 Benchmark Details

**Name**: AVHBench (Audio-Visual Hallucination Benchmark)

**Overview**: AVHBench is a comprehensive benchmark specifically designed to evaluate the perception and comprehension capabilities of audio-visual LLMs, focusing on their susceptibility to cross-modal hallucinations.

**Data Type**: question-answering pairs and audio-visual captions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/kaist-ami/AVHBench)

## 🎯 Purpose and Intended Users

**Goal**: To assess the perception and comprehension capabilities of audio-visual LLMs, specifically that pertaining to hallucinations caused by cross-interactions between audio and visual signals.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Audio-driven Video Hallucination
- Video-driven Audio Hallucination
- Audio-visual Matching
- Audio-visual Captioning

**Limitations**: Although the benchmark aims to assess cross-modal hallucinations, it may not encompass all possible scenarios due to the complexity of multimodal signals.

## 💾 Data

**Source**: The dataset comprises real and synthetic source videos collected from existing datasets, namely VALOR and AudioCaps.

**Size**: 10,327 videos with 87,624 QnA pairs and 1,106 audio-visual captions

**Format**: N/A

**Annotation**: A semi-automatic annotation pipeline with human validation is employed.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- METEOR
- CIDEr

**Calculation**: Metrics are calculated based on both judgment and description tasks using standard definitions.

**Interpretation**: High accuracy and F1 scores indicate better model performance in discerning between genuine and hallucinated signals.

**Baseline Results**: Models evaluated on AVHBench are X-InstructBLIP, ImageBind-LLM, Video-LLaMA, ChatBridge, PandaGPT, and OneLLM.

**Validation**: The benchmark's reliability is ensured through a comprehensive human verification process in the dataset construction.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: The benchmark aims to detect and mitigate hallucinations in audio-visual LLMs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
