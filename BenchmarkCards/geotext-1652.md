# GeoText-1652

## 📊 Benchmark Details

**Name**: GeoText-1652

**Overview**: GeoText-1652 is a new natural language-guided geolocalization benchmark that provides fine-grained spatial-aware text annotations for an existing image dataset, aimed at facilitating drone navigation and target localization tasks.

**Data Type**: image-text-bbox pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- University-1652

**Resources**:
- [Resource](https://multimodalgeo.github.io/GeoText/)

## 🎯 Purpose and Intended Users

**Goal**: To enhance natural language-guided drone geolocalization and address the challenges of dataset availability and the alignment of language with fine-grained visual representations.

**Target Audience**:
- ML Researchers
- Drone Developers
- Robotics Engineers

**Tasks**:
- Text-to-Image Retrieval
- Image-to-Text Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Built upon the University-1652 image dataset, with spatial-aware text annotations created through a human-computer interaction annotation process.

**Size**: 276,045 text-bbox pairs and 316,335 descriptions

**Format**: N/A

**Annotation**: Generated through an interactive human-computer process leveraging Large Language Model-driven annotation techniques.

## 🔬 Methodology

**Methods**:
- Image-text contrastive learning
- Cross-modal retrieval
- Spatial relation matching

**Metrics**:
- Recall@1
- Recall@5
- Recall@10

**Calculation**: Metrics calculated based on similarity scores between image and text representations using cosine similarity.

**Interpretation**: Higher Recall@K indicates a better performance in retrieving relevant images or text descriptions related to the input queries.

**Baseline Results**: Achieved 31.2% Recall@10 accuracy surpassing established models such as ALBEF and XVLM.

**Validation**: Evaluated using human feedback and comparison against baseline models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
