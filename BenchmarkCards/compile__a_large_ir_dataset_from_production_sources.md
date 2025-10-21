# ComPile: A Large IR Dataset from Production Sources

## 📊 Benchmark Details

**Name**: ComPile: A Large IR Dataset from Production Sources

**Overview**: ComPile is a novel dataset of LLVM-IR collected from production-grade programs across several programming languages, including Rust, Julia, Swift, and C/C++. It aims to advance the training of large language models for compilers and includes high-quality code focused on machine learning applications in compiler tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Rust
- Julia
- Swift
- C
- C++

**Similar Benchmarks**:
- Anghabench
- Exebench
- HPCORPUS

**Resources**:
- [Resource](https://huggingface.co/datasets/llvm-ml/ComPile)
- [GitHub Repository](https://github.com/llvm-ml/llvm-ir-dataset-utils)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large, high-quality LLVM-IR dataset aimed at improving machine learning applications in compilers and enabling better compiler heuristics and intelligent optimizations.

**Target Audience**:
- ML Researchers
- Compiler Engineers

**Tasks**:
- Machine Learning for Compiler Optimization

**Limitations**: N/A

## 💾 Data

**Source**: Production-grade programs from various package ecosystems including Rust, Julia, Swift, and C/C++.

**Size**: 2.8TB

**Format**: LLVM Intermediate Representation

**Annotation**: Extracted through automated compilation and IR generation processes utilizing LLVM.

## 🔬 Methodology

**Methods**:
- Automated data generation
- Statistical analysis

**Metrics**:
- Token Count
- Size Distribution

**Calculation**: Token counts were computed using the Llama 2 tokenizer; size computed from total bitcode.

**Interpretation**: The dataset's utility for training models can be inferred from its size and token distribution.

**Baseline Results**: N/A

**Validation**: Statistical analysis of LLVM-IR modules demonstrated the dataset's quality and utility.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is filtered for permissively licensed projects, no personally identifiable information included.

**Data Licensing**: License information is provided for all included software.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
