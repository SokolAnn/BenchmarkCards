# CETBench (Code Equivalence with Transformations Benchmark)

## 📊 Benchmark Details

**Name**: CETBench (Code Equivalence with Transformations Benchmark)

**Overview**: CETBench is a comprehensive benchmark for evaluating LLMs on the task of code-equivalence checking via controlled program transformations.

**Data Type**: program pairs

**Domains**:
- Computer Science

**Languages**:
- Python

**Similar Benchmarks**:
- HumanEval
- MBPP
- BigCloneBench
- GPT-CloneBench
- EqBench
- SeqCoBench
- EquiBench

**Resources**:
- [GitHub Repository](https://github.com/google-deepmind/code_contests)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the robustness of LLMs for the task of code equivalence checking.

**Target Audience**:
- ML Researchers
- Software Developers
- Model Developers

**Tasks**:
- Code Equivalence Checking

**Limitations**: While our analysis presents deep insights into the performance of LLMs on the task of code equivalence under various perturbations, several limitations remain. First, our evaluation is primarily restricted to a single programming language (Python), highlighting the need to explore other languages to assess the generality of observed trends.

## 💾 Data

**Source**: CodeContests dataset

**Size**: 10,000 competitive programming problems

**Format**: N/A

**Annotation**: Automatically generated via program transformations

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics calculated as overall accuracy and F1 scores across model predictions.

**Interpretation**: A higher accuracy indicates better performance in identifying code equivalence.

**Baseline Results**: N/A

**Validation**: Validated by extensive testing on perturbed and original program pairs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack, Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0 (Creative Commons Attribution 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
