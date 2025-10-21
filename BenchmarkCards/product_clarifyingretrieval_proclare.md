# PROduct CLArifyingREtrieval (PROCLARE)

## 📊 Benchmark Details

**Name**: PROduct CLArifyingREtrieval (PROCLARE)

**Overview**: This paper introduces the PROCLARE benchmark to evaluate the performance of a conversational product search agent, ProductAgent, designed to clarify user demands through dialog and strategic questioning.

**Data Type**: dialogue exchanges

**Domains**:
- Natural Language Processing
- E-commerce

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2407.00942)

## 🎯 Purpose and Intended Users

**Goal**: To provide an automatic evaluation framework for conversational product demand clarification agents.

**Target Audience**:
- Research Scientists
- Data Scientists
- Industry Practitioners

**Tasks**:
- Information Retrieval

**Limitations**: The benchmark relies on a user simulation technique, lacking direct human user interaction.

## 💾 Data

**Source**: Produced by simulating dialogues between a user simulator and the ProductAgent.

**Size**: 2,000 dialogues

**Format**: JSON

**Annotation**: Automatically generated via an LLM-driven user simulator.

## 🔬 Methodology

**Methods**:
- Automated metrics
- User simulation

**Metrics**:
- Mean Reciprocal Rank (MRR)
- Hit Rate

**Calculation**: Calculated based on the retrieved product relevance after each dialog turn.

**Interpretation**: Higher MRR and Hit Rate values indicate better performance in guiding users to relevant products.

**Validation**: Evaluated against traditional information retrieval benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
