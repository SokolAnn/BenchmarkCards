# buggy-HumanEval and buggy-FixEval

## 📊 Benchmark Details

**Name**: buggy-HumanEval and buggy-FixEval

**Overview**: This work defines the buggy-code completion (bCC) task—completing code when the context may contain potential bugs—and introduces two datasets for evaluating it: buggy-HumanEval (synthetic semantic operator-change bugs) and buggy-FixEval (realistic bugs derived from user submissions).

**Data Type**: text (problem statements as docstrings, partial code prefixes with potential bugs, and test cases)

**Domains**:
- Software Engineering

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- FixEval
- CodeNet
- MBPP
- APPs
- CodeXGLUE

**Resources**:
- [GitHub Repository](https://github.com/amazon-science/buggy-code-completion)
- [Resource](https://arxiv.org/abs/2306.03438v2)

## 🎯 Purpose and Intended Users

**Goal**: To define the buggy-code completion (bCC) task, introduce two benchmark datasets (buggy-HumanEval, buggy-FixEval), and evaluate existing Code-LLMs and simple baseline mitigation methods on bCC.

**Target Audience**:
- ML Researchers
- Software Engineering Researchers
- Model Developers

**Tasks**:
- Code Completion
- Program Repair
- Program Synthesis (Text-to-Code Generation)

**Limitations**: Baseline mitigation methods may degrade completion performance on reference (non-buggy) code contexts; unclear how closely buggy-FixEval aligns to general software-development settings; natural distributions of real bugs are imbalanced compared to the constructed/selected distributions used.

## 💾 Data

**Source**: buggy-HumanEval: constructed from a subset of HumanEval by introducing semantic-altering operator changes to reference solutions; buggy-FixEval: constructed from FixEval and CodeNet by pairing rejected and accepted user submissions and selecting prefixes with semantic differences, followed by manual inspection.

**Size**: buggy-HumanEval: 1,896 examples; buggy-FixEval: 292 examples

**Format**: N/A

**Annotation**: buggy-HumanEval: synthetic operator-flip edits applied to canonical solutions and filtered by test execution to ensure failing behavior; buggy-FixEval: matched rejected/accepted submission pairs with character-level edit-distance filtering and manual inspection to ensure semantic, non-syntax-error failures.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Execution-based evaluation (test-case execution/pass@k)
- Baseline augmentation methods: removal-then-completion, completion-then-rewriting (with RealiT), rewriting-then-completion (with INCODER-6B infilling)

**Metrics**:
- pass@k (pass@1, pass@10, pass@100)

**Calculation**: pass@k defined as in the paper with n = 100 completions sampled from a model and k ∈ {1,10,100}; for each bCC instance compute pass@k, average pass@k within each problem, then macro-average across problems. The paper uses n=100 and k=1,10,100.

**Interpretation**: pass@k estimates the probability that any of k samples from the model passes all test cases; higher pass@k indicates better functional correctness. Passing tests is used as a practical proxy for correctness but does not guarantee full correctness.

**Baseline Results**: Example results: On buggy-HumanEval, CODEGEN-2B-MONO pass@1 drops from 54.9% (reference partial code) to 3.1% (buggy partial code). On buggy-FixEval, CODEGEN-2B-MONO pass@1 drops from 37.8% to 4.3%. Mitigation methods improve scores (e.g., rewriting-then-completion yields 24.9% pass@1 for CODEGEN-2B-MONO on buggy-HumanEval) but substantial gaps remain to reference-prefix completion.

**Validation**: Programs are executed against provided test suites to validate functional correctness and to ensure that altered/buggy prefixes fail at least one test; manual inspection was used during buggy-FixEval construction to exclude undesirable cases; ensured semantic bugs (no syntax errors) when constructing instances.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy
- Governance

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Accuracy**: Unrepresentative data
- **Governance**: Unrepresentative risk testing

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
