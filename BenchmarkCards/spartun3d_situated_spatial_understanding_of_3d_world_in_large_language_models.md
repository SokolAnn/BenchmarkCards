# Spartun3D (Situated Spatial Understanding of 3D World in Large Language Models)

## 📊 Benchmark Details

**Name**: Spartun3D (Situated Spatial Understanding of 3D World in Large Language Models)

**Overview**: Spartun3D introduces a scalable situated 3D dataset that incorporates various situated spatial reasoning tasks, aiming to enhance the alignment between 3D visual representations and their corresponding textual descriptions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- SQA3D

**Resources**:
- [GitHub Repository](https://github.com/zhangyuejoslin/Spartun3D)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the situated understanding of 3D-based large language models through a new dataset and model architecture.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Situated Captioning
- Situated Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated dataset based on 3D scenes from 3RScan.

**Size**: 133,000 examples

**Format**: JSON

**Annotation**: Automatically generated

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- CIDEr
- BLEU Score
- METEOR
- ROUGE-L
- Exact Match

**Calculation**: Metrics calculated as per standard NLP evaluation methods.

**Interpretation**: Higher scores indicate better performance in generating situated responses.

**Validation**: Extensive experiments on various tasks demonstrating effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
