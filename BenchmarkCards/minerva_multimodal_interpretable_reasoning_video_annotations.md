# MINERVA (Multimodal INterpretablE Reasoning Video Annotations)

## 📊 Benchmark Details

**Name**: MINERVA (Multimodal INterpretablE Reasoning Video Annotations)

**Overview**: MINERVA is a challenging videoQA dataset consisting of 1,515 hand-crafted questions and detailed, manually-annotated reasoning traces to assess multimodal models' ability to perform complex video reasoning.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- VideoMME
- LVBench
- Neptune

**Resources**:
- [GitHub Repository](https://github.com/google-deepmind/neptune?tab=readme-ov-file#minerva)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating multimodal models on complex video reasoning tasks and to enable insights into how these models reason about video content.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Multimodal videos selected from platforms like YouTube, specifically chosen for their complexity and suitability for reasoning questions.

**Size**: 1,515 questions

**Format**: JSON

**Annotation**: Manually created by expert annotators with guidelines providing complex questions, answers, decoys, and reasoning traces.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Multiple Choice Accuracy (MCQ-Accuracy)

**Calculation**: Metrics are calculated based on the ratio of correctly answered questions to the total number of questions.

**Interpretation**: High accuracy indicates effective reasoning performance by the models evaluated on the dataset.

**Baseline Results**: The best model, Gemini 2.5 Pro Thinking, achieved 66.2% accuracy, while human performance was at 92.5%.

**Validation**: The dataset was validated through expert review and peer scoring.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential misuse in assessment of video reasoning failing to capture diverse reasoning styles.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
