# VulDetectBench

## 📊 Benchmark Details

**Name**: VulDetectBench

**Overview**: VulDetectBench is a new benchmark specifically designed to assess the vulnerability detection capabilities of Large Language Models (LLMs). It evaluates LLMs' ability to identify, classify, and locate vulnerabilities through five tasks of increasing difficulty.

**Data Type**: vulnerability detection tasks

**Domains**:
- Computer Security

**Languages**:
- C
- C++

**Resources**:
- [GitHub Repository](https://github.com/Sweetaroo/VulDetectBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark that evaluates the vulnerability detection capabilities of various LLMs through a structured set of tasks.

**Target Audience**:
- ML Researchers
- Security Analysts
- Model Developers

**Tasks**:
- Vulnerability Existence Detection
- CWE Type Inference
- Key Objects and Functions Identification
- Root Cause Location
- Trigger Point Location

**Limitations**: Although VulDetectBench provides a comprehensive evaluation, it currently focuses on C/C++ programming languages and can be expanded to include other languages in the future.

## 💾 Data

**Source**: The benchmark dataset is constructed from high-quality datasets of code vulnerabilities, including real-world datasets collected from open-source projects and the National Institute of Standards and Technology (NIST) Software Assurance Reference Dataset (SARD).

**Size**: 1,000 vulnerability samples for Task 1, 500 for Task 2, and 100 for Tasks 3, 4, and 5.

**Format**: JSON

**Annotation**: Annotated with detailed classification, descriptions, and key information about associated vulnerabilities.

## 🔬 Methodology

**Methods**:
- Automated evaluation
- Performance comparison

**Metrics**:
- Accuracy
- F1 Score
- Macro Recall (MAR)
- Micro Recall (MIR)
- Unified Recall Score (URS)

**Calculation**: Metrics are calculated based on model outputs against correct answers.

**Interpretation**: Higher scores indicate better performance in identifying and analyzing vulnerabilities.

**Baseline Results**: Various LLMs were evaluated, with GPT-4 achieving the highest reported accuracy and F1 Score.

**Validation**: The benchmark is validated through comprehensive model evaluations across the established tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Limited demographic analysis since the benchmark primarily focuses on code vulnerability types.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
