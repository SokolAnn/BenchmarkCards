# SPA-VL (Safety Preference Alignment for Vision Language Models)

## 📊 Benchmark Details

**Name**: SPA-VL (Safety Preference Alignment for Vision Language Models)

**Overview**: SPA-VL is a large-scale safety alignment dataset for vision-language models that contains 100,788 samples categorized into 6 harmfulness domains, 13 categories, and 53 subcategories, constructed for training models with Reinforcement Learning from Human Feedback (RLHF).

**Data Type**: quadruples (question, image, chosen response, rejected response)

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MM-SafetyBench
- ChEf
- OODCV-VQA

**Resources**:
- [Resource](https://sqrtizhang.github.io/SPA-VL/)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to enhance safety alignment in vision-language models by providing a comprehensive dataset that encompasses both harmlessness and helpfulness criteria.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Safety Alignment

**Limitations**: N/A

## 💾 Data

**Source**: Generated from open and closed-source vision language models, primarily using images from the LAION-5B dataset.

**Size**: 100,788 samples

**Format**: quadruples (JSON)

**Annotation**: Fully automated response generation and preference annotation from multiple models.

## 🔬 Methodology

**Methods**:
- Reinforcement Learning from Human Feedback (RLHF)
- Preference-based Optimization

**Metrics**:
- Harm Score
- Unsafe Rate

**Calculation**: Harm score is calculated based on the proportions of safe and unsafe responses as determined by human evaluators.

**Interpretation**: A lower unsafe rate indicates better alignment with safety standards.

**Baseline Results**: Compared to existing models like LLaV A-7B, the models trained on SPA-VL demonstrated significant improvements in safety metrics.

**Validation**: Evaluated using the HarmEval and HelpEval datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data collected complies with ethical standards, and no personal identification information is involved.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
