# LiveRepoReflection

## 📊 Benchmark Details

**Name**: LiveRepoReflection

**Overview**: LiveRepoReflection is a challenging benchmark for evaluating code understanding and generation in repository-style multi-file contexts, featuring 1,888 rigorously filtered test cases across 6 programming languages.

**Data Type**: code problems

**Domains**:
- Computer Programming

**Languages**:
- Python
- Java
- Go
- Rust
- C++
- JavaScript

**Similar Benchmarks**:
- Aider-polyglot
- HumanEval
- LiveCodeBench
- BigCodeBench

**Resources**:
- [Resource](https://LiveRepoReflection.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of large language models in repository-based code understanding and generation tasks.

**Target Audience**:
- ML Researchers
- Software Developers
- Benchmark Developers

**Tasks**:
- Code Generation
- Code Debugging

**Limitations**: Evaluation in repository-level multilingual scenarios are not fully explored.

## 💾 Data

**Source**: Diverse programming source code from repositories such as GitHub, Hugging Face, and Exercism.

**Size**: 1,888 test cases

**Format**: Custom multi-file repository structure

**Annotation**: Manual annotation by graduate students with assistance from large language models.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Pass@1
- Pass@2
- Fix Weight (FW)
- Well Formed (WF)

**Calculation**: Metrics are calculated based on the proportion of tasks completed correctly and adherence to specified formatting.

**Interpretation**: Higher scores indicate better performance and adherence to task requirements.

**Baseline Results**: Various language models including GPT-4, Claude, and Qwen were evaluated on the benchmark.

**Validation**: Evaluation conducted on over 40 LLMs with a dynamic leaderboard to track performances.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data anonymization strategies were not explicitly discussed.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The research adheres to ethical guidelines for AI development.
