# NordDRG-AI-Benchmark

## 📊 Benchmark Details

**Name**: NordDRG-AI-Benchmark

**Overview**: We release NordDRG-AI-Benchmark , the first public, rule-complete test-bed for DRG reasoning. It bundles (i) machine-readable ∼20-sheet NordDRG definition tables and (ii) expert manuals and change-log templates that capture governance workflows, and exposes two suites: a 13-task Logic benchmark and a 13-task Grouper benchmark.

**Data Type**: multimodal

**Domains**:
- Healthcare

**Languages**:
- Finnish
- English

**Similar Benchmarks**:
- MMLU
- GLUE

**Resources**:
- [GitHub Repository](https://github.com/longshoreforrest/norddrg-ai-benchmark)

## 🎯 Purpose and Intended Users

**Goal**: Provide a durable, governance-grade yardstick for future work on trustworthy automation in hospital funding.

**Target Audience**:
- Healthcare Researchers
- Machine Learning Practitioners
- Clinical Coders

**Tasks**:
- Logic Reasoning
- DRG Grouper Emulation

**Limitations**: N/A

## 💾 Data

**Source**: Definition tables and expert manuals provided by the Nordic Casemix Centre.

**Size**: ∼20 interlinked sheets

**Format**: Excel, JSON

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Exact Match

**Calculation**: Accuracy is measured through strict exact-match scoring on both DRG and drg_logic.id.

**Interpretation**: A model's ability to reproduce the same grouping decision as the specification is essential for evaluation.

**Baseline Results**: GPT-5 Thinking solves 7/13 tasks in the Grouper benchmark.

**Validation**: The benchmark was validated through empirical tests with different LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
