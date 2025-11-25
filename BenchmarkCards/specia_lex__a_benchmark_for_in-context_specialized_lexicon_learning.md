# SPECIA LEX: A Benchmark for In-Context Specialized Lexicon Learning

## 📊 Benchmark Details

**Name**: SPECIA LEX: A Benchmark for In-Context Specialized Lexicon Learning

**Overview**: SPECIA LEX is a benchmark for evaluating a language model’s ability to follow specialized lexicon-based constraints across 18 diverse subtasks. It encompasses tasks such as CHECKING, IDENTIFICATION, REWRITING, and OPEN GENERATION with a total of 1,785 test instances.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Similar Benchmarks**:
- LEGAL BENCH
- RAFT

**Resources**:
- [GitHub Repository](https://github.com/imperialite/specialex/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of how large language models capture lexicon-based constraints for content generation tasks across interdisciplinary fields.

**Target Audience**:
- ML Researchers
- Domain Experts
- Education Professionals

**Tasks**:
- Checking
- Identification
- Rewriting
- Open Generation

**Limitations**: Application limited to English language and focused on lexicon-based constraints only.

## 💾 Data

**Source**: Utilizes the Simple Technical English lexicon and the Oxford 5000 words list for the construction of test instances.

**Size**: 1,785 test instances

**Format**: N/A

**Annotation**: Automated and manual evaluations by domain experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact match accuracy

**Calculation**: Metrics are calculated based on adherence to specific roles, definitions, and audience appropriateness.

**Interpretation**: Higher accuracy indicates better compliance to specialized lexicon constraints.

**Baseline Results**: Evaluated against 15 state-of-the-art LLMs.

**Validation**: Continuous validation with domain experts and comparison to existing benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
