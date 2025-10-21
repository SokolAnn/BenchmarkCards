# Multilingual Collaborative Defense (MCD)

## 📊 Benchmark Details

**Name**: Multilingual Collaborative Defense (MCD)

**Overview**: MCD is a novel learning method that optimizes a continuous soft safety prompt to facilitate multilingual safeguarding of Large Language Models (LLMs) against harmful queries, enhancing robustness across diverse languages.

**Data Type**: multilingual jailbreak datasets

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Danish
- Korean
- Greek
- Irish

**Similar Benchmarks**:
- MaliciousInstruct
- AdvBench
- MultiJail

**Resources**:
- [GitHub Repository](https://github.com/HLiang-Lee/MCD)

## 🎯 Purpose and Intended Users

**Goal**: To improve the robustness and security of Large Language Models (LLMs) against multilingual jailbreak queries.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Robustness against harmful queries

**Limitations**: N/A

## 💾 Data

**Source**: Translated datasets based on previous research including MaliciousInstruct and AdvBench, extending to multilingual versions.

**Size**: 3,150 samples (including 315 in English and parallel samples in multiple languages)

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Attack Success Rate (ASR)

**Calculation**: Comparative analysis against baseline methods using statistical tests.

**Interpretation**: Lower ASR indicates better defense performance against harmful queries.

**Baseline Results**: Demonstrated significant improvement over existing defenses in multilingual settings.

**Validation**: Statistical significance tests (p-values) were performed to confirm the robustness of results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness

**Atlas Risks**:
- **Robustness**: Prompt injection attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
