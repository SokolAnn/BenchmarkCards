# M5 (Multimodal Multilingual Multicultural Benchmark)

## 📊 Benchmark Details

**Name**: M5 (Multimodal Multilingual Multicultural Benchmark)

**Overview**: M5 is a comprehensive benchmark designed to evaluate Large Multimodal Models (LMMs) on diverse vision-language tasks within a multilingual and multicultural context. It includes eight datasets covering five tasks and 41 languages, focusing on underrepresented languages and culturally diverse images.

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- German
- Bengali
- Amharic
- Berber
- Hausa
- Hindi
- Russian
- Swahili
- Thai
- Filipino
- Chinese
- Arabic

**Similar Benchmarks**:
- BIG-Bench
- HELM
- MMLU
- MMMU

**Resources**:
- [Resource](https://arxiv.org/abs/2407.03791)

## 🎯 Purpose and Intended Users

**Goal**: To fill the gap of multimodal multilingual benchmarks and examine the performance of LMMs across various languages.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Question Answering
- Visually Grounded Reasoning
- Visual Natural Language Inference
- Image Captioning
- Visio-Linguistic Outlier Detection

**Limitations**: N/A

## 💾 Data

**Source**: Mixed datasets including xGQA, MaXM, XVNLI, MaRVL, XM3600, and new datasets M5-VGR and M5-VLOD.

**Size**: N/A

**Format**: JSON, CSV

**Annotation**: Annotated by native speakers of each language for visual and linguistic tasks.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score
- chrF++

**Calculation**: Metrics calculated based on relaxed accuracy and standard evaluation metrics for image captioning.

**Interpretation**: Performance disparity analysis across high and low-resource languages.

**Baseline Results**: Random baseline performance for different datasets.

**Validation**: Extensive evaluation of 18 LMMs across five tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning

**Demographic Analysis**: Performance disparities between market-focused languages and underrepresented languages.

**Potential Harm**: Highlighting ongoing challenges in achieving equitable AI across languages and cultures.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
