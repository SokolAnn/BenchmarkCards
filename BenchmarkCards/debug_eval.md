# DEBUG EVAL

## 📊 Benchmark Details

**Name**: DEBUG EVAL

**Overview**: DEBUG EVAL is a comprehensive benchmark for evaluating the debugging abilities of Large Language Models (LLMs) by emulating the multi-stage human debugging process. It introduces four tasks: BUG Localization, BUG Identification, Code Repair, and Code Recognition.

**Data Type**: buggy code and corrected code pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Python
- C++
- Java

**Similar Benchmarks**:
- DebugBench
- CodeError
- CodeEditorBench

**Resources**:
- [GitHub Repository](https://github.com/NEUIR/COAST)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of LLMs' code debugging capabilities through a series of tasks that reflect real-world debugging processes.

**Target Audience**:
- ML Researchers
- Software Developers
- Educational Institutions

**Tasks**:
- BUG Localization
- BUG Identification
- Code Repair
- Code Recognition

**Limitations**: While DEBUG EVAL includes four evaluation tasks, incorporating additional tasks could enhance its ability to better evaluate the debugging capabilities of LLMs.

## 💾 Data

**Source**: Data is collected from existing benchmarks including DebugBench and LiveCodeBench, as well as human trials from platforms like AtCoder.

**Size**: 5,712 examples across multiple tasks

**Format**: JSON

**Annotation**: The data entries are manually reviewed for high quality and relevance.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: For BUG Localization, BUG Identification, and Code Recognition, models select answers from multiple choices. For Code Repair, performance is evaluated using Pass@1.

**Interpretation**: The performance is interpreted based on the accuracy of the models' responses to the given tasks, with specific performance metrics used for each task.

**Baseline Results**: Models like GPT-4o-mini, DeepSeek-Coder-V2, and others serve as baseline comparisons.

**Validation**: Each model's effectiveness is validated against predefined test sets of buggy and corrected code.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**
- **Accuracy**: Poor model accuracy
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
