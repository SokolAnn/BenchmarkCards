# PanoSent (Panoptic Sextuple Extraction Benchmark for Multimodal Conversational Aspect-based Sentiment Analysis)

## 📊 Benchmark Details

**Name**: PanoSent (Panoptic Sextuple Extraction Benchmark for Multimodal Conversational Aspect-based Sentiment Analysis)

**Overview**: PanoSent is a dataset designed for multimodal conversational Aspect-based Sentiment Analysis (ABSA) that incorporates the Panoptic Sentiment Sextuple Extraction and Sentiment Flipping Analysis tasks, covering multiple languages and scenarios.

**Data Type**: multimodal dialogue with sextuple elements including holder, target, aspect, opinion, sentiment, and rationale

**Domains**:
- Natural Language Processing
- Computer Vision
- Food and Cuisine
- Movies and Entertainment
- Technology
- Electronic Products
- Health and Wellness
- Finance and Economy
- Sports and Athletics
- Art and Culture
- Travel and Tourism

**Languages**:
- English
- Chinese
- Spanish

**Resources**:
- [Resource](https://PanoSent.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for evaluating multimodal conversational Aspect-based Sentiment Analysis, enhancing the understanding of sentiment dynamics in dialogues.

**Target Audience**:
- Research Community
- AI Practitioners
- Natural Language Processing Researchers

**Tasks**:
- Panoptic Sentiment Sextuple Extraction
- Sentiment Flipping Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Real-world dialogues collected from diverse social media platforms and synthesized using OpenAI GPT-4

**Size**: 10,000 annotated dialogues

**Format**: N/A

**Annotation**: Manually and automatically annotated with a focus on high-quality benchmarks.

## 🔬 Methodology

**Methods**:
- Chain-of-Sentiment reasoning framework
- Multimodal Large Language Model (Sentica)
- Paraphrase-based verification mechanism

**Metrics**:
- Exact Match F1
- Binary Match F1
- Proportional Match F1
- Macro F1

**Calculation**: F1 scores are calculated for sextuple extraction and sentiment flipping tasks based on precision and recall metrics.

**Interpretation**: Higher F1 scores indicate better model performance in accurately predicting sentiment sextuples and sentiment flipping.

**Baseline Results**: Various multimodal large language models and benchmarked systems as baselines.

**Validation**: Rigorous validation using manual inspections and cross-validation techniques.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset ensures anonymization of personal information and complies with data protection regulations.

**Data Licensing**: The dataset is licensed under a Creative Commons Attribution International 4.0 License.

**Consent Procedures**: Data collected from publicly available sources with explicit consent obtained where necessary.

**Compliance With Regulations**: Compliance with GDPR and CCPA regulations.
