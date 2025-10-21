# MATP-BENCH (Multimodal Automated Theorem Proving benchmark)

## 📊 Benchmark Details

**Name**: MATP-BENCH (Multimodal Automated Theorem Proving benchmark)

**Overview**: MATP-BENCH is a new Multimodal, Multi-level, and Multi-language benchmark designed to evaluate MLLMs as automated theorem provers, consisting of 1056 multimodal theorems sourced from high school, university, and competition-level mathematics.

**Data Type**: multimodal theorems

**Domains**:
- Natural Language Processing
- Mathematics

**Languages**:
- English

**Similar Benchmarks**:
- miniF2F
- ProofNet
- LeanEuclid
- PutnamBench

**Resources**:
- [Resource](https://matpbench.github.io)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of MATP-BENCH is to evaluate the capabilities of Multimodal Large Language Models (MLLMs) in the domain of automated theorem proving by presenting multimodal problems that require integration of visual understanding and mathematical reasoning.

**Target Audience**:
- ML Researchers
- Automated Proof Developers

**Tasks**:
- Automated Theorem Proving
- Theorem Formalization

**Limitations**: N/A

## 💾 Data

**Source**: Theorems drawn from high school, university, and competition-level mathematics, with formalizations in Lean 4, Coq, and Isabelle.

**Size**: 1,056 multimodal theorems

**Format**: JSON

**Annotation**: Manually annotated formal statements in three formal languages.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- pass@n (n=1, n=5, n=10)

**Calculation**: Metrics are calculated based on the model's ability to generate valid proofs and formalized theorems from multimodal inputs.

**Interpretation**: Higher scores indicate better performance in generating valid proofs and theorem formalizations.

**Baseline Results**: The performance of state-of-the-art models varies significantly, with the highest scoring models achieving a pass rate of 5.68% for end-to-end theorem proving in Lean 4.

**Validation**: Models are validated against formal theorem verification requirements to ensure correctness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
