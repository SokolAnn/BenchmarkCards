# SEED-Bench-2

## 📊 Benchmark Details

**Name**: SEED-Bench-2

**Overview**: SEED-Bench-2 is a comprehensive benchmark that evaluates the hierarchical capabilities of Multimodal Large Language Models (MLLMs) up to level L3, including the generation of both texts and images given interleaved image-text inputs. It consists of 24K multiple-choice questions with human annotations across 27 evaluation dimensions.

**Data Type**: multiple-choice questions with texts and images

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- SEED-Bench-1
- MMBench
- MME

**Resources**:
- [GitHub Repository](https://github.com/AILab-CVC/SEED-Bench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of SEED-Bench-2 is to evaluate and benchmark the capabilities of MLLMs in comprehending and generating multimodal content effectively.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Scene Understanding
- Instance Identity
- Instance Attribute
- Instance Location
- Instance Counting
- Spatial Relation
- Instance Interaction
- Visual Reasoning
- Text Recognition
- Celebrity Recognition
- Landmark Recognition
- Chart Understanding
- Visual Referring Expression
- Science Knowledge
- Emotion Recognition
- Visual Mathematics
- Difference Spotting
- Meme Comprehension
- Global Video Understanding
- Action Recognition
- Action Prediction
- Procedure Understanding
- In-Context Captioning
- Interleaved Image-Text Analysis
- Text-to-Image Generation
- Next Image Prediction
- Text-Image Creation

**Limitations**: N/A

## 💾 Data

**Source**: Generated multiple-choice questions based on various datasets including CC3M for textual and visual understanding.

**Size**: 24,000 multiple-choice questions

**Format**: JSON

**Annotation**: Human annotation with groundtruth answers derived from collected data.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is computed based on the proportion of correctly answered questions against the total number of questions in each evaluation dimension.

**Interpretation**: Higher accuracy indicates better performance of the MLLMs on given tasks. The evaluation results provide insights into model strengths and weaknesses.

**Validation**: Evaluation against multiple open-source MLLMs to validate performance across various dimensions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
