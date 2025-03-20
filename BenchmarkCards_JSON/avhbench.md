# AVHBench

## 📊 Benchmark Details

**Name**: AVHBench

**Overview**: AVHBench is the first comprehensive benchmark designed specifically to evaluate the perception and comprehension capabilities of audio-visual Large Language Models (LLMs) focusing on cross-modal hallucinations.

**Data Type**: multimodal (audio and visual)

**Resources**:
- [GitHub Repository](https://github.com/kaist-ami/AVHBench)

## 🎯 Purpose and Intended Users

**Goal**: To assess the stability of existing models toward cross-modal-driven hallucinations and to provide insights for developing more robust models.

**Target Audience**:
- Researchers
- Developers
- AI practitioners

**Tasks**:
- Audio-driven Video Hallucination
- Video-driven Audio Hallucination
- Audio-visual Matching
- Audio-visual Captioning

**Limitations**: None

## 💾 Data

**Source**: V ALOR and AudioCaps datasets

**Size**: 5,816 QnA pairs and 1,238 audio-visual captions across 2,136 videos

**Format**: Mixed (QnA pairs and captions)

**Annotation**: Semi-automatic annotation pipeline ensures high-quality annotations

## 🔬 Methodology

**Methods**:
- Low-Rank Adaptation (LoRA) fine-tuning
- Multi-modal training
- Annotation pipeline

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score
- METEOR
- CIDEr
- GA VIE

**Calculation**: Evaluated based on conventional metrics for assessing vision-language hallucinations.

**Interpretation**: Metrics indicate the performance of models in distinguishing hallucinations and accurately describing multimodal input.

**Validation**: Evaluated on six different recent audio-visual LLMs

## ⚠️ Targeted Risks

**Risk Categories**:
- Hallucination
- Misinterpretation of signals

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Hallucination

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The benchmark has undergone a human annotation process, mitigating potential negative biases.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
