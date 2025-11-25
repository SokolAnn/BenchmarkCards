# Neptune

## 📊 Benchmark Details

**Name**: Neptune

**Overview**: Neptune is a benchmark for long video understanding requiring reasoning over long time horizons and across different modalities. It covers a broad range of long video reasoning abilities, including dense, time-aligned video captions and challenging question-answer-decoy sets for video segments.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- EgoSchema
- 1H-VideoQA
- ActivityNet-QA

**Resources**:
- [GitHub Repository](https://github.com/google-deepmind/neptune)

## 🎯 Purpose and Intended Users

**Goal**: To spur the development of more advanced models capable of understanding long videos and to provide a comprehensive evaluation framework for video question answering tasks.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Question Answering
- Video Summarization
- Visual Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Automated YouTube video selection and processing pipeline

**Size**: 3,268 questions across 2,405 videos

**Format**: JSON

**Annotation**: Semi-automated with manual rater verification

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Gemma Equivalence Metric (GEM)

**Calculation**: Metrics are calculated based on matching candidate answers to reference answers, with evaluations derived from human-annotated equivalence.

**Interpretation**: Good performance is indicated by the ability to closely match human judgment on answer equivalence; underperformance shows a significant gap in understanding long videos.

**Baseline Results**: Performance comparisons made against state-of-the-art models such as Gemini-1.5-pro and Video-LLaMA2

**Validation**: Tested against a variety of state-of-the-art video understanding models including both open-source and proprietary systems.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency
- **Societal Impact**: Impact on cultural diversity

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset leverages publicly available videos under the assumption of consent for academic use.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
