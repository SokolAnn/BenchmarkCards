# PrivaCI-Bench

## 📊 Benchmark Details

**Name**: PrivaCI-Bench

**Overview**: PrivaCI-Bench is a comprehensive contextual privacy evaluation benchmark targeted at legal compliance to cover well-annotated privacy and safety regulations, real court cases, privacy policies, and synthetic data built from the official toolkit to study LLMs’ privacy and safety compliance.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Ci-bench

**Resources**:
- [Resource](https://hkust-knowcomp.github.io/privacy/)
- [GitHub Repository](https://github.com/HKUST-KnowComp/PrivaCI-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs' privacy and safety awareness in relation to various legal compliance regulations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Legal Experts

**Tasks**:
- Legal Compliance Evaluation
- Context Understanding Probing

**Limitations**: The benchmark primarily focuses on legal regulations and may not fully capture individual privacy expectations or cultural norms.

## 💾 Data

**Source**: Real court cases, privacy policies, and synthetic data from official toolkits.

**Size**: 154,191 examples

**Format**: JSON

**Annotation**: Annotated by LLMs with humans in the loop.

## 🔬 Methodology

**Methods**:
- Direct Prompt
- Chain-of-Thought Reasoning
- Retrieval Augmented Generation

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on the classification results of responses to legal compliance tasks and context understanding.

**Interpretation**: Higher accuracy indicates better compliance with privacy regulations and greater understanding of context.

**Validation**: Validation includes human evaluation of annotated data and regular checks for compliance assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness

**Atlas Risks**:
- **Privacy**: Personal information in data, Data privacy rights alignment
- **Fairness**: Data bias

**Demographic Analysis**: Includes consideration of legal compliance across diverse segments but not aggregated demographic data.

**Potential Harm**: Potential risks of LLMs failing to accurately interpret legal contexts leading to incorrect compliance judgments.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Real cases collected are anonymized with no identifiable private information.

**Data Licensing**: Data is used under fair use provisions and relevant licenses for research purposes.

**Consent Procedures**: All collected data is sourced from publicly accessible legal documents and cases.

**Compliance With Regulations**: Developed in adherence to GDPR, HIPAA, and relevant local privacy laws.
