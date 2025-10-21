# CFDLLMBench

## 📊 Benchmark Details

**Name**: CFDLLMBench

**Overview**: CFDLLMBench is a benchmark suite designed to holistically evaluate large language model performance in Computational Fluid Dynamics (CFD), comprising three tasks: graduate-level CFD knowledge, numerical reasoning, and context-dependent implementation of CFD workflows using OpenFOAM.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Engineering

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/NREL-Theseus/cfdllmbench/)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of CFDLLMBench is to provide a comprehensive evaluation framework for assessing the abilities of LLMs in automating numerical simulations in CFD.

**Target Audience**:
- ML Researchers
- Engineering Practitioners
- Domain Experts

**Tasks**:
- Graduate-level Question Answering
- Code Generation
- Configuration of Simulation Workflows

**Limitations**: N/A

## 💾 Data

**Source**: Curated datasets created from CFD lecture notes, GitHub repositories, and expert-authored content.

**Size**: 126 cases (90 CFDQuery questions, 24 CFDCodeBench tasks, 16 advanced FoamBench tasks)

**Format**: JSON, Plain Text

**Annotation**: Dataset curated by experts in the field of Computational Fluid Dynamics.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Expert-informed metrics
- Automated metrics

**Metrics**:
- Success Rate
- Code Executability
- Numerical Error
- Numerical Convergence

**Calculation**: Metrics used to evaluate LLM performance include Success Rate, which is the aggregate of code executability, numerical error, and convergence.

**Interpretation**: A higher Success Rate indicates better execution of simulation workflows and physical accuracy of the results.

**Baseline Results**: N/A

**Validation**: Validated against expert-determined reference solutions and iterative review by domain experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Released under the BSD 3-Clause License, free for use and modification.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
