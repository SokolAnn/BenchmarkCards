# SHIELD

## 📊 Benchmark Details

**Name**: SHIELD

**Overview**: SHIELD is introduced to evaluate the performance of multimodal large language models in face spoofing and forgery detection tasks. It comprises true/false and multiple-choice questions designed to assess MLLM capabilities on multimodal face data across various attack types.

**Data Type**: multimodal

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://www.idiap.ch/en/scientific-research/data/wmca)
- [Resource](https://cvlab.cse.msu.edu/category/downloads.html)
- [GitHub Repository](https://github.com/ondyari/FaceForensics/tree/master/dataset)
- [Resource](https://huggingface.co/datasets/OpenRL/DeepFakeFace)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the effectiveness of multimodal large language models in detecting face spoofing and forgery.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Face Anti-Spoofing
- Face Forgery Detection

**Limitations**: N/A

## 💾 Data

**Source**: WMCA, SiW-Mv2, and FaceForensics++ datasets.

**Size**: 500 images

**Format**: N/A

**Annotation**: Images from various modalities (RGB, infrared, depth) annotated with multiple attack types.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Half Total Error Rate (HTER)

**Calculation**: Performance is calculated based on the correct response to questions regarding real vs. spoofed faces and the classifications of forgery types.

**Interpretation**: Higher accuracy and lower HTER indicate better detection capabilities of models.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
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
