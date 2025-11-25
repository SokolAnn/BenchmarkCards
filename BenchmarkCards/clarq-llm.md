# ClarQ-LLM

## 📊 Benchmark Details

**Name**: ClarQ-LLM

**Overview**: ClarQ-LLM is an evaluation framework designed to assess agents’ ability to ask clarification questions in task-oriented dialogues. It includes 31 task types, each with 10 unique dialogue scenarios between information seeker and provider agents.

**Data Type**: bilingual conversation tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- ShARC
- ClariT

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate how well LLMs can handle task-oriented dialogues with clarification questions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Task-Oriented Dialogue

**Limitations**: N/A

## 💾 Data

**Source**: 31 task types with 10 unique dialogue scenarios each.

**Size**: 310 dialogue scenarios

**Format**: N/A

**Annotation**: Tasks were reviewed and annotated for logical correctness.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Success Rate
- Average Query Discrepancy (AQD)
- Average Query Length (AQL)

**Calculation**: Metrics are calculated based on the number of successful information-gathering tasks, discrepancies in queries asked, and the length of those queries.

**Interpretation**: A successful dialog task is determined by whether the seeker agent successfully gathers all required information.

**Baseline Results**: Experimental results show that even state-of-the-art models like GPT-4o achieve around 60.5% success rate.

**Validation**: Model performance was validated through comparisons with human seekers and the provider agents.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
