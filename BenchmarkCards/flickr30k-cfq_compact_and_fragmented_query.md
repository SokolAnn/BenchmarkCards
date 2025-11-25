# Flickr30K-CFQ (Compact and Fragmented Query)

## 📊 Benchmark Details

**Name**: Flickr30K-CFQ (Compact and Fragmented Query)

**Overview**: We introduce a new Compact and Fragmented Query dataset to the text-image retrieval community, named Flickr30K-CFQ, which is used to model natural text-image retrieval in real-world scenarios.

**Data Type**: text-image pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MS-COCO
- Flickr30K

**Resources**:
- [Resource](https://sites.google.com/view/Flickr30K-cfq)

## 🎯 Purpose and Intended Users

**Goal**: To model natural text-image retrieval in real-world scenarios by providing a dataset that overcomes the limitations of existing vision-language datasets.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Text-Image Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Flickr30K Entities and generated through prompt engineering with LLMs

**Size**: 31,783 images, 158,915 captions, 305 imagery tags, 111,240 phrases, 133,540 triples, 139,607 fragments

**Format**: N/A

**Annotation**: Manually annotated noun phrases and images, along with generated imagery tags and triples

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Multi-recall@K
- Recall@K

**Calculation**: Metrics are calculated based on the similarity of image-text pairs and performance improvements via query enhancement.

**Interpretation**: The performance improvement indicates the effectiveness of the LLM-based Query-enhanced method in text-image retrieval.

**Baseline Results**: Existing methods on the full-scale Flickr30K-CFQ dataset showed significant performance drops compared to previous benchmarks.

**Validation**: Results validated through experiments on the proposed dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
