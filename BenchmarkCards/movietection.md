# MovieTection

## 📊 Benchmark Details

**Name**: MovieTection

**Overview**: MovieTection is a benchmark designed for detecting training data of vision-language models (VLMs), comprising 14,000 diverse movie frames paired with descriptive captions, facilitating the analysis of copyrighted content within model training data.

**Data Type**: image-caption pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/avduarte333/DIS-CO)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for assessing the detection of copyrighted content in vision-language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Image Classification
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: 100 movie titles sampled from Box Office Mojo, framed into 14,000 images with detailed captions.

**Size**: 14,000 frames

**Format**: N/A

**Annotation**: Generated using the 7B version of the Qwen2-VL model.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Area Under the Curve (AUC)

**Calculation**: Calculated by measuring the performance of models on the MovieTection dataset.

**Interpretation**: Higher accuracy indicates better memorization detection capabilities of models.

**Validation**: Performance compared against models known to include the training data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons BY-NC-SA 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Reviewed and approved by the Data Protection Officer of the institution.
