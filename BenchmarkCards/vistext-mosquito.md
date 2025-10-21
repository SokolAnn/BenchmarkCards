# VisText-Mosquito

## 📊 Benchmark Details

**Name**: VisText-Mosquito

**Overview**: VisText-Mosquito is a multimodal dataset integrating visual and textual data to support automated detection, segmentation, and reasoning for mosquito breeding site analysis.

**Data Type**: image-text pairs

**Domains**:
- Public Health
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MosquitoFusion

**Resources**:
- [GitHub Repository](https://github.com/adnanul-islam-jisun/VisText-Mosquito)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for automated detection, segmentation, and reasoning on mosquito breeding sites.

**Target Audience**:
- ML Researchers
- Public Health Professionals

**Tasks**:
- Object Detection
- Image Segmentation
- Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: Collected images from various mosquito breeding habitats across Bangladesh, annotated for object detection and segmentation.

**Size**: 1,828 images for object detection, 142 images for water surface segmentation

**Format**: N/A

**Annotation**: Manual annotation using the Roboflow platform, includes bounding boxes and segmentation masks.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- mAP@50
- BLEU Score
- ROUGE-L
- BERTScore
- Precision
- Recall

**Calculation**: Metrics calculated based on standard evaluation protocols for detection and generation tasks.

**Interpretation**: High values in metrics indicate better performance in detecting mosquito breeding sites and generating coherent reasoning.

**Baseline Results**: YOLOv9s: mAP@50 of 0.92891 for object detection; YOLOv11n-Seg: mAP@50 of 0.79795 for segmentation; Mosquito-LLaMA3-8B: BLEU score of 54.7.

**Validation**: The models were validated using a split of the dataset into training, validation, and testing sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Anonymization techniques applied to protect sensitive location details.

**Data Licensing**: Not Applicable

**Consent Procedures**: Permission obtained from local authorities and property owners.

**Compliance With Regulations**: Not Applicable
