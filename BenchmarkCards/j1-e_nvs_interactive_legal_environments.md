# J1-E NVS (Interactive Legal Environments)

## 📊 Benchmark Details

**Name**: J1-E NVS (Interactive Legal Environments)

**Overview**: J1-E NVS introduces the first interactive and dynamic legal environment tailored for LLM-based agents, consisting of six representative scenarios from Chinese legal practices across three levels of environmental complexity.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- LexGLUE
- LegalBench
- LawBench
- LexEval
- Law-Eval
- LAiW

**Resources**:
- [Resource](https://J1Bench.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of LLM-based agents in dynamic legal environments.

**Target Audience**:
- ML Researchers
- Legal Professionals
- AI Developers

**Tasks**:
- Legal Consultation
- Complaint Drafting
- Defence Drafting
- Court Proceedings

**Limitations**: The benchmark focuses primarily on procedural flow of legal tasks without advanced capabilities for real-world applications.

## 💾 Data

**Source**: Based on real-world legal scenarios derived from Chinese legal practices.

**Size**: 508 distinct environments

**Format**: text

**Annotation**: Annotated by legal experts.

## 🔬 Methodology

**Methods**:
- Automated metrics
- LLM-based evaluation
- Expert evaluation

**Metrics**:
- Binary accuracy
- Non-binary score
- Format-following score
- Document score
- Procedural-following score
- Judgment score

**Calculation**: Metrics calculated based on task completion and procedural compliance.

**Interpretation**: Higher scores indicate better task completion and procedural adherence.

**Baseline Results**: SOTA models struggle to exceed 60% performance overall.

**Validation**: Evaluated across multiple runs with consistent results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Output bias
- **Robustness**: Evasion attack

**Demographic Analysis**: Analysis of diverse participant behaviors integrated into role settings.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
