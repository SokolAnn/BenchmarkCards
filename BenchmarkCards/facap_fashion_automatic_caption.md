# FACap (Fashion Automatic Caption)

## 📊 Benchmark Details

**Name**: FACap (Fashion Automatic Caption)

**Overview**: FACap is a large-scale fashion-domain composed image retrieval (CIR) dataset with fine-grained annotations, generated automatically to support the retrieval of fashion images based on user preferences and alterations.

**Data Type**: triples of <reference image, modification text, target image>

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Fashion IQ
- DeepFashion

**Resources**:
- [Resource](https://fgxaos.github.io/facap-paper-website/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality dataset for composed image retrieval in the fashion domain with detailed annotations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Composed Image Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Automatically constructed from web-sourced fashion images using a two-stage annotation pipeline with vision-language models and a large language model.

**Size**: 227,680 CIR triplets

**Format**: N/A

**Annotation**: Generated automatically using a vision-language model and a large language model.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Recall@k

**Calculation**: Evaluation is done using the recall metric, measuring how many target images appear in the top-k retrieved images.

**Interpretation**: Higher recall values indicate better performance in retrieving relevant fashion images based on user queries.

**Baseline Results**: N/A

**Validation**: Quality evaluation through manual assessment of randomly sampled triplets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
