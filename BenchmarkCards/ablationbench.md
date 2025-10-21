# AblationBench

## 📊 Benchmark Details

**Name**: AblationBench

**Overview**: AblationBench is a benchmark suite for evaluating agents on ablation planning tasks in empirical AI research. It includes two tasks: AuthorAblation, which assists authors in proposing ablation experiments, and ReviewerAblation, which helps reviewers find missing ablations in a paper.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- CiteME
- LitSearch
- PaperQA2

**Resources**:
- [Resource](https://arxiv.org/abs/2507.08038)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation resource for developing ablation agents in empirical AI research.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Ablation Planning
- Text Normalization

**Limitations**: N/A

## 💾 Data

**Source**: Original research papers and ICLR submissions containing ablation studies.

**Size**: 433 instances (83 for AuthorAblation, 350 for ReviewerAblation)

**Format**: JSON

**Annotation**: Manual annotation of ablation examples and missing ablation suggestions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on the matches between generated ablations and ground truth ablations.

**Interpretation**: Higher precision indicates a better match of proposed ablations to actual ablations, while higher recall indicates comprehensive identification of relevant ablations.

**Baseline Results**: The best LM planners identify at most 34% of ablations in AuthorAblation and 26% in ReviewerAblation.

**Validation**: Performance assessed against a dedicated evaluation dataset with human annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
