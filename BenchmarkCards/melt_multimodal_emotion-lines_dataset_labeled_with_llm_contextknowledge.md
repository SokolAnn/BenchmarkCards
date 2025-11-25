# MELT (Multimodal Emotion-Lines Dataset Labeled with LLM ContexTKnowledge)

## 📊 Benchmark Details

**Name**: MELT (Multimodal Emotion-Lines Dataset Labeled with LLM ContexTKnowledge)

**Overview**: MELT is a multimodal emotion dataset fully annotated by GPT-4o using a context-aware automatic annotation method, showcasing the application of LLMs in generating reliable, scalable annotations for speech emotion recognition.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MELD

**Resources**:
- [GitHub Repository](https://github.com/KeiKinn/meltdataset.git)

## 🎯 Purpose and Intended Users

**Goal**: To develop a context-aware annotation method using GPT-4o for multimodal emotion data and demonstrate its effectiveness compared to traditional methods.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Speech Emotion Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Derived from the Multimodal EmotionLines Dataset (MELD), utilizing audio data from the sitcom 'Friends'.

**Size**: 7,024 training examples, 1,797 test examples

**Format**: JSON

**Annotation**: Automated annotation using GPT-4o; leveraging structured prompts for consistency.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Unweighted Accuracy Recall (UAR)
- Accuracy (ACC)
- F1 Score

**Calculation**: Metrics calculated as the average of predictions across multiple emotion recognition datasets.

**Interpretation**: Higher scores indicate better model performance in recognizing emotions across the datasets.

**Baseline Results**: MELT consistently outperformed MELD in SER tasks.

**Validation**: Validation through subjective experiments and objective evaluations across various emotion recognition datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
