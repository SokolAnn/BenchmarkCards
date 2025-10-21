# MONO (Multi-agent Operated Noise Outfilter)

## 📊 Benchmark Details

**Name**: MONO (Multi-agent Operated Noise Outfilter)

**Overview**: MONO is an LLM-powered framework designed to improve vulnerability datasets by addressing common issues like semantic mislabeling and undecidable patches that hinder vulnerability detection effectiveness.

**Data Type**: text

**Domains**:
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- MegaVul
- BigVul
- DiverseVul

**Resources**:
- [GitHub Repository](https://github.com/vul337/mono)

## 🎯 Purpose and Intended Users

**Goal**: To construct reliable vulnerability datasets using a multi-agent framework that improves upon existing dataset quality by filtering out noisy samples and enhancing context representation.

**Target Audience**:
- ML Researchers
- Security Auditors
- Software Developers

**Tasks**:
- Vulnerability Detection

**Limitations**: N/A

## 💾 Data

**Source**: The MegaVul dataset was used as the starting point to extract function-level and patch metadata, supplemented by custom crawlers to gather repository-level context.

**Size**: 6,212 CVEs

**Format**: Custom structured format containing metadata, context, and classification.

**Annotation**: Automated classification aided by LLM analysis and human expert validation.

## 🔬 Methodology

**Methods**:
- Iterative contextual analysis
- Multi-agent classification
- Static analysis tool integration

**Metrics**:
- Precision
- Recall

**Calculation**: Precision is calculated as the ratio of true positives to the sum of true positives and false positives. Recall is calculated as the ratio of true positives to the sum of true positives and false negatives.

**Interpretation**: High precision indicates that when a security patch is identified, it is correct, while high recall signifies the capability to find all relevant security patches.

**Baseline Results**: The model demonstrated a precision of 100% and a recall of 96.2% on test data, filtering non-security patches.

**Validation**: Human evaluation on a sample of identified patches to verify classification accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Noise due to semantic mislabeling and incorrect patch classifications.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Open-sourced under a GitHub repository. License type not specified.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
