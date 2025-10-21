# CKAD (Cost-effective Knowledge Acquisition Dataset)

## 📊 Benchmark Details

**Name**: CKAD (Cost-effective Knowledge Acquisition Dataset)

**Overview**: CKAD is a new benchmark dataset designed for cost-effective LLM domain knowledge acquisition, aiming to enhance the performance of large language models in specialized domains, particularly drug discovery and rare disease research.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/YANGWU001/PU-ADKA)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the CKAD dataset is to facilitate the enhancement of domain-specific large language models through efficient and cost-effective expert engagement.

**Target Audience**:
- ML Researchers
- Domain Experts
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from PubMed articles published after 2023, extracting question-answer pairs using GPT-4 based on unique mechanisms.

**Size**: 48,219 question-answer pairs

**Format**: JSON

**Annotation**: Manually validated by experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Model-based evaluation

**Metrics**:
- Win Rate (WR)
- Length-Controlled Win Rate (LC_WR)

**Calculation**: Metrics are calculated based on the percentage of instances where model-generated answers adequately capture the core meaning of the golden answer and account for answer length discrepancies.

**Interpretation**: Higher WR and LC_WR indicate better performance and knowledge acquisition from the dataset.

**Baseline Results**: Comparison with existing methods shows PU-ADKA outperforming all baselines in both WR and LC_WR.

**Validation**: Performance validated through simulations and a real-world case study with biomedical experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All content derived from publicly available biomedical literature; no personal or sensitive information collected.

**Data Licensing**: Not Applicable

**Consent Procedures**: All expert annotations performed as part of their institutional responsibilities without additional compensation.

**Compliance With Regulations**: Not Applicable
