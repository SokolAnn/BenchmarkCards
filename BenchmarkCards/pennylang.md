# PennyLang

## 📊 Benchmark Details

**Name**: PennyLang

**Overview**: PennyLang is a high-quality dataset of 3,347 PennyLane-specific quantum code samples with contextual descriptions, curated from textbooks, official documentation, and open-source repositories, designed for quantum programming using PennyLane.

**Data Type**: code samples

**Domains**:
- Quantum Computing

**Languages**:
- Python

**Resources**:
- [GitHub Repository](https://github.com/PennyLaneAI)

## 🎯 Purpose and Intended Users

**Goal**: To provide a structured dataset specifically for LLM-based quantum code generation and assist developers in writing optimized quantum code using PennyLane.

**Target Audience**:
- ML Researchers
- Quantum Software Developers

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Curated from GitHub repositories, quantum computing textbooks, and official PennyLane documentation.

**Size**: 3,347 samples

**Format**: JSON

**Annotation**: Manual verification and contextual descriptions added to each code sample.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Success Rate

**Calculation**: Success Rate is calculated as pass@5 / 264 x 100, where pass@5 indicates the number of test cases for which at least one correct solution was generated among the five attempts.

**Interpretation**: Higher success rates indicate better model performance in generating correct quantum code.

**Baseline Results**: Open-source models like Qwen 7B and LLaMa 4 showed significant improvements when evaluated with the PennyLang dataset.

**Validation**: Evaluated through a benchmark suite comprising 264 test cases assessed across multiple LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
