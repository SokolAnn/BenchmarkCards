# DafnyBench

## 📊 Benchmark Details

**Name**: DafnyBench

**Overview**: DafnyBench is the largest benchmark for training and evaluating machine learning systems for formal software verification, testing LLMs like GPT-4 and Claude 3 to auto-generate hints for the Dafny verification engine to effectively verify programs.

**Data Type**: programs

**Domains**:
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- Clover
- dafny-synthesis

**Resources**:
- [GitHub Repository](https://github.com/sun-wendy/DafnyBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark dataset for formal verification, expanding the size and complexity of previously existing benchmarks.

**Target Audience**:
- ML Researchers
- Developers of verification tools
- Formal verification practitioners

**Tasks**:
- Formal software verification

**Limitations**: N/A

## 💾 Data

**Source**: Scraped from publicly available Dafny files on GitHub and existing benchmarks like Clover and dafny-synthesis.

**Size**: 782 programs

**Format**: JSON

**Annotation**: Manual verification of program correctness by human programmers.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Success rate

**Calculation**: A program is considered successfully verified if it passes the Dafny verifier without modifications.

**Interpretation**: A higher success rate indicates better performance of LLMs in generating valid hints for formal verification.

**Baseline Results**: Claude 3 Opus achieved a success rate of ∼68% on the benchmark.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data scraped from publicly available repositories on GitHub.

**Data Licensing**: The DafnyBench dataset is released under an Apache 2.0 license and GNU General Public License v3.0.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
