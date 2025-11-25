# Saturation-Driven Dataset Generation for LLM

## 📊 Benchmark Details

**Name**: Saturation-Driven Dataset Generation for LLM

**Overview**: The paper introduces a new framework for generating tasks for mathematical reasoning in LLMs, utilizing a saturation-driven approach to ensure logical validity of generated problems.

**Data Type**: question-answering pairs

**Domains**:
- Mathematics

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/sileod/reasoning_core)
- [Resource](https://hf.co/datasets/reasoning-core/rc1)

## 🎯 Purpose and Intended Users

**Goal**: To generate a diverse set of logically valid reasoning tasks to assess and improve the reasoning capabilities of LLMs.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Conjecture Entailment Verification
- Minimal Premise Selection
- Proof Graph Reconstruction

**Limitations**: N/A

## 💾 Data

**Source**: TPTP axiom library used to generate theorems through saturation.

**Size**: 3,000 problems

**Format**: N/A

**Annotation**: Automatically generated through a reasoning framework.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the proportion of correctly identified tasks and logical entailments.

**Interpretation**: Higher scores indicate better reasoning capabilities of LLMs.

**Baseline Results**: Performance of gpt-5 models evaluated across various tasks.

**Validation**: Tasks validated using advanced theorem provers like Vampire.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
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
