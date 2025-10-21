# FormalBench

## 📊 Benchmark Details

**Name**: FormalBench

**Overview**: FormalBench is a comprehensive benchmark designed to evaluate the reasoning abilities of Large Language Models (LLMs) on program semantics through formal specification inference.

**Data Type**: program specifications

**Domains**:
- Computer Science

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/thanhlecongg/FormalBench/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the reasoning capabilities of LLMs in synthesizing formal program specifications.

**Target Audience**:
- Researchers
- Software Engineers
- Model Developers

**Tasks**:
- Formal Specification Inference

**Limitations**: N/A

## 💾 Data

**Source**: A dataset of 700 manually validated Java programs and 6,219 augmented programs.

**Size**: 700 Java programs and 6,219 augmented programs

**Format**: N/A

**Annotation**: Manually validated and augmented with semantic-preserving transformations.

## 🔬 Methodology

**Methods**:
- Deductive Verification
- Mutation Testing

**Metrics**:
- Success Rate
- Failure Rate
- Completeness Rate

**Calculation**: Success Rate is calculated as the proportion of specifications that pass verification; Failure Rate is the proportion that fail; Completeness Rate is the fraction of mutants that violate the specification.

**Interpretation**: Higher rates of success and completeness indicate better reasoning capabilities of LLMs.

**Baseline Results**: N/A

**Validation**: The benchmark was validated through empirical studies evaluating state-of-the-art LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Apache 2.0 License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
