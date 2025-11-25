# IC Dataset (Image Captioning Dataset)

## 📊 Benchmark Details

**Name**: IC Dataset (Image Captioning Dataset)

**Overview**: The IC dataset includes 150 challenging images designed to challenge hallucination control in multimodal large language models, focusing on evaluating precision and recall of image captions.

**Data Type**: image-caption pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Object HallBench

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for effectively evaluating and improving the image captioning capabilities of multimodal large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Image Captioning

**Limitations**: N/A

## 💾 Data

**Source**: 150 challenging images collected across a wide range of domains and scenarios for image captioning tasks.

**Size**: 150 images

**Format**: N/A

**Annotation**: Evaluated using GPT-4o for precision and recall based on generated captions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Precision measures the accuracy of elements in the caption that are present in the image, while Recall assesses the elements in the image that are captured in the caption.

**Interpretation**: Higher precision and recall indicate lower hallucination in captions and better alignment with image content.

**Baseline Results**: N/A

**Validation**: Evaluations compared against existing methods on both the IC dataset and the Object HallBench benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
