# Products-10K

## 📊 Benchmark Details

**Name**: Products-10K

**Overview**: Products-10K is a human-labeled product image dataset containing 10,000 fine-grained SKU-level products frequently bought by online customers in JD.com, aimed at improving the accuracy of product recognition systems.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- iMaterialist Competition
- AliProducts Challenge

**Resources**:
- [Resource](https://products-10k.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large, high-quality product recognition dataset for improving fine-grained image classification in retail and e-commerce applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Image Classification
- Fine-grained Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Images collected from the online shopping website JD.com

**Size**: 150,000 images

**Format**: N/A

**Annotation**: Manually labeled by human experts, with at least three experts verifying each image.

## 🔬 Methodology

**Methods**:
- Deep Learning Model Training
- Evaluation on Validation Set

**Metrics**:
- Top-1 Accuracy

**Calculation**: Accuracy is calculated using the top-1 accuracy metric based on the predictions made on the test set.

**Interpretation**: Higher top-1 accuracy indicates better performance in correctly identifying SKU-level products.

**Baseline Results**: Top-1 accuracy has reached 64.12% after applying various model fine-tuning tricks.

**Validation**: Validation was performed using a balanced subset of the training data to avoid class imbalance issues.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Available for non-commercial research and educational purposes.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
