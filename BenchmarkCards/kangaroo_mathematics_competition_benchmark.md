# Kangaroo Mathematics Competition Benchmark

## 📊 Benchmark Details

**Name**: Kangaroo Mathematics Competition Benchmark

**Overview**: This paper presents a benchmark to evaluate the mathematical problem-solving capabilities of Multimodal Large Language Models (MLLMs) using a multilingual dataset based on the Kangaroo Mathematics Competition, testing models across geometry, visual algebra, logic, patterns, and combinatorics.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English
- French
- Spanish
- Catalan

**Similar Benchmarks**:
- Geometry3K
- MathVista
- NPHardEval4V

**Resources**:
- [GitHub Repository](https://github.com/QwenLM/Qwen2.5-VL)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of MLLMs in solving mathematical problems across multiple languages, particularly those involving visual elements.

**Target Audience**:
- ML Researchers
- Educators
- Model Developers

**Tasks**:
- Mathematical Reasoning
- Visual Question Answering

**Limitations**: No single model excels uniformly across all topics, and substantial variation exists across languages and difficulty levels.

## 💾 Data

**Source**: Kangaroo Mathematics Competition tests collected from 2014-2024 across different languages

**Size**: N/A

**Format**: CSV

**Annotation**: Automatically generated based on structured formats for test questions

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on correct answers supported by reasoning against ground truth.

**Interpretation**: Models show varying capabilities in reasoning, with few achieving human-level performance.

**Baseline Results**: Gemini 2.0 Flash achieved the highest accuracy in image-based tasks at 45.4%.

**Validation**: Evaluations conducted on multilingual datasets comparing model responses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Analysis of performance variations across different demographic groups in the evaluated languages.

**Potential Harm**: ['Unrepresentative data']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
