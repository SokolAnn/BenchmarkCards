# PATENT DESC-355K

## 📊 Benchmark Details

**Name**: PATENT DESC-355K

**Overview**: We introduce PATENT DESC-355K, a novel large-scale dataset containing ∼355K patent figures along with their brief and detailed textual descriptions extracted from 60K+ US patent documents.

**Data Type**: image-description pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- COCO
- TextCaps
- NoCaps

**Resources**:
- [Resource](https://vl2g.github.io/projects/PatentLMM/)

## 🎯 Purpose and Intended Users

**Goal**: To automate the understanding of patent figures, enabling efficient knowledge sharing and faster drafting of patent documents.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Image Captioning

**Limitations**: N/A

## 💾 Data

**Source**: Curated from over 60K US patent documents and their corresponding descriptions.

**Size**: 355,000 images

**Format**: N/A

**Annotation**: Descriptions extracted from HTML documents of patents.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU Score
- ROUGE-L
- METEOR

**Calculation**: Based on standard image captioning metrics comparing generated and ground-truth descriptions.

**Interpretation**: Higher scores indicate better match to human-generated descriptions.

**Baseline Results**: Outperforms existing models by significant margins.

**Validation**: Cross-validated across training, validation, and test sets.

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
