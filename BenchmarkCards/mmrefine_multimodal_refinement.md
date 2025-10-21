# MMRefine (MultiModal Refinement)

## 📊 Benchmark Details

**Name**: MMRefine (MultiModal Refinement)

**Overview**: MMRefine is a MultiModal Refinement benchmark designed to evaluate the error refinement capabilities of Multimodal Large Language Models (MLLMs) across various scenarios and error types.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/naver-ai/MMRefine)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the refinement capabilities of MLLMs across the entire refinement process.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Model Developers

**Tasks**:
- Error Detection
- Error Correction

**Limitations**: N/A

## 💾 Data

**Source**: MathOdyssey and MathVision datasets

**Size**: 200 problems

**Format**: N/A

**Annotation**: Manual annotation by 14 annotators

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- RefScore
- mRecall

**Calculation**: RefScore is calculated as RS - FD, where RS is the proportion of corrected solutions and FD is the proportion of uncorrected solutions.

**Interpretation**: Higher RefScore indicates better refinement performance.

**Validation**: The effectiveness of MMRefine was validated through experiments with various MLLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MMRefine is released under the CC BY-SA 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
