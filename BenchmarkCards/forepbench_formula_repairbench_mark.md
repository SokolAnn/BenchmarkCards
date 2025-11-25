# FoRepBench (Formula RepairBench mark)

## 📊 Benchmark Details

**Name**: FoRepBench (Formula RepairBench mark)

**Overview**: FoRepBench is a benchmark dataset specifically designed for context-aware Excel formula repair, focusing on runtime errors. It includes spreadsheet context, faulty formulas, corrected versions, and user utterances expressing intent.

**Data Type**: Excel formula repair examples

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/microsoft/prose-benchmarks/tree/main/FoRepBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality benchmark for evaluating models that assist in repairing Excel formulas and diagnosing errors.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Excel Formula Repair

**Limitations**: N/A

## 💾 Data

**Source**: Curated seed samples from online forums and generated using a synthetic data generation pipeline.

**Size**: 618 examples

**Format**: N/A

**Annotation**: Manual verification and correction by annotators, supplemented by automated checks.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Manual annotation
- LLM-based validation

**Metrics**:
- Syntax Validity
- Can Execute
- Execution Match

**Calculation**: Metrics are calculated based on the ability of the repaired formula to compile and execute without errors.

**Interpretation**: Higher scores in Execution Match indicate better performance of the model in repairing formulas.

**Baseline Results**: Various LLMs including GPT-4o, GPT-4.1, Phi-3, and Mistral were evaluated with varying performance.

**Validation**: The benchmark was validated through execution checks and LLM-based semantic validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
