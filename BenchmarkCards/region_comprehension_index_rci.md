# Region Comprehension Index (RCI)

## 📊 Benchmark Details

**Name**: Region Comprehension Index (RCI)

**Overview**: RCI is the first model-based score to explicitly quantify a dataset's reliance on global versus local visual information in multimodal benchmarks, aiding researchers and practitioners in auditing and aligning benchmarks with real-world reasoning needs.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MS COCO
- GQA
- TextVQA
- VizWiz

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation framework for quantifying reasoning requirements in multimodal datasets and benchmarks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Dataset Designers

**Tasks**:
- Visual Question Answering
- Multiple-Choice Question Answering
- Yes/No Classification

**Limitations**: N/A

## 💾 Data

**Source**: Evaluated across 13 widely used multimodal benchmarks including AI2D, BLINK, and CHARTQA.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Model-based evaluation
- Patch-based assessment

**Metrics**:
- Region Comprehension Index (RCI)

**Calculation**: RCI is calculated as RCI_n = 1 - (Maximum Patch Performance (MPP_n) / Full Image Performance (FIP)).

**Interpretation**: RCI values indicate the type of reasoning required: RCI > 0 indicates strong global reasoning needed; RCI < 0 indicates reliance on localized cues.

**Baseline Results**: N/A

**Validation**: RCI is validated when the Full Image Performance exceeds chance thresholds.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
