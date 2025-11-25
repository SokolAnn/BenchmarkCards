# CapArena (Detailed Image Captioning Benchmark)

## 📊 Benchmark Details

**Name**: CapArena (Detailed Image Captioning Benchmark)

**Overview**: CapArena is an evaluation platform designed to benchmark the performance of vision-language models (VLMs) in generating detailed image captions through a series of pairwise caption battles and human preference votes.

**Data Type**: captioning pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MSCOCO

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark the detailed captioning capabilities of vision-language models and analyze their performance in comparison to human annotators.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Image Captioning

**Limitations**: N/A

## 💾 Data

**Source**: DOCCI dataset, consisting of high-resolution images and human-annotated detailed descriptions.

**Size**: 6,522 instances

**Format**: N/A

**Annotation**: Manual annotation through human preference voting in a pairwise battle format.

## 🔬 Methodology

**Methods**:
- Human evaluation
- VLM-as-a-Judge evaluation

**Metrics**:
- Correlation with human preferences

**Calculation**: Metrics are derived from human rankings based on pairwise comparisons in caption battles.

**Interpretation**: A higher correlation score indicates better alignment with human judgments.

**Baseline Results**: High correlation with human annotations at 94.3% in the automated benchmark.

**Validation**: Inter-annotator agreement tested with a score of 0.782.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
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
