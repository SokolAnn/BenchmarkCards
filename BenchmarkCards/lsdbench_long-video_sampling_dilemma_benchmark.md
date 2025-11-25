# LSDBench (Long-video Sampling Dilemma Benchmark)

## 📊 Benchmark Details

**Name**: LSDBench (Long-video Sampling Dilemma Benchmark)

**Overview**: LSDBench is the first benchmark designed to evaluate Large Vision-Language Models (LVLMs) on long-video tasks by constructing questions characterized by high Necessary Sampling Density (NSD), addressing the sampling dilemma in long video analysis.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- EgoSchema
- ActivityNet-QA
- LongVideoBench

**Resources**:
- [GitHub Repository](https://github.com/dvlab-research/LSDBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standard evaluation for LVLMs in high-NSD scenarios, focusing on sampling efficiency and performance in long-video tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: 400 videos with corresponding action narrations annotated by human provided by EGO4D.

**Size**: 1304 QA pairs

**Format**: N/A

**Annotation**: Fully automated QA generation pipeline with a two-round filtering process.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on model performance on the LSDBench dataset through question answering tasks.

**Interpretation**: Good performance is indicated by higher accuracy rates in answering questions while managing sampling efficiency.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
