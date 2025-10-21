# ViSa

## 📊 Benchmark Details

**Name**: ViSa

**Overview**: ViSa is a large dataset for benchmarking the video subtitle extraction task, containing a total of 2.5M videos for pre-training, 230K for supervised fine-tuning, and 1.6K for testing.

**Data Type**: video

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese
- English

**Resources**:
- [GitHub Repository](https://github.com/jianchang512/pyvideotrans)

## 🎯 Purpose and Intended Users

**Goal**: To support and benchmark the task of end-to-end video subtitle extraction.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Video Subtitle Extraction

**Limitations**: N/A

## 💾 Data

**Source**: The dataset was constructed from the CNVid and MovieChat datasets.

**Size**: 2.5M videos

**Format**: N/A

**Annotation**: Each video is annotated with subtitle text tracking and recognition.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation

**Metrics**:
- Normalized Edit Distance
- SubER

**Calculation**: Metrics are calculated based on predicted subtitles against ground truth.

**Interpretation**: Lower Normalized Edit Distance and SubER indicate better performance in subtitle extraction.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
