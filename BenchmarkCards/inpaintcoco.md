# InpaintCOCO

## 📊 Benchmark Details

**Name**: InpaintCOCO

**Overview**: InpaintCOCO is a new challenging dataset for assessing the fine-grained alignment of colors, objects, and sizes in vision-language models, created using generative inpainting from COCO images by altering visual concepts.

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- ARO
- VL-CheckList
- SVO

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To enhance fine-grained concept understanding in vision-language models through a new dataset and a novel pretraining method with synthetic hard negative samples.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Question Answering
- Text-to-Image Retrieval

**Limitations**: The dataset only includes minor changes to visual components, which may not generalize well outside the Western context.

## 💾 Data

**Source**: Generative inpainting from COCO images, creating adversarial examples to evaluate models

**Size**: 1,260 images

**Format**: Inpainted images with textual descriptions

**Annotation**: Manual annotation by student workers with specific guidelines for generating hard negatives

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Recall@5

**Calculation**: Model performance is calculated based on ranking evaluation for fine-grained understanding and retrieval capabilities.

**Interpretation**: Accuracy measures how well specific visual concepts are learned, while Recall@5 indicates general retrieval performance.

**Baseline Results**: Original OpenAI CLIP model, classical pre-trained CLIP model, models trained with 1, 2, or 3 hard negatives per batch.

**Validation**: Extensive evaluations across various vision-language datasets to verify robustness and performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Potential for misuse in large-scale video surveillance and bias toward Western perspectives

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Images from COCO follow Creative Commons Attribution 4.0 License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
