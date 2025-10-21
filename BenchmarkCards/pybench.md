# PyBench

## 📊 Benchmark Details

**Name**: PyBench

**Overview**: PyBench is a comprehensive benchmark that evaluates LLM Agents on various real-world coding tasks. It encompasses five main categories: Chart Analysis, Text Analysis, Image & Audio Editing, Complex Math, and Software & Website Development, reflecting daily situations and requiring comprehensive capabilities.

**Data Type**: task-based coding scenarios

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- MBPP
- DS-1000
- DevBench
- SWE-Bench

**Resources**:
- [GitHub Repository](https://github.com/Mercury7353/PyBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the practical coding abilities of LLMs in solving real-world coding tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification
- Object Detection

**Limitations**: N/A

## 💾 Data

**Source**: The data is collected from various sources, including Kaggle (CSV and Excel files), arXiv (PDF and TXT files), and other online sources for images and audio files.

**Size**: N/A

**Format**: Various formats including CSV, XLSX, TXT, PDF, PNG, JPEG, MP3, WAV

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Unit tests
- LLM Evaluator

**Metrics**:
- Pass Rate (UT)
- Pass Rate (LLM)
- Average Turns

**Calculation**: The pass rate is calculated as the percentage of tasks passed by either the Unit Test or the LLM Evaluator within a defined maximum turn limit.

**Interpretation**: Higher pass rates and lower average turns indicate better performance by the LLM Agent on PyBench tasks.

**Baseline Results**: N/A

**Validation**: The tasks are validated through unit tests and peer assessment to ensure comprehensive evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
