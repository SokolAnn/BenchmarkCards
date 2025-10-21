# JsDeObsBench (JavaScript Deobfuscation Benchmark)

## 📊 Benchmark Details

**Name**: JsDeObsBench (JavaScript Deobfuscation Benchmark)

**Overview**: JsDeObsBench is a dedicated benchmark designed to rigorously evaluate the effectiveness of large language models (LLMs) in the context of JavaScript (JS) deobfuscation, incorporating a wide range of obfuscation techniques and providing a robust framework for assessing LLM performance.

**Data Type**: JavaScript programs

**Domains**:
- Security

**Languages**:
- JavaScript

**Resources**:
- [GitHub Repository](https://github.com/Ch3nYe/JsDeObsBench)
- [Resource](https://jsdeobf.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for the capabilities of large language models in deobfuscating JavaScript code.

**Target Audience**:
- ML Researchers
- Security Analysts
- Model Developers

**Tasks**:
- Code Deobfuscation

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from a large-scale and execution-verifiable dataset with 36,260 unique obfuscated JavaScript programs and 4,515 malicious obfuscated programs.

**Size**: 36,260 unique obfuscated JavaScript programs and 4,515 malicious obfuscated JavaScript programs

**Format**: Dataset of JavaScript files

**Annotation**: Automatically generated from various obfuscation transformations applied to JavaScript code.

## 🔬 Methodology

**Methods**:
- Automated evaluation metrics
- Experimental evaluation on LLMs

**Metrics**:
- Syntax Correctness
- Execution Correctness
- Code Simplification Score
- Code Similarity Score

**Calculation**: Metrics are calculated based on the correctness of the deobfuscated code against the original, examining syntax, semantics, complexity, and readability.

**Interpretation**: Higher scores indicate better performance in accurately deobfuscating JS code and maintaining its readability.

**Baseline Results**: Compared against state-of-the-art deobfuscators including JS-deobfuscator and Synchrony.

**Validation**: Validated through a systematic evaluation of code snippets deobfuscated by state-of-the-art LLMs and existing baselines.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy
- Safety

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Privacy**: Personal information in data
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential for data leakage through malicious code analysis.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
