# COCO-Urdu

## 📊 Benchmark Details

**Name**: COCO-Urdu

**Overview**: COCO-Urdu is the largest Urdu image-caption dataset to date, created by translating and validating a balanced subset of MS COCO, containing 59,000 images and 319,000 Urdu captions with a multimodal quality estimation framework.

**Data Type**: image-caption pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- Urdu

**Similar Benchmarks**:
- UICD
- Flickr8k Urdu

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To advance multimodal research for low-resource languages by providing a large-scale Urdu image caption dataset and a systematic hybrid quality estimation framework.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Image Captioning

**Limitations**: Human evaluation was restricted to 200 captions due to budget and time constraints.

## 💾 Data

**Source**: Derived from MS COCO.

**Size**: 59,000 images and 319,000 Urdu captions

**Format**: N/A

**Annotation**: Translated captions validated with a hybrid multimodal quality estimation framework.

## 🔬 Methodology

**Methods**:
- Quality estimation using COMET-Kiwi, BERTScore, and CLIP-based visual grounding
- Iterative refinement of low-scoring captions

**Metrics**:
- BLEU
- SacreBLEU
- chrF

**Calculation**: Metrics are calculated based on translation quality and visual grounding consistency.

**Interpretation**: Higher scores indicate better translation fidelity and visual-text alignment.

**Baseline Results**: COCO-Urdu achieves BLEU scores of 0.53 (Refined) and 0.52 (Zero-shot).

**Validation**: The dataset was validated using reference-free and reference-based evaluation metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The COCO-Urdu dataset is released under CC BY 4.0, allowing modifications and adaptations with proper attribution.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
