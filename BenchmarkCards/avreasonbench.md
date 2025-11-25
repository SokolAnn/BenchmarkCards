# AVReasonBench

## 📊 Benchmark Details

**Name**: AVReasonBench

**Overview**: AVReasonBench is a comprehensive benchmark consisting of 4500 audio-visual samples equipped with detailed step-by-step reasoning solutions across six diverse tasks, aimed at evaluating the reasoning capabilities of audio-visual LLMs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/schowdhury671/aurelia)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and enhance the reasoning capabilities of audio-visual large language models (LLMs) through structured reasoning data.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Audio-Visual Question Answering
- Audio-Visual Captioning
- Audio-Visual Compositional Understanding
- A V-GeoIQ
- A V-Meme
- Dance and Music Matching

**Limitations**: N/A

## 💾 Data

**Source**: Curated from Music-A VQA, A VSD, and V ALOR datasets along with additional manual inspection for task creation.

**Size**: 4500 examples

**Format**: N/A

**Annotation**: Reasoning steps are generated through a structured multi-agent system.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Multi-agent evaluation

**Metrics**:
- Top-1 accuracy
- BLEU Score
- METEOR
- ROUGE

**Calculation**: Accuracy is calculated based on the correctness of the generated reasoning steps against given questions.

**Interpretation**: Higher accuracy indicates better reasoning capabilities of the models in processing audio-visual content.

**Baseline Results**: Various audio-visual LLMs are evaluated against AVReasonBench.

**Validation**: Comparative validation against existing benchmarks such as VideoMME.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
