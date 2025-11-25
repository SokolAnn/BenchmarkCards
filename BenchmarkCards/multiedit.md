# MultiEdit

## 📊 Benchmark Details

**Name**: MultiEdit

**Overview**: MultiEdit is a comprehensive dataset for advancing instruction-based image editing, featuring over 107K samples across 6 challenging editing tasks, which includes 18 non-style-transfer editing types and 38 style transfer operations.

**Data Type**: image-editing samples

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- EmuEdit

**Resources**:
- [Resource](https://huggingface.co/datasets/inclusionAI/MultiEdit)

## 🎯 Purpose and Intended Users

**Goal**: To provide a valuable resource that facilitates research into more diverse and challenging instruction-based image editing capabilities.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Image Editing

**Limitations**: N/A

## 💾 Data

**Source**: MultiEdit comprises samples collected from various image datasets, specifically designed to address complex editing tasks.

**Size**: 107,634 samples

**Format**: N/A

**Annotation**: Generated using a multi-modal large language model context.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- CLIP img
- DINO
- L1
- L2

**Calculation**: Metrics are calculated based on the performance of models fine-tuned on the MultiEdit-Train set against the MultiEdit-Test benchmark.

**Interpretation**: Higher scores indicate better model performance on the image editing tasks.

**Baseline Results**: Various models tested including Stable Diffusion and UltraEdit, with improvements noted post fine-tuning on the MultiEdit dataset.

**Validation**: Extensive experiments validate the dataset through comparisons with baseline models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
