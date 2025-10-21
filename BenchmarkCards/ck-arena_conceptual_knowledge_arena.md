# CK-Arena (Conceptual Knowledge Arena)

## 📊 Benchmark Details

**Name**: CK-Arena (Conceptual Knowledge Arena)

**Overview**: CK-Arena is a game-based benchmark designed to evaluate the ability of Large Language Models (LLMs) to understand conceptual knowledge boundaries through interactive, multi-agent gameplay. It challenges models to reason about semantic similarities and distinctions in complex scenarios, simulating real-world interactions.

**Data Type**: concept pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- HellaSwag
- BIG-Bench

**Resources**:
- [Resource](https://ck-arena.site)

## 🎯 Purpose and Intended Users

**Goal**: To provide a scalable and realistic benchmark for assessing conceptual reasoning in dynamic environments for Large Language Models.

**Target Audience**:
- ML Researchers
- AI Developers
- Educational Researchers

**Tasks**:
- Conceptual Reasoning

**Limitations**: CK-Arena is currently effective primarily for evaluating noun-based concepts, and all evaluations are conducted in English.

## 💾 Data

**Source**: Constructed dataset of semantically related concept pairs

**Size**: 529 English concept pairs

**Format**: N/A

**Annotation**: Manual curation to ensure semantic proximity and descriptive clarity

## 🔬 Methodology

**Methods**:
- Game-based evaluation
- LLM interactions
- Automated scoring by LLM judges

**Metrics**:
- Win Rate
- Survival Rate
- Novelty
- Relevance
- Reasonableness

**Calculation**: Metrics are calculated based on a combination of player performance and statement evaluations utilizing specific scoring criteria.

**Interpretation**: Higher scores indicate stronger conceptual understanding and effective communication in the game context.

**Baseline Results**: Results from evaluations of six popular LLMs demonstrating varying strengths and weaknesses in conceptual reasoning.

**Validation**: Games are played in controlled conditions with multiple LLM judges for consistency

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The research does not involve collecting personally identifiable information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
