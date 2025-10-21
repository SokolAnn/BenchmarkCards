# PersonaLens

## 📊 Benchmark Details

**Name**: PersonaLens

**Overview**: PersonaLens is a comprehensive benchmark designed for evaluating personalization in task-oriented AI assistants, featuring diverse user profiles, rich preferences, interaction histories, and specialized LLM-based agents to assess personalization quality.

**Data Type**: dialogue interactions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- PersonaChat
- LaMP
- PENS

**Resources**:
- [GitHub Repository](https://github.com/amazon-science/PersonaLens)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate personalization capabilities in task-oriented conversational AI assistants.

**Target Audience**:
- AI Researchers
- Conversational AI Developers
- Natural Language Processing Practitioners

**Tasks**:
- Personalization Assessment
- Task-oriented Dialogue Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Generated from diverse user profiles and interaction scenarios.

**Size**: 122,133 dialogues

**Format**: JSON

**Annotation**: Generated using LLMs

## 🔬 Methodology

**Methods**:
- Automated evaluation
- User simulation

**Metrics**:
- Task Completion Rate (TCR)
- Personalization score (P)
- Naturalness
- Coherence

**Calculation**: Metrics are computed based on user-agent interactions and evaluation criteria set for personalization and task performance.

**Interpretation**: Higher scores indicate better performance in personalization and task completion capability.

**Baseline Results**: N/A

**Validation**: Extensive empirical validation against user behavior and preferences.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark includes a diverse representation across demographic factors such as age, gender, and ethnicity.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
