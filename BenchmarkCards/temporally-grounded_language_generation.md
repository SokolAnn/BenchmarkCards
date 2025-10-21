# Temporally-Grounded Language Generation

## 📊 Benchmark Details

**Name**: Temporally-Grounded Language Generation

**Overview**: Temporally-Grounded Language Generation (TGLG) is a benchmark task that requires models to generate utterances that are both semantically accurate and precisely timed in response to streaming visual input. It evaluates two core capabilities necessary for real-time environments: perceptual updating and contingency awareness.

**Data Type**: video-text pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2505.11326)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to facilitate the development and evaluation of vision-language models (VLMs) in real-time environments.

**Target Audience**:
- Machine Learning Researchers
- AI Practitioners
- Model Developers

**Tasks**:
- Real-Time Language Generation
- Video Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Curated datasets from sports broadcasting (SoccerNet) and egocentric human interactions (HoloAssist)

**Size**: 16,487 examples for perceptual updating, 1,761 examples for contingency awareness

**Format**: N/A

**Annotation**: Manual annotation and filtering of commentary in SoccerNet, and transcription with fine-grained dialogue acts in HoloAssist.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Temporal Responsiveness and Alignment Evaluation (TRACE)

**Calculation**: TRACE measures alignments of generated utterances to ground-truth by evaluating both semantic accuracy and timing precision.

**Interpretation**: High TRACE scores indicate effective real-time interactions where utterance content and timing closely match expected outcomes.

**Baseline Results**: VLM-TSI outperforms VideoLLM-Online on TGLG under the TRACE metric.

**Validation**: Detailed evaluations conducted across datasets to establish model performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
