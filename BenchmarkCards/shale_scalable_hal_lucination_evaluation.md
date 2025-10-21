# SHALE (Scalable HAL lucination Evaluation)

## 📊 Benchmark Details

**Name**: SHALE (Scalable HAL lucination Evaluation)

**Overview**: SHALE is a scalable hallucination benchmark designed to assess both faithfulness and factuality hallucinations via a fine-grained hallucination categorization scheme, comprising over 30K image-instruction pairs across various evaluation tasks and scenarios.

**Data Type**: image-instruction pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/BeiiiY/SHALE)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of hallucinations in Large Vision-Language Models (LVLMs) under diverse conditions and scenarios.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Discriminative Tasks
- Generative Tasks

**Limitations**: SHALE currently covers only a representative subset rather than an exhaustive range of fine-grained hallucination dimensions.

## 💾 Data

**Source**: Generated using an automated data construction pipeline based on predefined prompt templates filled with diverse image elements.

**Size**: 30,000 image-instruction pairs

**Format**: JSON

**Annotation**: Automatically generated with minimal human verification for quality control.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation via LLM-as-a-Judge approach

**Metrics**:
- Accuracy
- Non-hallucination rate
- Resistance Rate (RR)

**Calculation**: Non-hallucination rates are calculated by prompting an LLM to assess if responses from models are hallucination-free.

**Interpretation**: A higher non-hallucination rate indicates better model performance in handling hallucinations.

**Validation**: Extensive experiments were conducted on over 20 mainstream LVLMs revealing significant factuality hallucinations and model sensitivities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No identifiable personal data or explicit content was included in the benchmark.

**Data Licensing**: This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
