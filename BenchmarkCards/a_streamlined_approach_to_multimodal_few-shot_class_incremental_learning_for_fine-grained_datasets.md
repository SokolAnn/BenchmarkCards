# A streamlined Approach to Multimodal Few-Shot Class Incremental Learning for Fine-Grained Datasets

## 📊 Benchmark Details

**Name**: A streamlined Approach to Multimodal Few-Shot Class Incremental Learning for Fine-Grained Datasets

**Overview**: This paper introduces a minimalist multi-modal approach to Few-Shot Class Incremental Learning (FSCIL) that enhances separability in fine-grained datasets and introduces three new fine-grained datasets for evaluation.

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- CIFAR100
- miniImageNet
- CUB200
- StanfordCars
- FGVCAircraft
- iNF200

**Resources**:
- [GitHub Repository](https://github.com/tldoan/CLIP-M3)

## 🎯 Purpose and Intended Users

**Goal**: To tackle the challenge of retaining knowledge while learning from limited new data streams in a parameter-efficient manner.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Image Classification
- Object Detection

**Limitations**: N/A

## 💾 Data

**Source**: Three newly introduced fine-grained datasets specifically designed for Few-Shot Class Incremental Learning.

**Size**: 10,000 images for each dataset

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the average performance across multiple sessions of learning.

**Interpretation**: Higher accuracy indicates better performance in retaining learned knowledge while adapting to new data.

**Baseline Results**: The method shows an average 10-point improvement over existing baselines.

**Validation**: Results validated on three newly introduced fine-grained datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
