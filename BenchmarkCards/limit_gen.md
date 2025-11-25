# LIMIT GEN

## 📊 Benchmark Details

**Name**: LIMIT GEN

**Overview**: LIMIT GEN is a comprehensive benchmark for evaluating LLMs’ capability to support early-stage feedback and complement human peer review by identifying the limitations of scientific research, particularly in AI.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/yale-nlp/LimitGen)
- [Resource](https://huggingface.co/datasets/yale-nlp/LimitGen)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate models on identifying and addressing scientific research limitations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Limitation Identification
- Peer Review Generation

**Limitations**: N/A

## 💾 Data

**Source**: Data is collected from ICLR 2025 submissions and includes synthetic data created through controlled perturbations of high-quality papers.

**Size**: 2,000 examples

**Format**: JSON

**Annotation**: Annotations conducted by human experts and the use of LLMs for synthetic generation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Jaccard Index
- Recall
- Precision

**Calculation**: Metrics are calculated based on comparisons between generated limitations and ground truth.

**Interpretation**: Higher scores indicate better alignment and relevance of the generated limitations to the actual research limitations.

**Baseline Results**: N/A

**Validation**: Inter-annotator agreement is measured using Cohen’s Kappa.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
