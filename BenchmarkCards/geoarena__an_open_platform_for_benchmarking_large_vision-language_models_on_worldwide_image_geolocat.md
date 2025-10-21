# GeoArena: An Open Platform for Benchmarking Large Vision-Language Models on Worldwide Image Geolocation

## 📊 Benchmark Details

**Name**: GeoArena: An Open Platform for Benchmarking Large Vision-Language Models on Worldwide Image Geolocation

**Overview**: GeoArena is the first live, user-preference-based open platform for evaluating Large Vision-Language Models on image worldwide geolocalization tasks. It collects in-the-wild images from users and uses pairwise human preference evaluations to overcome limitations of existing static benchmarks.

**Data Type**: image and text

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/spaces/garena2/GeoArena)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dynamic and user-centered evaluation framework for large vision-language models in geolocalization tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Image Geolocation

**Limitations**: N/A

## 💾 Data

**Source**: User-submitted in-the-wild images

**Size**: 1,000 samples

**Format**: JSON

**Annotation**: Collects user-uploaded images, textual instructions, model responses, and human voting outcomes.

## 🔬 Methodology

**Methods**:
- Pairwise human preference evaluations
- Ranking computation via the Bradley-Terry model

**Metrics**:
- Elo rating

**Calculation**: Scores are calculated based on user preferences and match outcomes between model responses.

**Interpretation**: The metrics reflect the model's capability as judged by user responses in a pairwise comparison.

**Baseline Results**: N/A

**Validation**: The robustness of the rankings is verified through confidence intervals of model performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in prompt
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User inputs are anonymized to preserve privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Users submit images voluntarily.

**Compliance With Regulations**: Not Applicable
