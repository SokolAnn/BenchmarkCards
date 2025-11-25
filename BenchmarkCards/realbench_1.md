# RealBench

## 📊 Benchmark Details

**Name**: RealBench

**Overview**: RealBench is the first Chinese multimodal multi-image dataset designed to evaluate multi-image understanding capabilities in real-world Chinese scenarios, containing 9393 samples and 69910 images.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- Chinese

**Similar Benchmarks**:
- MMDU

**Resources**:
- [GitHub Repository](https://github.com/1429904852/RealBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for multimodal understanding of Chinese multi-image scenarios using real user-generated content.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Multi-image Retrieval
- Multi-image Ranking
- Multi-image Extraction
- Multi-image Reasoning

**Limitations**: The dataset is still not exhaustive and can be further expanded to meet the growing data demands of large-scale pretraining models.

## 💾 Data

**Source**: Data is sourced from real user inputs on the Chinese social media platform Xiaohongshu.

**Size**: 9,393 samples and 69,910 images

**Format**: N/A

**Annotation**: Data was collected based on strict filtering criteria ensuring high relevance between images and text.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- ROUGE-L

**Calculation**: Metrics calculated based on model outputs compared to ground truth answers.

**Interpretation**: High ROUGE-L scores indicate better multi-image reasoning capabilities.

**Baseline Results**: GPT-4o and Claude-3.5-Sonnet performed at about 28.55% and 39.32% accuracy on complex tasks.

**Validation**: Quality control through reviews by multiple annotators and expert evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Privacy**

**Demographic Analysis**: The dataset includes diverse scenarios from everyday life.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Comprehensive anonymization techniques are implemented to protect user privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Explicit consent obtained from data providers for any data collected.

**Compliance With Regulations**: Not Applicable
