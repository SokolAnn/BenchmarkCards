# Automated Theorem Generation (ATG)

## 📊 Benchmark Details

**Name**: Automated Theorem Generation (ATG)

**Overview**: This paper introduces the Automated Theorem Generation (ATG) task, which evaluates generative language models' capability of generating high-quality theorems and reducing complex theorems. The proposed ATG benchmark aims to facilitate the development of language models' theorem generation and improve automated theorem proving.

**Data Type**: theorem statements

**Domains**:
- Mathematics
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/metamath/set.mm/blob/develop/set.mm)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the ability of generative language models to generate new and reusable theorems for automated theorem proving.

**Target Audience**:
- ML Researchers
- Theorem Provers
- Mathematicians

**Tasks**:
- Automated Theorem Generation

**Limitations**: N/A

## 💾 Data

**Source**: Metamath formal language and its 'set.mm' library.

**Size**: 38,000 theorems

**Format**: N/A

**Annotation**: Manually annotated from human-written theorems.

## 🔬 Methodology

**Methods**:
- Monte Carlo Tree Search (MCTS)
- Self-play learning

**Metrics**:
- Average Proof Reduction (APR)
- Precision

**Calculation**: APR is calculated based on the reduction in proof length from using the expanded theorem library, while precision is calculated by comparing generated theorems to human-written theorems.

**Interpretation**: Higher APR indicates better generation quality and shorter proofs, and higher precision indicates better alignment with human-written theorems.

**Baseline Results**: N/A

**Validation**: Validated through extensive experiments comparing generated theorems with existing human-written proofs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
