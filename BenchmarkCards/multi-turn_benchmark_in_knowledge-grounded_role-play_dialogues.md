# Multi-Turn Benchmark in Knowledge-Grounded Role-Play Dialogues

## 📊 Benchmark Details

**Name**: Multi-Turn Benchmark in Knowledge-Grounded Role-Play Dialogues

**Overview**: This benchmark exposes LLM degradation in knowledge-grounded role-play dialogues and provides a validated hybrid evaluation framework to guide the reliable integration of LLMs in training simulations.

**Data Type**: dialogue exchanges

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Similar Benchmarks**:
- MT-Bench

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To compare LLM-generated and human-authored responses in multi-turn professional training simulations and validate a hybrid evaluation framework.

**Target Audience**:
- ML Researchers
- Education Practitioners
- Model Developers

**Tasks**:
- Dialogue Quality Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Human-authored conversation scenarios adapted for empirical study.

**Size**: N/A

**Format**: text

**Annotation**: Human evaluation through participant judgments and automated LLM assessment.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated LLM-as-a-judge assessment

**Metrics**:
- Naturalness
- Context Maintenance
- Overall Quality
- Interestingness
- Knowledge Utilization
- Understandability

**Calculation**: LLM-generated responses rated on a scale, compared to human-authored benchmarks.

**Interpretation**: Higher scores indicate better quality, reflecting more natural and contextually appropriate responses.

**Baseline Results**: LLM-generated responses showed a quality degradation over multi-turn dialogues compared to progressive improvements in human responses.

**Validation**: Linear mixed-effects models were used to assess quality variations across dialogue turns.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent was obtained from all participants.

**Compliance With Regulations**: This study complies with the research ethics guidelines of Utrecht University.
