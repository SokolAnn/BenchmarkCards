# VIDHAL

## 📊 Benchmark Details

**Name**: VIDHAL

**Overview**: VIDHAL is a benchmark specifically designed to evaluate video-based hallucinations in Vision Large Language Models (VLLMs). It features a diverse range of video instances annotated with captions exhibiting varying levels of hallucination.

**Data Type**: Video

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMHalBench
- Hallu-sionBench
- AMBER

**Resources**:
- [GitHub Repository](https://github.com/Lookuz/VidHal)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating hallucinations in VLLMs using video data.

**Target Audience**:
- Researchers
- Developers
- Practitioners

**Tasks**:
- Evaluating hallucination generation
- Understanding spatiotemporal responses
- Fine-grained caption ordering

**Limitations**: The benchmark uniquely focuses on video hallucinations, excluding text-only or image-only evaluation.

**Out of Scope Uses**:
- Non-video language model evaluations
- Comparative studies on image-only benchmarks

## 💾 Data

**Source**: Public video understanding datasets including TempCompass, MVBench, Perception Test, and AutoEval-Video.

**Size**: 1,000 video instances

**Format**: Annotated videos with multiple captions

**Annotation**: Captions that demonstrate varying levels of hallucinations.

## 🔬 Methodology

**Methods**:
- Video annotation
- Caption generation using VLLMs
- Human validation for accuracy assessment

**Metrics**:
- Multiple-Choice Question Answering (MCQA)
- NDCG for caption ranking

**Calculation**: Accuracy is calculated based on match rates between generated captions and ground truth.

**Interpretation**: Higher accuracy indicates better performance in understanding and reducing hallucinations.

**Validation**: Data was validated by human annotators to ensure reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness Risk
- Privacy Risk
- Robustness Risk

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Privacy**: Personal information in data
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset respects user privacy and anonymity protocols.

**Data Licensing**: Data sourced from public datasets that allow for academic use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The dataset conforms to relevant data usage regulations.
