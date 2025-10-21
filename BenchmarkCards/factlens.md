# FactLens

## 📊 Benchmark Details

**Name**: FactLens

**Overview**: FactLens is a benchmark designed specifically for fine-grained fact verification, allowing for the precise identification of inaccuracies by breaking complex claims into smaller sub-claims for individual verification.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/megagonlabs/factlens)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of FactLens is to facilitate fine-grained verification of factual claims by evaluating the quality of sub-claims generated from complex claims.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Fact Verification

**Limitations**: N/A

## 💾 Data

**Source**: The dataset consists of 733 instances from CoverBench which are fact-checked claims sampled from diverse sources.

**Size**: 733 examples

**Format**: N/A

**Annotation**: The data was manually curated to ensure high-quality ground truth sub-claims.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Atomicity
- Sufficiency
- Fabrication
- Coverage
- Redundancy
- Readability

**Calculation**: Metrics are computed based on evaluations from both LLM-generated scores and statistical methods.

**Interpretation**: High atomicity, sufficiency, coverage, and readability are desirable, while low fabrication and redundancy are preferred.

**Baseline Results**: N/A

**Validation**: The alignment of automated evaluator scores with human judgments was validated.

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
