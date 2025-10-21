# MONDAY (Mobile OS Navigation Task Dataset for Agents from YouTube)

## 📊 Benchmark Details

**Name**: MONDAY (Mobile OS Navigation Task Dataset for Agents from YouTube)

**Overview**: MONDAY is a large-scale dataset of 313K annotated frames from 20K instructional videos capturing diverse real-world mobile OS navigation tasks across multiple platforms. It enables continuous dataset expansion and demonstrates robust cross-platform generalization capabilities in models trained with it.

**Data Type**: annotated frames

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- AndroidInTheWild
- RICO

**Resources**:
- [Resource](https://monday-dataset.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research in mobile OS navigation by providing a comprehensive dataset for training robust navigation agents.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Mobile OS Navigation
- Task Execution from Instructional Videos

**Limitations**: N/A

## 💾 Data

**Source**: YouTube instructional videos

**Size**: 313,000 frames

**Format**: N/A

**Annotation**: Automated extraction via OCR-based scene detection and UI element identification

## 🔬 Methodology

**Methods**:
- OCR-based scene detection
- UI element detection
- Multi-step action identification

**Metrics**:
- F1 Score

**Calculation**: Metrics calculated through the accuracy of action identification compared to ground truth during evaluations.

**Interpretation**: Higher scores indicate better performance and robustness in action identification across different platforms.

**Baseline Results**: Models showed an average performance gain of 18.11% on an unseen mobile OS platform compared to existing datasets.

**Validation**: Evaluated via manual annotations of extracted actions in the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
