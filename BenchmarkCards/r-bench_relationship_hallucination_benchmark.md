# R-Bench (Relationship Hallucination Benchmark)

## 📊 Benchmark Details

**Name**: R-Bench (Relationship Hallucination Benchmark)

**Overview**: R-Bench is a novel benchmark for evaluating relationship hallucinations in Large Vision-Language Models (LVLMs), featuring image-level and instance-level questions focused on the existence of relationships and assessing local visual comprehension.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- POPE
- AMBER

**Resources**:
- [GitHub Repository](https://github.com/mrwu-mac/R-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To analyze and evaluate relationship hallucinations in Large Vision-Language Models.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Visual Question Answering
- Visual Relationship Detection

**Limitations**: N/A

## 💾 Data

**Source**: Based on the nocaps validation set, which consists of images from OpenImage and curated manually to prevent overlap with pre-trained data of LVLMs.

**Size**: 11,651 questions

**Format**: N/A

**Annotation**: Combination of automatic generation by Large Language Model and manual curation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are computed based on evaluation of model responses to yes/no questions.

**Interpretation**: Higher scores reflect better model understanding of visual relationships and lower hallucination rates.

**Baseline Results**: N/A

**Validation**: Question evaluation through visual validation to ensure logical consistency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
