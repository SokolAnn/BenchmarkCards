# CLIMATE MEMES

## 📊 Benchmark Details

**Name**: CLIMATE MEMES

**Overview**: CLIMATE MEMES is the first dataset of climate-change memes annotated with both stance and media frames, allowing analysis of frame prominence over time and communities, and examining framing preferences of different stance holders.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Media Frames Corpus

**Resources**:
- [GitHub Repository](https://github.com/JaidedAI/EasyOCR)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to analyze stances and media frames in climate change memes, examining how media frames shape the visual representation of climate change across varying stances.

**Target Audience**:
- ML Researchers
- Communication Science Specialists
- Media Analysts

**Tasks**:
- Stance Detection
- Media Frame Detection

**Limitations**: The dataset focuses exclusively on memes sourced from Reddit, introducing potential biases associated with the platform.

**Out of Scope Uses**:
- N/A

## 💾 Data

**Source**: 1,184 CC memes from 47 subreddits annotated with stance on climate change and media frames.

**Size**: 1,184 memes

**Format**: JSON

**Annotation**: Manual annotation by graduate students in computational linguistics.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics for stance detection are calculated based on label distribution; F1 Score is emphasized due to label imbalance.

**Interpretation**: Higher accuracy and F1 indicate better model performance in detecting the correct stances and frames.

**Baseline Results**: Baseline accuracy of 80.85% for majority class is convinced; baseline F1 Score of 29.80%.

**Validation**: Inter-Annotator Agreement was assessed with Cohen's Kappa scoring high at 0.83.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**
- **Robustness**
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['N/A']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All annotations were conducted ethically, ensuring annotators were not exposed to distressing content.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
