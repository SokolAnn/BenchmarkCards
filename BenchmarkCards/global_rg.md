# GLOBAL RG

## 📊 Benchmark Details

**Name**: GLOBAL RG

**Overview**: The GLOBAL RG benchmark comprises two tasks: retrieval across universals and cultural visual grounding. The retrieval task entails retrieving culturally diverse images for universal concepts from 50 countries, while the grounding task aims at grounding culture-specific concepts within images from 15 countries.

**Data Type**: image

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://globalrg.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the multicultural understanding of vision-language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Image Retrieval
- Visual Grounding

**Limitations**: Cultural coverage is limited to 15 cultures for grounding task; represents a selected set of cultural keywords.

## 💾 Data

**Source**: Images collected from Google Images using human universals and cultural keywords extracted from CANDLE.

**Size**: 3,000 images for retrieval task; 591 images for grounding task.

**Format**: N/A

**Annotation**: Annotated by cultural experts who drew bounding boxes around relevant concepts.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Precision@k
- Diversity@k
- Intersection over Union (IoU)

**Calculation**: Precision measures correctness of retrieved images; diversity uses entropy to measure cultural diversity among retrieved images; IoU assesses correctness of predicted bounding boxes.

**Interpretation**: Higher precision indicates better retrieval performance; higher diversity denotes a better representation of multiple cultures.

**Baseline Results**: Performance was reported for several state-of-the-art models, such as CLIP, OpenCLIP, and CoCA.

**Validation**: Extensive evaluation across multiple vision-language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Cultural representation analysis across various regions and demographics.

**Potential Harm**: Inadvertent reinforcement of stereotypes through cultural imagery.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
