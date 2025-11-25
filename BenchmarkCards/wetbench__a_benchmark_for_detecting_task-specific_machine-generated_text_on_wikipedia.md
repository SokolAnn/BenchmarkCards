# WETBench: A Benchmark for Detecting Task-Specific Machine-Generated Text on Wikipedia

## 📊 Benchmark Details

**Name**: WETBench: A Benchmark for Detecting Task-Specific Machine-Generated Text on Wikipedia

**Overview**: WETBench is a multilingual, multi-generator, and task-specific benchmark for detecting machine-generated text on Wikipedia. The benchmark introduces two new datasets across three languages and defines three editing tasks: Paragraph Writing, Summarisation, and Text Style Transfer.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Portuguese
- Vietnamese

**Resources**:
- [GitHub Repository](https://github.com/username/repository)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for assessing the performance of machine-generated text detectors in realistic editorial contexts on Wikipedia.

**Target Audience**:
- ML Researchers
- Wikipedia Editors
- AI Developers

**Tasks**:
- Paragraph Writing
- Summarisation
- Text Style Transfer

**Limitations**: The benchmark does not fully capture how machine-generated text arises in real-world Wikipedia usage and is limited to the evaluated detectors, generators, and tasks.

## 💾 Data

**Source**: Two new Wikipedia text corpora: WikiPS and mWNC, covering English, Portuguese, and Vietnamese.

**Size**: 101,940 texts (human-written and machine-generated)

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Training-based detection
- Zero-shot detection

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the benchmarked detectors' performance across various tasks and languages.

**Interpretation**: Higher accuracy scores indicate better performance of detectors in identifying machine-generated text.

**Baseline Results**: Training-based detectors achieve an average accuracy of 78%.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-SA 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
