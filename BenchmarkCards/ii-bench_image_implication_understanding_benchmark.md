# II-Bench (Image Implication Understanding Benchmark)

## 📊 Benchmark Details

**Name**: II-Bench (Image Implication Understanding Benchmark)

**Overview**: II-Bench is designed to evaluate multimodal large language models' higher-order perception of images, assessing their reasoning and comprehension skills through complex images that convey deeper meanings and implications.

**Data Type**: image

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/m-a-p/II-Bench)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate multimodal large language models' higher-order perceptual, reasoning, and comprehension abilities with complex imagery.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Developers

**Tasks**:
- Image Understanding
- Image Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Images were manually curated and annotated from diverse illustration websites, involving a 3-stage data filtration process.

**Size**: 1,222 images and 1,434 questions

**Format**: N/A

**Annotation**: Images were manually annotated with questions regarding their metaphorical implications by 50 undergraduate students.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is determined by extracting selected options from the model's responses to multiple-choice questions.

**Interpretation**: Higher accuracy indicates better image implication understanding, while significant gaps between model and human performance highlight deficiencies in MLLMs.

**Baseline Results**: Top open-source model: LLaV A-1.6-34B (73.8%), Top closed-source model: Qwen-VL-MAX (74.8%), Average human accuracy: 90.3%

**Validation**: Extensive experimentation conducted on various models across different settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
