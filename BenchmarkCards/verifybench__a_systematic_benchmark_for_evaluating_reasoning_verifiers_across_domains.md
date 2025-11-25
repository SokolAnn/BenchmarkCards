# VerifyBench: A Systematic Benchmark for Evaluating Reasoning Verifiers Across Domains

## 📊 Benchmark Details

**Name**: VerifyBench: A Systematic Benchmark for Evaluating Reasoning Verifiers Across Domains

**Overview**: VerifyBench is a cross-domain comprehensive benchmark for systematically evaluating verifiers constructed from about 4,000 expert-level questions covering mathematics, physics, chemistry, and biology. Each question includes reliable reference answers and diverse responses, ensuring rigorous evaluation.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2507.09884)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic, multidisciplinary evaluation platform for verifiers across STEM domains and to comprehensively analyze behavioral differences between verifier types.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from approximately 4,000 expert-level questions selected through manual review from diverse sources.

**Size**: 3,989 questions

**Format**: N/A

**Annotation**: Annotated by a multidisciplinary expert team through a two-stage process including independent review.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Accuracy
- Recall

**Calculation**: Metrics are calculated through a comparison of verifier responses against reference answers according to defined evaluation criteria.

**Interpretation**: High accuracy indicates correct alignment with reference answers, while recall reflects the ability to identify valid responses regardless of expression.

**Baseline Results**: Specialized verifiers show leading accuracy in structured domains, while general models excel in recall.

**Validation**: Validation through inter-annotator agreement and multi-stage annotation processes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
