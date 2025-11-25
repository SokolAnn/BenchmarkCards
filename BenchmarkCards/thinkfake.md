# ThinkFake

## 📊 Benchmark Details

**Name**: ThinkFake

**Overview**: ThinkFake is a reasoning-based framework for AI-generated image detection leveraging Multimodal Large Language Models (MLLMs) with a focus on providing interpretable reasoning and generalization capabilities. It outperforms existing state-of-the-art methods and demonstrates robust performance across various benchmarks.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- GenImage
- LOKI

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the detection of AI-generated images using a reasoning framework that provides interpretable outputs.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Image Detection

**Limitations**: The model requires significant computational resources during training, and real-time detection during inference remains challenging.

## 💾 Data

**Source**: Real images from ImageNet and fake images generated using SD v1.4 based on ImageNet labels.

**Size**: 6,000 examples

**Format**: N/A

**Annotation**: Automated generated reasoning paths and attribute-level answers based on prompts.

## 🔬 Methodology

**Methods**:
- Reinforcement Learning
- Supervised Fine-tuning
- Ablation Studies

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the model's predictions compared to ground-truth labels.

**Interpretation**: Higher accuracy indicates better performance in distinguishing between real and AI-generated images.

**Baseline Results**: Strong generalization on the LOKI benchmark and superior performance on the GenImage benchmark.

**Validation**: Extensive experiments, including ablation studies, to validate reasoning capabilities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
