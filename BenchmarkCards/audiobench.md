# AudioBench

## 📊 Benchmark Details

**Name**: AudioBench

**Overview**: AudioBench is a universal benchmark designed to evaluate Audio Large Language Models (AudioLLMs) across 8 distinct tasks and 26 datasets, including 7 newly proposed datasets, focusing on speech understanding, audio scene understanding, and voice understanding.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/AudioLLMs/AudioBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework specifically for AudioLLMs that measures their instruction-following capabilities and performance in various audio-related tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Automatic Speech Recognition
- Speech Question Answering
- Audio Question Answering
- Emotion Recognition
- Accent Recognition
- Gender Recognition
- Audio Captioning
- Speech Instruction

**Limitations**: The current benchmark exclusively includes English datasets and does not cover multilingual capabilities or code-switching.

## 💾 Data

**Source**: The benchmark includes existing datasets and newly created datasets tailored for AudioLLMs.

**Size**: 400+ hours of audio, 100k+ samples

**Format**: N/A

**Annotation**: Various, including manual annotation and automated generation

## 🔬 Methodology

**Methods**:
- Model-as-Judge
- Human evaluation

**Metrics**:
- Word Error Rate (WER)
- METEOR

**Calculation**: Scores are calculated using model outputs against reference answers, primarily employing Model-as-Judge methods.

**Interpretation**: Evaluation scores are rescaled to a 100-point scale for easier comparison.

**Baseline Results**: Results are compared across five models including SALMONN, Qwen-Audio, and Whisper+Llama3.

**Validation**: Evaluation of models was conducted through comprehensive testing across a variety of tasks with detailed statistical analysis.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
