# CombiBench

## 📊 Benchmark Details

**Name**: CombiBench

**Overview**: CombiBench is a comprehensive benchmark comprising 100 combinatorial problems, each formalized in Lean 4 and paired with its corresponding informal statement. The problem set covers a wide spectrum of difficulty levels, ranging from middle school to IMO and university level, and spans over ten combinatorial topics.

**Data Type**: formal statements paired with informal descriptions

**Domains**:
- Natural Language Processing
- Mathematics

**Languages**:
- English

**Similar Benchmarks**:
- miniF2F
- FIMO
- PutnamBench
- ProofNet

**Resources**:
- [GitHub Repository](https://github.com/MoonshotAI/CombiBench/)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of CombiBench is to provide testing standards for evaluating the capabilities of large language models in combinatorial mathematics.

**Target Audience**:
- ML Researchers
- Mathematicians
- Model Developers

**Tasks**:
- Automated Theorem Proving
- Mathematical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: CombiBench includes problems sourced from various competitions and textbooks, including all IMO combinatorial problems since 2000.

**Size**: 100 problems

**Format**: Lean 4 formal statements

**Annotation**: Manually annotated by experts

## 🔬 Methodology

**Methods**:
- Fine-Eval (Fill-in-the-blank in Lean Evaluation)

**Metrics**:
- Pass Rate
- Comparison with ground truth solutions

**Calculation**: Metrics are calculated based on the success of LLMs in generating solutions and proofs that align with ground truth measures set by the benchmark.

**Interpretation**: Models are considered successful if they generate correct, compilable proofs and solutions.

**Baseline Results**: Kimina-Prover Preview solved 7 problems out of 100 during evaluation.

**Validation**: Benchmarks were validated through comparative evaluation across multiple state-of-the-art LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
