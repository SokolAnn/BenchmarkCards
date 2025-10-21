# OmniDocBench

## 📊 Benchmark Details

**Name**: OmniDocBench

**Overview**: OmniDocBench is a novel benchmark featuring high-quality annotations across nine document sources, aimed at evaluating diverse PDF document parsing methods through flexible, multi-level evaluations.

**Data Type**: PDF pages with comprehensive annotations for layout and content recognition

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- PubLayNet
- DocBank
- TableBank

**Resources**:
- [GitHub Repository](https://github.com/opendatalab/OmniDocBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous and comprehensive evaluation for document parsing models across pipeline-based and end-to-end paradigms.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Document Parsing
- Content Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Diverse origins including academic papers, textbooks, handwritten notes, and newspapers.

**Size**: 981 pages

**Format**: PDF

**Annotation**: Annotated using a combination of automated tools and expert review processes.

## 🔬 Methodology

**Methods**:
- End-to-end evaluation
- Task-specific evaluation
- Attribute-based evaluation

**Metrics**:
- Normalized Edit Distance
- Tree-Edit-Distance-based Similarity (TEDS)
- Character Detection Matching (CDM)

**Calculation**: Metrics are calculated based on comparison between model outputs and ground truth annotations.

**Interpretation**: Scores are averaged at the sample level to obtain final results, with specific thresholds applied for matching.

**Baseline Results**: N/A

**Validation**: Evaluation procedures ensured through a comprehensive pipeline involving element extraction, matching algorithms, and metric calculations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
