# A VQA-Hard and Music-A VQA-Hard

## 📊 Benchmark Details

**Name**: A VQA-Hard and Music-A VQA-Hard

**Overview**: We curate and release A VQA-Hard and Music-A VQA-Hard by filtering out items solvable from a single frame to enable faithful evaluation of audio-visual reasoning.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- A VQA
- Music-A VQA

**Resources**:
- [GitHub Repository](https://github.com/naver-ai/LLaVA-AV-SSM)

## 🎯 Purpose and Intended Users

**Goal**: To enable faithful evaluation of how audio contributes to video understanding in Video-LLMs.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Audio-Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Constructed by filtering existing datasets to remove items solvable from a single frame.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Evaluation on curated hard splits
- Comparison of model variants with and without audio

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Accuracy is calculated based on the percentage of correct answers for the question-answering tasks.

**Interpretation**: Higher accuracy indicates better performance in utilizing audio and visual information in Video-LLMs.

**Baseline Results**: N/A

**Validation**: Performance validated across multiple benchmarks and model configurations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
