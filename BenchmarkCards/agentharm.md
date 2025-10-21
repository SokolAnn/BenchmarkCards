# AgentHarm

## 📊 Benchmark Details

**Name**: AgentHarm

**Overview**: AgentHarm is a benchmark created to measure the harmfulness of LLM agents in terms of their compliance with explicit malicious requests, evaluating their functionality post-jailbreak in completing multi-step tasks.

**Data Type**: malicious agent tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AgentDojo

**Resources**:
- [Resource](https://huggingface.co/datasets/ai-safety-institute/AgentHarm)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research on the robustness of LLM agents against misuse through a diverse set of malicious tasks.

**Target Audience**:
- ML Researchers
- AI Safety Practitioners
- Ethics Researchers

**Tasks**:
- Task Completion
- Malicious Behavior Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Diverse generated tasks covering multiple harm categories.

**Size**: 440 tasks (110 unique + 330 augmented)

**Format**: JSON

**Annotation**: Manually annotated with evaluations based on specific grading rubrics.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Harm score
- Refusal rate

**Calculation**: Metrics are calculated using predefined grading rubrics assessing adherence to task requirements and outcomes.

**Interpretation**: A higher score indicates greater compliance with harmful tasks post-jailbreak.

**Baseline Results**: N/A

**Validation**: Tasks are validated through multiple rounds of human review.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Security

**Atlas Risks**:
- **Misuse**: Improper usage, Spreading disinformation

**Demographic Analysis**: N/A

**Potential Harm**: ['Facilitating harmful actions', 'Promoting illegal activities']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
