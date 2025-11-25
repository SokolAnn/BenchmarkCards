# Ineq-Comp

## 📊 Benchmark Details

**Name**: Ineq-Comp

**Overview**: Ineq-Comp is a benchmark for evaluating the compositional reasoning abilities of formal theorem provers on inequalities. It is created using 75 seed problems and extends through 150 additional problems involving human-intuitive transformations to assess models' performance on compositional reasoning.

**Data Type**: algebraic inequality problems

**Domains**:
- Mathematics

**Languages**:
- English

**Similar Benchmarks**:
- MiniF2F
- ProofNet
- PutnamBench

**Resources**:
- [GitHub Repository](https://github.com/haoyuzhao123/LeanIneqComp)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and measure the compositional reasoning ability of automated theorem provers in the context of mathematical inequalities.

**Target Audience**:
- Researchers in formal mathematics
- Developers of automated theorem proving systems

**Tasks**:
- Automated Theorem Proving

**Limitations**: N/A

## 💾 Data

**Source**: Curated set of inequality problems, with each seed problem verified in Lean 4 and accompanied by formal proofs.

**Size**: 75 seed problems and 150 additional transformed problems plus 50 real-world problems

**Format**: Lean 4 code

**Annotation**: Verified Lean 4 proofs accompanying each seed problem.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Pass@N accuracy

**Calculation**: Metrics are calculated based on whether at least one of N generated proofs for a given problem is correct.

**Interpretation**: Higher pass@N indicates better compositional reasoning ability of the theorem provers.

**Validation**: Benchmarks are validated through results of existing models and demonstrable performance analyses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
