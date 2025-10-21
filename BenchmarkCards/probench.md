# ProBench

## 📊 Benchmark Details

**Name**: ProBench

**Overview**: ProBench is designed to benchmark large language models in competitive programming, collecting comprehensive competitive programming problems and establishing a unified problem attribute system for thorough assessment of model capabilities.

**Data Type**: programming problems

**Domains**:
- Computer Science

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- HumanEval
- APPS

**Resources**:
- [GitHub Repository](https://github.com/YL-9/probench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for assessing the reasoning capabilities of large language models in competitive programming.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Code Generation
- Competitive Programming Assessment

**Limitations**: ProBench primarily relies on three major programming contest platforms and may lag behind offline evaluation systems in convenience.

## 💾 Data

**Source**: Competitive programming platforms (Codeforces, Luogu, Nowcoder)

**Size**: 790 problems

**Format**: N/A

**Annotation**: Problems were aggregated from competitive programming platforms with comprehensive metadata such as difficulty levels and algorithm tags.

## 🔬 Methodology

**Methods**:
- Online submission evaluation
- Systematic data analysis

**Metrics**:
- pass@1

**Calculation**: Metrics are calculated based on the code's success rate on the original competitive programming platforms.

**Interpretation**: Higher pass@k scores indicate better performance in reasoning and problem-solving capabilities.

**Baseline Results**: QwQ-32B-Preview achieved a pass@1 score of 20.93.

**Validation**: Evaluations were compared against established benchmarks and involved using real competitive programming test cases.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
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
