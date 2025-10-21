# SENSE-7 (Subjective Empathy in Natural Sustained Exchanges)

## 📊 Benchmark Details

**Name**: SENSE-7 (Subjective Empathy in Natural Sustained Exchanges)

**Overview**: SENSE-7 is a human-centered digital empathy dataset comprising 695 annotated real-world conversations between information workers and Large Language Models (LLMs), reflecting user perceptions of empathy including contextual and emotional states.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- EmpatheticDialogues
- EPITOME
- ESConv

**Resources**:
- [Resource](https://arxiv.org/abs/2509.16437)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive understanding of user perceptions of empathy in AI through a human-centered and multi-dimensional framework, facilitating advancements in empathic AI designs.

**Target Audience**:
- ML Researchers
- AI Developers
- Human-Computer Interaction Researchers

**Tasks**:
- Empathy Measurement
- Conversational Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Real-world conversations between information workers and LLMs

**Size**: 695 conversations

**Format**: N/A

**Annotation**: User-annotated empathy perceptions with per-turn empathy ratings.

## 🔬 Methodology

**Methods**:
- User-annotated evaluations
- Statistical analysis
- Qualitative analysis

**Metrics**:
- Accuracy
- Spearman Correlation

**Calculation**: Metrics are calculated based on user ratings and feedback across multiple turns of conversation.

**Interpretation**: Higher scores indicate greater perceived empathy as evaluated by users in the conversation context.

**Baseline Results**: Average Spearman correlation = 0.369, Accuracy = 0.487 over a sample set of 672 conversations.

**Validation**: Validation was performed through user feedback and statistical tests on empathy ratings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: Analysis on participant demographics including age and gender influence on empathy perceptions.

**Potential Harm**: ['Misleading users into emotional dependency on AI systems', "Insufficient clarity in AI's empathic abilities"]

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Anonymization procedures were employed to protect user identities and sensitive information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants provided consent for data collection and usage in research.

**Compliance With Regulations**: Study was approved by the Microsoft Research Institutional Review Board.
