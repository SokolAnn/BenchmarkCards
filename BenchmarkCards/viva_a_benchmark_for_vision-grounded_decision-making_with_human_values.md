# VIVA (A Benchmark for Vision-Grounded Decision-Making with Human Values)

## 📊 Benchmark Details

**Name**: VIVA (A Benchmark for Vision-Grounded Decision-Making with Human Values)

**Overview**: VIVA is a benchmark aimed at evaluating vision-grounded decision-making capabilities of vision language models (VLMs) driven by human values. The benchmark contains 1,240 images depicting various real-world situations along with manually annotated decisions grounded in them.

**Data Type**: image-action pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Derekkk/VIVA_EMNLP24)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate vision-grounded decision-making capabilities of VLMs with a focus on human values.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Ethicists

**Tasks**:
- Action Selection
- Value Inference

**Limitations**: The data annotation tends to be brief, potentially limiting depth. Additionally, human values may vary culturally.

## 💾 Data

**Source**: Images collected from open-sourced platforms like Pinterest and Reddit.

**Size**: 1,240 images

**Format**: N/A

**Annotation**: Manually annotated by skilled annotators with support from language models.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Combined accuracy of both action selection and value inference tasks.

**Interpretation**: Higher accuracy indicates better decision-making capabilities aligned with human values.

**Baseline Results**: Baseline accuracy for action selection is 20%, and for value inference is 50%.

**Validation**: Extensive evaluations on both commercial and open-source VLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: Analysis of demographic factors is included to assess fairness across groups.

**Potential Harm**: The benchmark aims to identify potential biases and improve decision-making alignment with human values.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All images sourced from public domains, ensuring compliance with copyright.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
