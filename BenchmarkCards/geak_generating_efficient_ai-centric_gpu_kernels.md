# GEAK (Generating Efficient AI-centric GPU Kernels)

## 📊 Benchmark Details

**Name**: GEAK (Generating Efficient AI-centric GPU Kernels)

**Overview**: GEAK is a framework that leverages cutting-edge LLMs to generate performant Triton code specifically for AMD GPUs, including the AMD Instinct ™MI300X and MI250. We introduce two benchmark suites for evaluating AI-generated Triton kernels, enabling measurement of both execution correctness and runtime performance of generated kernels.

**Data Type**: GPU kernel code

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- TritonBench
- KernelBench

**Resources**:
- [GitHub Repository](https://github.com/user/repo1)
- [GitHub Repository](https://github.com/user/repo2)

## 🎯 Purpose and Intended Users

**Goal**: To push the frontier of AI-assisted code generation by combining state-of-the-art LLMs with structured reasoning and feedback loops for automating Triton kernel development.

**Target Audience**:
- Researchers
- Practitioners
- Developers

**Tasks**:
- Code Generation
- Performance Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Triton kernels adapted from TritonBench-G and new kernels from open-source AMD ROCm repositories.

**Size**: 214 kernels

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Unit testing

**Metrics**:
- Call Accuracy
- Execution Accuracy
- Speedup

**Calculation**: Call Accuracy is calculated as the fraction of AI-generated kernels that can compile and run without errors. Execution Accuracy is the percentage of AI-generated kernels that satisfy all unit tests. Speedup is the ratio of median reference kernel latency to generated kernel latency.

**Interpretation**: Higher accuracy and speedup values indicate better performance of the generated kernels.

**Validation**: The benchmarks were validated by testing multiple kernels and comparing the results against baseline standards.

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
