# Energy-Aware Code Generation Benchmark

## 📊 Benchmark Details

**Name**: Energy-Aware Code Generation Benchmark

**Overview**: This study benchmarks Small Language Models (SLMs) against Large Language Models (LLMs) for energy-efficient code generation, comparing their performance and energy efficiency on 150 programming problems from LeetCode.

**Data Type**: programming problems

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/stabilityai/stable-code-3b)
- [Resource](https://huggingface.co/bigcode/starcoderbase-3b)
- [Resource](https://huggingface.co/Qwen/Qwen2.5-Coder-3B-Instruct)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the efficiency and sustainability of Small Language Models (SLMs) in comparison to Large Language Models (LLMs) for code generation tasks.

**Target Audience**:
- Academic Researchers
- Software Developers
- Environmental Scientists

**Tasks**:
- Code Generation
- Performance Evaluation

**Limitations**: The findings may not apply to all LLMs, especially those using newer architectures or trained on different datasets.

## 💾 Data

**Source**: 150 coding problems randomly selected from LeetCode, categorized by difficulty: easy, medium, and hard.

**Size**: 150 problems

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Statistical evaluation
- Energy consumption measurement
- Runtime and memory usage analysis

**Metrics**:
- Correctness
- Runtime
- Memory usage
- Energy consumption

**Calculation**: Metrics are calculated based on execution of generated code in a controlled environment using Python scripts.

**Interpretation**: Lower execution time and energy consumption indicate better efficiency. Higher correctness signals more effective code generation.

**Baseline Results**: Human-written solutions are used as the baseline for correctness and efficiency.

**Validation**: Each generated solution is tested against community-verified solutions to assess correctness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Energy Efficiency
- Code Performance

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
