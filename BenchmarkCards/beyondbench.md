# BEYONDBENCH

## 📊 Benchmark Details

**Name**: BEYONDBENCH

**Overview**: BEYONDBENCH is an evaluation framework that avoids the problem of data contamination by using algorithmic problem generation to create mathematically grounded problems on the fly, ensuring fresh and uncontaminated test instances for evaluating reasoning capabilities in language models.

**Data Type**: algorithmic problems

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://ctrl-gaurav.github.io/BeyondBench/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a contamination-free evaluation framework for reasoning capabilities in language models, ensuring fair and meaningful assessment through dynamic problem generation.

**Target Audience**:
- Researchers
- AI Practitioners

**Tasks**:
- Algorithmic Reasoning
- Logical Deduction

**Limitations**: Due to the dynamic nature of the problems generated, specific benchmarks targeting areas like commonsense reasoning are not covered.

**Out of Scope Uses**:
- Models that exhibit no reasoning capabilities.
- Models that solely memorize patterns without generalization.

## 💾 Data

**Source**: Mathematically generated problems through dynamic algorithms, ensuring a unique and verifiable solution for each instance.

**Size**: 117 problem variations across 44 algorithmic tasks

**Format**: Dynamic generation using algorithmic problem generation

**Annotation**: Automatically verified via mathematical proofs.

## 🔬 Methodology

**Methods**:
- Dynamic problem generation
- Algorithmic evaluation
- Verification of solution uniqueness

**Metrics**:
- Accuracy
- Instruction Following
- Token Efficiency

**Calculation**: Accuracy is measured based on the percentage of problems solved correctly validated against ground truth or complete solution sets. Instruction Following assesses the percentage of responses conforming to required output formats.

**Interpretation**: Higher accuracy denotes better reasoning performance, while lower token efficiency suggests potential overthinking by the models, with lower instruction-following accuracy indicating format mismatches.

**Validation**: The model evaluations are tested using a number of randomly generated problem instances to ensure robustness in results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning
- **Privacy**: Data privacy rights alignment

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The framework generates abstract mathematical problems that do not encode real-world biases, providing a safe evaluation methodology.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
