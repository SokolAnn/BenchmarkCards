# XtraQA

## 📊 Benchmark Details

**Name**: XtraQA

**Overview**: XtraQA is a comprehensive dataset consisting of 7,040 research papers from top-tier venues, annotated with over 140,000 instruction-response pairs that facilitate context-aware and controllable revisions in academic writing.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [Resource](https://arxiv.org/abs/2505.11336)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset that enhances the capabilities of LLMs in academic paper revision through human-AI collaboration.

**Target Audience**:
- ML Researchers
- Academics
- Model Developers

**Tasks**:
- Text Revision

**Limitations**: N/A

## 💾 Data

**Source**: 7,040 research papers collected from ICLR 2024 and annotated for instruction-response pairs.

**Size**: 7,040 papers

**Format**: JSON

**Annotation**: Annotated with over 140,000 instruction-response pairs reflective of realistic scientific revisions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Length-Controlled Win Rate

**Calculation**: Maximizing the conditional log-likelihood of generated revisions given original paragraphs and instructions.

**Interpretation**: Positive win rates indicate improved quality of paper revisions.

**Baseline Results**: XtraGPT outperformed baseline models including GPT-4o-mini.

**Validation**: Validation through quantitative and qualitative evaluations with human judges.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential for over-reliance and introduction of bias from training data.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
