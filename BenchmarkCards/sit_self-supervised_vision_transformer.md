# SiT (Self-supervised vIsion Transformer)

## 📊 Benchmark Details

**Name**: SiT (Self-supervised vIsion Transformer)

**Overview**: SiT is the first masked image modeling work for vision transformers that establishes that self-supervised pretraining can outperform supervised pretraining for downstream applications.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- MoCo-v3
- Dino
- MAE
- SimMIM

**Resources**:
- [GitHub Repository](https://github.com/Sara-Ahmed/SiT)

## 🎯 Purpose and Intended Users

**Goal**: To learn a representation of the data in an unsupervised fashion using group masked model learning and estimate different geometric transformations applied to the input image.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Image Classification
- Object Detection
- Segmentation

**Limitations**: N/A

## 💾 Data

**Source**: Publicly available datasets for image classification and segmentation tasks.

**Size**: 1.28M training samples from ImageNet-1K

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Pretraining using self-supervised learning
- Fine-tuning on downstream tasks

**Metrics**:
- Mean Average Precision (mAP)
- Accuracy

**Calculation**: Accuracy is calculated based on the standard classification tasks on the respective datasets, obtaining state-of-the-art results.

**Interpretation**: Higher metric values indicate better performance on the respective visual tasks.

**Baseline Results**: SiT consistently outperforms supervised pretraining and achieves state-of-the-art results on several benchmarks.

**Validation**: Evaluated using standard protocols on benchmark datasets including ImageNet-1K.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
