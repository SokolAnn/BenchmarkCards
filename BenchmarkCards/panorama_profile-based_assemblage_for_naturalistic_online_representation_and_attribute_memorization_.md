# PANORAMA (Profile-based Assemblage for Naturalistic Online Representation and Attribute Memorization Analysis)

## 📊 Benchmark Details

**Name**: PANORAMA (Profile-based Assemblage for Naturalistic Online Representation and Attribute Memorization Analysis)

**Overview**: PANORAMA is a large-scale synthetic corpus designed to closely emulate the distribution, variety, and context of PII and sensitive data as it naturally occurs in online environments, comprising 384,789 samples derived from 9,674 synthetic profiles.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LLM-PBE
- PII-Scope

**Resources**:
- [Resource](https://huggingface.co/datasets/PANORAMA)
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for privacy risk assessment, model auditing, and the development of privacy-preserving LLMs.

**Target Audience**:
- ML Researchers
- Privacy Auditors
- Model Developers

**Tasks**:
- Memorization Risk Evaluation

**Limitations**: Limited diversity in content tone; restricted to English language.

## 💾 Data

**Source**: Synthetic profiles generated through a constrained selection approach reflecting real-world demographics.

**Size**: 384,789 samples

**Format**: JSON

**Annotation**: Automatically generated based on synthetic profiles.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- ROUGE-L
- Soft Match Rate

**Calculation**: Measured using soft match criteria with ROUGE-L scores.

**Interpretation**: Higher ROUGE-L and Soft Match rates indicate better memorization performance.

**Validation**: Validated through fine-tuning Mistral-7B and measuring memorization rates.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Includes diverse demographics across 8 different regions.

**Potential Harm**: ['Leakage of sensitive PII']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is synthetically generated to mitigate privacy concerns.

**Data Licensing**: Publicly available under research-friendly terms.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
