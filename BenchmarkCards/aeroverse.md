# AeroVerse

## 📊 Benchmark Details

**Name**: AeroVerse

**Overview**: AeroVerse is a benchmark suite for simulating, pre-training, fine-tuning, and evaluating aerospace embodied world models, specifically for unmanned aerial vehicles (UAVs). It includes two pre-training datasets (AerialAgent-Ego10k and CyberAgent-Ego500k), five downstream task instruction datasets, and a comprehensive evaluation method based on GPT-4.

**Data Type**: image-text pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2408.15511)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for advancing aerospace embodied intelligence and empowering UAV agents with autonomous capabilities.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Aerospace Embodied Scene Awareness
- Aerospace Embodied Spatial Reasoning
- Aerospace Embodied Navigational Exploration
- Aerospace Embodied Task Planning
- Aerospace Embodied Motion Decision

**Limitations**: N/A

## 💾 Data

**Source**: AerialAgent-Ego10k and CyberAgent-Ego500k pre-training datasets, and SkyAgent task instruction datasets constructed using AeroSimulator.

**Size**: 10,000 images for AerialAgent-Ego10k; 500,000 images for CyberAgent-Ego500k; 3,000 examples for each of the five SkyAgent tasks.

**Format**: image and text

**Annotation**: Annotated by trained professionals using defined guidelines for UAV-specific tasks.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- BLEU Score
- SPICE
- LLM-Judge-Scene
- LLM-Judge-Reason&Nav
- LLM-Judge-Plan

**Calculation**: BLEU, SPICE scores calculated based on n-gram matches; LLM-Judge evaluates alignment with human feedback through prompt templates.

**Interpretation**: Higher scores indicate better alignment with human preferences and understanding of task requirements.

**Baseline Results**: Various baselines evaluated including 2D and 3D visual-language models on the UAV tasks.

**Validation**: Extensive experiments conducted across multiple datasets and models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected with attention to user privacy and anonymization where applicable.

**Data Licensing**: Pending; N/A if not specified.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
