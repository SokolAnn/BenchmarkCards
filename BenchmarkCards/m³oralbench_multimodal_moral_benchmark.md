# M³oralBench (MultiModal Moral Benchmark)

## 📊 Benchmark Details

**Name**: M³oralBench (MultiModal Moral Benchmark)

**Overview**: M³oralBench is the first multimodal moral evaluation benchmark for large vision-language models (LVLMs), designed to assess their moral understanding and reasoning across six moral foundations of Moral Foundations Theory (MFT) through tasks of moral judgement, moral classification, and moral response.

**Data Type**: moral judgement scenarios, images

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/BeiiiY/M3oralBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation tool for assessing the moral understanding and reasoning abilities of large vision-language models.

**Target Audience**:
- ML Researchers
- Ethicists
- AI Developers

**Tasks**:
- Moral Judgement
- Moral Classification
- Moral Response

**Limitations**: The benchmark currently relies on closed-ended multiple-choice questions without including open-ended question-answering formats.

## 💾 Data

**Source**: Generated using a combination of Moral Foundations Vignettes and a text-to-image diffusion model (SD3.0).

**Size**: 1,160 moral scenarios and 4,640 instructions

**Format**: Custom dataset format

**Annotation**: Automatically generated from moral scenarios with manual verification.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: The likelihood of choosing an option is quantified using Monte Carlo sampling to estimate probabilities based on model responses.

**Interpretation**: Higher accuracy indicates better abilities in moral understanding and reasoning, showing greater alignment with human moral standards.

**Validation**: Extensive experiments conducted on 10 popular open-source and closed-source LVLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All generated images contain no identifiable data or depictions of explicit violence or gore.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
