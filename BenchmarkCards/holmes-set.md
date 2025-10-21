# Holmes-Set

## 📊 Benchmark Details

**Name**: Holmes-Set

**Overview**: Holmes-Set is a large-scale dataset designed for AI-generated image detection. It includes the Holmes-SFTSet for instruction-tuning with explanations about whether images are AI-generated, and the Holmes-DPOSet, a human-aligned preference dataset. It aims to enhance explainability and generalization in AI-generated image detection.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- CNNDetection
- GenImage
- DRCT
- FakeBench
- LOKI

**Resources**:
- [GitHub Repository](https://github.com/wyczzy/AIGI-Holmes)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the Holmes-Set is to provide a comprehensive benchmark for training and evaluating algorithms for detecting AI-generated images, with a focus on human-verifiable explanations and preferences.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Image Classification
- Image Detection

**Limitations**: N/A

## 💾 Data

**Source**: Holmes-SFTSet comprises 65,000 annotated images with explanations, while Holmes-DPOSet includes 4,000 additional human-aligned preference pairs based on these images.

**Size**: 65,000 images

**Format**: N/A

**Annotation**: Annotated using a combination of human experts and automated approaches through Multimodal Large Language Models (MLLMs).

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score
- BLEU Score
- ROUGE-L

**Calculation**: Metrics calculated based on detection results and explanation quality on test samples reviewed by experts.

**Interpretation**: Higher scores in metrics indicate better detection performance and quality of explanations, showcasing the effectiveness of the model in identifying AI-generated images.

**Baseline Results**: AIGI-Holmes achieved state-of-the-art performance on various benchmarks, surpassing existing models by significant margins.

**Validation**: Extensive experiments were conducted to validate the effectiveness of the proposed methods and datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Data privacy concerns related to AI-generated content and user-generated content in the datasets.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: To ensure participant privacy, all expert annotations were conducted under strict guidelines and no personal data was used.

**Data Licensing**: The datasets are open-access under CC BY 4.0 License, allowing for widespread use and modification with proper attribution.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
