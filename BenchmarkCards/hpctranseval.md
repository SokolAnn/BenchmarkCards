# HPCTransEval

## 📊 Benchmark Details

**Name**: HPCTransEval

**Overview**: HPCTransEval is a benchmark for evaluating LLM performance on CUDA transpilation, including 100 standalone operators, 100 computation graphs built from these operators, and 10 building blocks for deep learning models.

**Data Type**: CUDA-CPU code pairs

**Domains**:
- High-Performance Computing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/PJLAB-CHIP/HPCTransCompile)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust benchmark for evaluating LLM performance in CUDA transpilation.

**Target Audience**:
- ML Researchers
- Software Developers
- AI Practitioners

**Tasks**:
- Code Transpilation

**Limitations**: N/A

## 💾 Data

**Source**: Automatically generated high-performance CUDA and corresponding platform code pairs using AI compiler and optimization techniques.

**Size**: 20,000 code pairs

**Format**: N/A

**Annotation**: Includes function-level annotations from professional high-performance engineers.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Compile Pass
- Execute Pass
- Speedup Ratio

**Calculation**: Metrics calculated based on the performance of generated CPU code compared to original code.

**Interpretation**: Higher values indicate better performance in compiling and executing the translated code.

**Baseline Results**: N/A

**Validation**: Evaluated against three leading LLMs: Qwen2.5-Coder, DeepSeek-Coder-V2, and OpenCoder.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
