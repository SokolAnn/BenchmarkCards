# SimdBench

## 📊 Benchmark Details

**Name**: SimdBench

**Overview**: SimdBench is the first code benchmark specifically designed for SIMD-intrinsic code generation, comprising 136 carefully crafted tasks and targeting five representative SIMD intrinsics: SSE (x86 Streaming SIMD Extension), AVX (x86 Advanced Vector Extension), Neon (ARM Advanced SIMD Extension), SVE (ARM Scalable Vector Extension), and RVV (RISC-V Vector Extension).

**Data Type**: code generation tasks

**Domains**:
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval

**Resources**:
- [Resource](https://anonymous.4open.science/r/SimdBench-1B3F/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of large language models in generating vectorized code with SIMD intrinsics.

**Target Audience**:
- ML Researchers
- Developers
- Compiler Developers

**Tasks**:
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Manually crafted and modified tasks from HumanEval.

**Size**: 136 tasks

**Format**: N/A

**Annotation**: Each task includes functional descriptions, correctness test cases, and performance evaluation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Pass@k
- Speedup
- Efficient@k

**Calculation**: Pass@k represents the mean probability of correctness across tasks; Speedup measures performance improvement relative to scalar implementations.

**Interpretation**: A high pass@k indicates better LLM performance on generating valid SIMD-intrinsic code.

**Baseline Results**: N/A

**Validation**: Tasks validated by correctness tests against canonical scalar solutions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Performance
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
