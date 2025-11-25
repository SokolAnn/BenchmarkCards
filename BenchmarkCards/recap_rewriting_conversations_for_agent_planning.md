# RECAP (REwriting Conversations for Agent Planning)

## 📊 Benchmark Details

**Name**: RECAP (REwriting Conversations for Agent Planning)

**Overview**: RECAP is a new benchmark designed to evaluate and advance intent rewriting by reframing user-agent dialogues into concise representations of user goals. It captures diverse challenges such as ambiguity, intent drift, vagueness, and mixed-goal conversations.

**Data Type**: user-agent dialogues

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/megagonlabs/recap)

## 🎯 Purpose and Intended Users

**Goal**: To enable a deeper understanding of how to effectively represent complex user intent for agent planning.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Intent Rewriting
- Agent Planning

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic conversations generated to reflect realistic user-agent interactions across various topics.

**Size**: 750 instances

**Format**: N/A

**Annotation**: Conversations were carefully vetted for coherency and adherence to the assigned challenge type.

## 🔬 Methodology

**Methods**:
- Human evaluation
- LLM-based evaluation

**Metrics**:
- Node and Edge Count Differences
- Graph Edit Distance
- BERTScore

**Calculation**: Metrics were calculated based on the differences in generated plans following rewrites of user-agent dialogues.

**Interpretation**: Higher scores in the metrics indicate better quality rewrites and planning outcomes.

**Validation**: Plans validated against human preferences and various automatically computed metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Conversations were generated with attention to removing personal identifiable information and ensuring ethical vetting.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
