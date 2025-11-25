# debiaSAE: Benchmarking and Mitigating Vision-Language Model Bias

## 📊 Benchmark Details

**Name**: debiaSAE: Benchmarking and Mitigating Vision-Language Model Bias

**Overview**: This paper introduces a rigorous evaluation dataset and a debiasing method based on Sparse Autoencoders to assess and reduce bias in Vision Language Models (VLMs). It identifies weaknesses in existing bias evaluation datasets and presents improvements in both measurement and model fairness.

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/KuleenS/VLMBiasEval)
- [Resource](https://arxiv.org/abs/2410.13146v2)

## 🎯 Purpose and Intended Users

**Goal**: To provide a more effective dataset for measuring bias in Vision-Language Models and introduce a novel method for debiasing these models.

**Target Audience**:
- ML Researchers
- Ethics Researchers
- AI Practitioners

**Tasks**:
- Bias Evaluation
- Debiasing

**Limitations**: The models evaluated may not fully represent all existing VLMs due to the impracticality of evaluating every available model.

## 💾 Data

**Source**: Multiple datasets including UTKFace, CelebA, VisoGender, PATA, and VLStereoSet.

**Size**: Approximately 700 images for VisoGender, 200k images for CelebA, and over 20k images for UTKFace.

**Format**: N/A

**Annotation**: Annotation based on protected attributes such as sex, race, and religion.

## 🔬 Methodology

**Methods**:
- Evaluating bias through comparative analysis of model performance on various datasets.
- Using Sparse Autoencoders for debiasing methods.

**Metrics**:
- Macro-F1 Score
- Demographic Parity Ratio (DPR)
- Resolution Bias (RB)

**Calculation**: Metrics calculated based on model performance on evaluated datasets, using established fairness evaluation methods.

**Interpretation**: High Macro-F1 scores indicate better model performance, whereas lower RB values suggest less bias.

**Validation**: Validation of the proposed method involves comparison against baseline models and previously established benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Comprehensive analysis of biases across gender and race in VLMs.

**Potential Harm**: ['Perpetuation of societal biases through biased model outputs.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
