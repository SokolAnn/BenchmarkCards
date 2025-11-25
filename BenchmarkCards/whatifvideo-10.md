# WhatifVideo-1.0

## 📊 Benchmark Details

**Name**: WhatifVideo-1.0

**Overview**: WhatifVideo-1.0 is a new evaluation dataset for open-ended action editing in video, which includes scenarios ranging from simple to complex, and interactions involving multiple people and human-object interactions.

**Data Type**: video with questions and text prompts

**Domains**:
- Computer Vision

**Languages**:
- English

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to evaluate the performance and robustness of models designed for dynamic human action editing in videos based on text prompts.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Video Editing

**Limitations**: N/A

## 💾 Data

**Source**: WhatifVideo-1.0 dataset includes videos collected for evaluating video editing methods focusing on human actions.

**Size**: 101 videos

**Format**: N/A

**Annotation**: Each video is annotated with captions and designed counterfactual questions.

## 🔬 Methodology

**Methods**:
- Quantitative evaluation using pretrained VideoCLIP and CLIP
- Qualitative assessments

**Metrics**:
- Vid-Acc
- Vid-Con
- GT-Con

**Calculation**: Metrics are calculated based on video similarities and consistency to the source video and ground truth.

**Interpretation**: Higher values in Vid-Acc and Vid-Con indicate better performance in editing fidelity and consistency.

**Validation**: Evaluation is performed against other video editing methods using metrics in the benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
