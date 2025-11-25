# ESTR-CoT (Event Stream based Scene Text Recognition with Chain-of-Thought Reasoning)

## 📊 Benchmark Details

**Name**: ESTR-CoT (Event Stream based Scene Text Recognition with Chain-of-Thought Reasoning)

**Overview**: The ESTR-CoT framework improves both the accuracy and interpretability of scene text recognition by integrating chain-of-thought reasoning within event stream inputs, producing both recognition results and reasoning processes.

**Data Type**: image-reasoning pairs

**Domains**:
- Computer Vision

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- EventSTR
- WordArt
- IC15

**Resources**:
- [GitHub Repository](https://github.com/Event-AHU/ESTR-CoT)

## 🎯 Purpose and Intended Users

**Goal**: To propose a novel reasoning-based framework for event stream scene text recognition that enhances model interpretability and accuracy.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Scene Text Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Constructed via a three-stage process involving generation, polishing, and expert verification.

**Size**: 16,222 image-reasoning pairs

**Format**: N/A

**Annotation**: Expert verification and structured multi-stage dataset curation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- BLEU-1
- BLEU-2
- BLEU-3
- BLEU-4

**Calculation**: BLEU scores calculated at character and word levels for Chinese and English, respectively.

**Interpretation**: Higher BLEU scores indicate better linguistic accuracy and reasoning quality.

**Baseline Results**: Comparative performance metrics against traditional STR methods.

**Validation**: Evaluated against three event-based scene text recognition benchmark datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Privacy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
