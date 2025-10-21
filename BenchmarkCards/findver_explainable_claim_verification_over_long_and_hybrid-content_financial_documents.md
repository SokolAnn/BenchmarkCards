# FINDVER (Explainable Claim Verification over Long and Hybrid-Content Financial Documents)

## 📊 Benchmark Details

**Name**: FINDVER (Explainable Claim Verification over Long and Hybrid-Content Financial Documents)

**Overview**: FINDVER is a comprehensive benchmark specifically designed to evaluate the explainable claim verification capabilities of LLMs in the context of understanding and analyzing long, hybrid-content financial documents. It contains 2,400 expert-annotated examples, divided into three subsets: information extraction, numerical reasoning, and knowledge-intensive reasoning.

**Data Type**: question-answering pairs

**Domains**:
- Finance

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/yilunzhao/FinDVer)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating the capabilities of LLMs in claim verification over complex, expert-domain documents.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Entailment Classification
- Reasoning-process Explanation Generation

**Limitations**: N/A

## 💾 Data

**Source**: Quarterly (Form 10-Q) and annual reports (Form 10-K) from the U.S. Securities and Exchange Commission.

**Size**: 2,400 examples

**Format**: JSON

**Annotation**: Expert annotation by financial professionals.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the comparison of LLM performance against human expert performance.

**Interpretation**: Higher accuracy indicates better performance in verifying claims based on financial documents.

**Validation**: Data quality validation involves proofreading by models and validation by separate expert annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
