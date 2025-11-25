# MER-UniBench

## 📊 Benchmark Details

**Name**: MER-UniBench

**Overview**: MER-UniBench is a comprehensive evaluation benchmark designed to cover typical multimodal emotion recognition (MER) tasks, including fine-grained emotion recognition, basic emotion recognition, and sentiment analysis.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MER2023
- MER2024
- IEMOCAP
- MELD
- CMU-MOSI
- CMU-MOSEI

**Resources**:
- [GitHub Repository](https://github.com/zeroQiaoba/AffectGPT)

## 🎯 Purpose and Intended Users

**Goal**: To advance emotional understanding capabilities of MLLMs through a unified benchmark with tailored evaluation metrics.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Fine-grained Emotion Recognition
- Basic Emotion Recognition
- Sentiment Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Sourced from the unlabeled parts of MER2024 with explicit permission from dataset owners.

**Size**: 115,595 samples

**Format**: N/A

**Annotation**: Model-led, human-assisted annotation strategy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Hit Rate
- Weighted Average F-score (WAF)
- Accuracy

**Calculation**: Hit Rate is calculated based on whether the true emotion label is included in the predicted labels from MLLM outputs.

**Interpretation**: Higher scores indicate better performance and recognition of emotional states.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The paper does not involve the collection of new data; it uses existing datasets with permission.

**Data Licensing**: Data is licensed under CC BY-NC 4.0, requiring responsible use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
