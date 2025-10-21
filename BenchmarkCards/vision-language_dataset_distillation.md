# Vision-Language Dataset Distillation

## 📊 Benchmark Details

**Name**: Vision-Language Dataset Distillation

**Overview**: This work introduces the first vision-language dataset distillation method, which distills image-text pairs into a smaller dataset while preserving critical information for training vision-language models.

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://princetonvisualai.github.io/multimodal_dataset_distillation/)

## 🎯 Purpose and Intended Users

**Goal**: To efficiently distill vision-language datasets to simplify complex interactions and improve model training.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Image-Text Retrieval

**Limitations**: Dataset distillation is influenced by learning algorithms which could lead to poor transferability; computationally intensive processes are still a challenge.

## 💾 Data

**Source**: Flickr30K and COCO datasets

**Size**: 1000 image-text pairs (for training)

**Format**: N/A

**Annotation**: Automatically generated through the proposed distillation methods.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Image-to-text Retrieval Accuracy (R@1)

**Calculation**: Metrics are calculated by evaluating the fraction of times the correct result appears among the top K items in image-text retrieval tasks.

**Interpretation**: Higher retrieval scores (e.g., R@1, R@5, R@10) indicate effectiveness in matching images and their corresponding text descriptions.

**Baseline Results**: Best performance noted as 9.9% retrieval accuracy (R@1) using 100 distilled pairs.

**Validation**: Performance metrics validated against original datasets (Flickr30K and COCO).

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

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
