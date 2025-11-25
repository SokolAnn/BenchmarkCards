# IllusionBench

## 📊 Benchmark Details

**Name**: IllusionBench

**Overview**: IllusionBench is a dataset that challenges current vision-language models (VLMs) to decipher shape information represented by an arrangement of visual elements in coherent, naturalistic scenes. It evaluates the shape recognition capabilities of VLMs, highlighting their limitations in detecting abstract shapes within these scenes.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- Stylized-ImageNet

**Resources**:
- [Resource](https://huggingface.co/datasets/arshiahemmat/IllusionBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate shape recognition capabilities in vision-language models and to identify their limitations in detecting abstract shapes within scenes.

**Target Audience**:
- ML Researchers
- Computer Vision Practitioners

**Tasks**:
- Shape Recognition
- Object Recognition

**Limitations**: The current benchmark only hides a single shape in each image, limiting complexity. Future work aims to create more complex images with multiple objects.

## 💾 Data

**Source**: Generated images using a diffusion model based on ControlNet.

**Size**: 32,000 images

**Format**: PNG

**Annotation**: Human annotations were performed to verify the recognizability of shapes in the generated dataset.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- In-context learning

**Metrics**:
- Shape Recall
- Scene Recall

**Calculation**: Shape and scene recall are calculated as the proportion of correctly identified shapes and scenes across all samples in the datasets.

**Interpretation**: Higher recall values indicate better performance in identifying abstract shapes in visual scenes.

**Baseline Results**: Prior benchmarks like Stylized-ImageNet show higher recall for shapes, while VLMs struggle with IllusionBench.

**Validation**: Participants validated results through manual annotation, achieving high average accuracy in recognizing shapes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: The limited shape perception abilities of current VLMs could be exploited for undesirable purposes such as content moderation failures.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-NC 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
