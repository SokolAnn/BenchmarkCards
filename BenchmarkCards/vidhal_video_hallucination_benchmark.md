# VIDHAL (Video Hallucination Benchmark)

## 📊 Benchmark Details

**Name**: VIDHAL (Video Hallucination Benchmark)

**Overview**: VIDHAL is a benchmark specifically designed to evaluate video-based hallucinations in Vision Large Language Models (VLLMs). It includes video instances sourced from public datasets with annotations representing varying levels of hallucination, enabling fine-grained evaluation of VLLMs through a novel caption ordering task.

**Data Type**: video-caption pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Lookuz/VidHal)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and benchmark the performance of Vision Large Language Models (VLLMs) in understanding and generating video content without hallucination.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Video Question Answering
- Caption Ordering

**Limitations**: N/A

## 💾 Data

**Source**: Public video understanding datasets (TempCompass, Perception Test, MVBench, AutoEval-Video)

**Size**: 1,000 video instances

**Format**: N/A

**Annotation**: Video instances annotated with multiple captions of varying degrees of hallucination.

## 🔬 Methodology

**Methods**:
- Multiple-choice question answering (MCQA)
- Caption ordering

**Metrics**:
- MCQA Accuracy
- Normalized Discounted Cumulative Gain (NDCG)

**Calculation**: Accuracy is calculated based on the proportion of correct answers in the MCQA task and on the ranking of captions in the caption ordering task.

**Interpretation**: A higher accuracy score indicates better performance, with the NDCG metric capturing the ranked order of captions and rewarding partially correct rankings.

**Baseline Results**: N/A

**Validation**: Human validation was performed to ensure the reliability of the generated captions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
