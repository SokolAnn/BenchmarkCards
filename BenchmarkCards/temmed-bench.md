# TEMMED-BENCH

## 📊 Benchmark Details

**Name**: TEMMED-BENCH

**Overview**: TEMMED-BENCH is the first benchmark designed for analyzing changes in patients’ conditions between different clinical visits, challenging large vision-language models to reason over temporal medical images.

**Data Type**: visual question-answering pairs, report generation, image-pair selection

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://TemMedBench.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the ability of large vision-language models in reasoning over temporal medical images and to provide a comprehensive assessment that simulates real-world clinical practices.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Model Developers

**Tasks**:
- Visual Question Answering
- Report Generation
- Image-Pair Selection

**Limitations**: N/A

## 💾 Data

**Source**: CheXpert Plus dataset

**Size**: 18,144 instances

**Format**: N/A

**Annotation**: Reviews and generation using expert input and automatic methods.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- BLEU
- ROUGE-L
- METEOR

**Calculation**: Metrics are calculated using standard evaluation methods defined for each task.

**Interpretation**: Higher scores indicate better performance in reasoning tasks pertaining to temporal medical images.

**Baseline Results**: Highest VQA accuracy achieved by GPT o4-mini at 79.15%.

**Validation**: Extensive evaluation conducted on twelve large vision-language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Anonymization procedures were implemented; no personally identifiable information was retained.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
