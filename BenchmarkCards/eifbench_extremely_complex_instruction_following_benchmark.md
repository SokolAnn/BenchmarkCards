# EIFBENCH (Extremely Complex Instruction Following Benchmark)

## 📊 Benchmark Details

**Name**: EIFBENCH (Extremely Complex Instruction Following Benchmark)

**Overview**: EIFBENCH is designed to facilitate a more realistic and robust evaluation of large language models by including multi-task scenarios and a variety of constraints, replicating complex operational environments.

**Data Type**: instruction-following pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/Hope-Rita/EIFBench)
- [GitHub Repository](https://github.com/Tongyi-CCAI/Complex-IF)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the instruction following abilities of large language models in complex, multi-instruction, and multi-constraint scenarios.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Instruction Following
- Multi-task Processing

**Limitations**: The dataset currently focuses primarily on Chinese instructions, limiting its applicability to multilingual scenarios.

## 💾 Data

**Source**: Multi-scenario data collection involving plain text, dyadic dialogue, and multi-party dialogue.

**Size**: 1,000 instances

**Format**: N/A

**Annotation**: Tasks and constraints are generated and refined using large language models.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Instruction-Level Accuracy (ILA)
- Constraint-Level Accuracy (CLA)

**Calculation**: ILA is calculated by averaging compliance across all instructions within a single instance. CLA assesses the fulfillment of individual constraints.

**Interpretation**: Higher scores indicate better performance in following complex multi-instruction tasks.

**Validation**: Quality assessment through a post-inspection protocol with both automated and human evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
