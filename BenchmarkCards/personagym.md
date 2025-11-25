# PersonaGym

## 📊 Benchmark Details

**Name**: PersonaGym

**Overview**: PersonaGym is the first dynamic evaluation framework for persona agents, allowing for large-scale, multi-dimensional, and targeted evaluation of persona agents. It includes a novel metric called PersonaScore that aligns with human judgment and assesses the agent's adherence to its assigned persona across diverse tasks and environments.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RoleBench
- CharacterEval
- RoleEval

**Resources**:
- [Resource](https://personagym.com)

## 🎯 Purpose and Intended Users

**Goal**: To enable comprehensive and robust evaluation of persona agents through dynamic personalization in relevant environments and tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Action Justification
- Expected Action
- Linguistic Habits
- Persona Consistency
- Toxicity Control

**Limitations**: N/A

## 💾 Data

**Source**: A static benchmark consisting of 200 personas and 10,000 questions generated using LLMs.

**Size**: 10,000 questions

**Format**: N/A

**Annotation**: Responses evaluated using expert-curated rubrics and automatic LLM evaluations.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- PersonaScore

**Calculation**: PersonaScore is calculated based on the alignment of agent responses with expected persona behavior across multiple tasks.

**Interpretation**: Higher PersonaScores indicate better alignment with the assigned persona, reflecting effective role-playing.

**Baseline Results**: N/A

**Validation**: Validation through human evaluation and ensemble methods to ensure robustness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Governance**: Lack of testing diversity
- **Privacy**: Reidentification

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: PersonaGym addresses privacy concerns by mitigating risks associated with persona generation.

**Data Licensing**: MIT License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
