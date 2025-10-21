# HumanEvalComm

## 📊 Benchmark Details

**Name**: HumanEvalComm

**Overview**: HumanEvalComm is created to evaluate the degree of communication skills of LLMs in code generation tasks by modifying problem descriptions to include inconsistencies, ambiguities, and incompletenesses. It assesses the ability of LLMs to ask clarifying questions when descriptions are modified according to specified requirement engineering concepts.

**Data Type**: text

**Domains**:
- Software Engineering

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval

**Resources**:
- [GitHub Repository](https://github.com/jie-jw-wu/human-eval-comm)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to evaluate the communication competence of large language models and LLM agents in code generation tasks.

**Target Audience**:
- ML Researchers
- Software Developers
- AI Practitioners

**Tasks**:
- Code Generation
- Clarification Questioning

**Limitations**: N/A

## 💾 Data

**Source**: The benchmark constructs modified problem descriptions based on the HumanEval benchmark, applying different classification types from Requirement Engineering to trigger clarifying questions in LLMs.

**Size**: 164 problems

**Format**: JSON

**Annotation**: Manually modified by experienced software engineers to introduce ambiguities, inconsistencies, and incompleteness.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Communication Rate
- Good Question Rate
- Pass@1
- Test Pass Rate

**Calculation**: Communication Rate is calculated as the percentage of responses containing questions instead of code. Good Question Rate measures the percentage of questions labeled as good by a LLM-based evaluator.

**Interpretation**: Higher Communication Rate and Good Question Rate indicate better communication competence of the models.

**Baseline Results**: N/A

**Validation**: Statistical significance tests (e.g., t-tests) are performed on the results to validate findings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Output bias
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential miscommunication due to LLMs not asking for clarification when needed.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
