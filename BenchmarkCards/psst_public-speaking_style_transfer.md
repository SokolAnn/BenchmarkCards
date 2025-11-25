# PSST (Public-Speaking Style Transfer)

## 📊 Benchmark Details

**Name**: PSST (Public-Speaking Style Transfer)

**Overview**: PSST is a novel task designed to transform formal, passage-level texts into more engaging public-speaking styles, encompassing various linguistic sub-styles and evaluated through a fine-grained framework to enhance the language style modeling capabilities of large language models.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Text Style Transfer

**Resources**:
- [GitHub Repository](https://github.com/shs910/PSST)
- [Resource](https://huggingface.co/datasets/iwslt2017/viewer/iwslt2017-en-zh)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of PSST is to evaluate and enhance the language style modeling capabilities of large language models through the transformation of formal texts into public-speaking styles.

**Target Audience**:
- ML Researchers
- Speech Designers
- Natural Language Processing Practitioners

**Tasks**:
- Text Style Transfer

**Limitations**: N/A

## 💾 Data

**Source**: The dataset for PSST includes formal texts from encyclopedias, news articles, and academic papers, as well as real public speaking data such as TED Talks.

**Size**: 240 samples

**Format**: text

**Annotation**: Manual annotation by experts focusing on linguistic characteristics relevant to public speaking.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Style strength score
- Semantic preservation accuracy

**Calculation**: Style strength and semantic preservation are evaluated using defined scoring metrics based on linguistic sub-styles and a QA framework.

**Interpretation**: Higher scores indicate better adherence to public-speaking characteristics such as interactivity, emotionality, vividness, and orality.

**Baseline Results**: N/A

**Validation**: The performance of LLMs on PSST tasks was validated through comparative analysis with human evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
