# Binary Code Understanding Benchmark

## 📊 Benchmark Details

**Name**: Binary Code Understanding Benchmark

**Overview**: This work proposes a benchmark to evaluate the effectiveness of Large Language Models (LLMs) in real-world reverse engineering scenarios, focusing on two key binary code understanding tasks: function name recovery and binary code summarization.

**Data Type**: binary code understanding tasks

**Domains**:
- Software Security

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/Sxxxw/BinaryLLMs-Eval)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate the capabilities of LLMs for understanding binary code in software security.

**Target Audience**:
- ML Researchers
- Software Security Practitioners

**Tasks**:
- Function Name Recovery
- Binary Code Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from real-world projects implemented in C, including binaries with multiple target architectures and optimization options.

**Size**: 2000 functions

**Format**: Binary and pseudo code

**Annotation**: Ground-truth generated using ChatGPT for function summaries.

## 🔬 Methodology

**Methods**:
- Automated evaluation
- Human evaluation

**Metrics**:
- BLEU-4
- METEOR
- Rouge-L
- Precision
- Recall
- F1 Score

**Calculation**: Various metrics calculated for function name recovery and binary code summarization based on generated outputs.

**Interpretation**: Higher scores indicate better performance of models in understanding binary code meaning and functionality.

**Baseline Results**: N/A

**Validation**: The benchmark was validated using expert reviews for correctness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
