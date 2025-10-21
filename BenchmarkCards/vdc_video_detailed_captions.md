# VDC (Video Detailed Captions)

## 📊 Benchmark Details

**Name**: VDC (Video Detailed Captions)

**Overview**: VDC is a video detailed captioning benchmark featuring over one thousand high-quality video-caption pairs, providing significantly longer and more detailed captions than existing benchmarks.

**Data Type**: video-caption pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MSVD
- MSR-VTT
- VATEX

**Resources**:
- [GitHub Repository](https://github.com/InternLM/xtuner)
- [GitHub Repository](https://github.com/EvolvingLMMs-Lab/lmms-eval)
- [GitHub Repository](https://github.com/sgl-project/sglang)

## 🎯 Purpose and Intended Users

**Goal**: To advance the field of video detailed captioning by providing a dataset with structured, high-quality captions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Video Captioning
- Evaluation of Captioning

**Limitations**: N/A

## 💾 Data

**Source**: Videos sourced from Panda-70M, Ego4D, Mixkit, Pixabay, Pexels

**Size**: 1,027 videos

**Format**: N/A

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- CIDEr
- BLEU
- ROUGE-L
- VDCscore

**Calculation**: Metrics are calculated using the generated video captions compared to ground truth structured captions.

**Interpretation**: Higher scores indicate better alignment of generated captions with human expectations.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Generating misleading captions']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
