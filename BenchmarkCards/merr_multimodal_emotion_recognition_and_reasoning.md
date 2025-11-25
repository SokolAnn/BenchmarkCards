# MERR (Multimodal Emotion Recognition and Reasoning)

## 📊 Benchmark Details

**Name**: MERR (Multimodal Emotion Recognition and Reasoning)

**Overview**: The MERR dataset contains 28,618 coarse-grained and 4,487 fine-grained annotated samples across diverse emotional categories, enabling models to learn from varied scenarios and generalize to real-world applications.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- EMER
- MER2023
- DFEW

**Resources**:
- [GitHub Repository](https://github.com/ZebangCheng/Emotion-LLaMA)
- [Resource](https://huggingface.co/spaces/ZebangCheng/Emotion-LLaMA)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rich dataset for multimodal emotion recognition and reasoning, enabling models to accurately identify and explain emotional states using integrated audio, visual, and textual data.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Emotion Recognition
- Emotion Reasoning

**Limitations**: The dataset exhibits some mismatches between emotional cues in a small subset of samples.

## 💾 Data

**Source**: Constructed through comprehensive emotion annotation in video data with human and algorithmic contributions, filtered to enhance quality.

**Size**: 33,105 examples

**Format**: JSON

**Annotation**: Combination of manual annotation and automated processes.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Weighted Average Recall (WAR)
- Unweighted Average Recall (UAR)

**Calculation**: Metrics are calculated based on the predictions of the Emotion-LLaMA model against the ground truth annotations in the dataset.

**Interpretation**: High scores indicate better performance in recognizing and reasoning about emotions.

**Validation**: Extensive evaluations on multiple datasets to establish performance metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Analysis of emotion accuracy across diverse demographic groups is included in future work.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset annotations are derived from publicly available video data and do not contain personally identifiable information.

**Data Licensing**: The dataset is governed by signed usage agreements restricting its use to academic research.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
