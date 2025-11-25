# TEXTQUESTS

## 📊 Benchmark Details

**Name**: TEXTQUESTS

**Overview**: TEXTQUESTS is a benchmark based on the Infocom suite of interactive fiction games, designed to assess an LLM agent’s capacity for self-contained problem-solving through long-context reasoning in exploratory environments.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://textquests.ai)

## 🎯 Purpose and Intended Users

**Goal**: To enable a more accurate assessment of AI agents in challenging exploratory environments that require sustained, self-directed reasoning.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Game Developers

**Tasks**:
- Text-based Game Navigation
- Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Classic Infocom interactive fiction games.

**Size**: 25 games

**Format**: N/A

**Annotation**: Using built-in game annotations and external InvisiClues hint booklets for context.

## 🔬 Methodology

**Methods**:
- Game Progress tracking
- Harm assessment

**Metrics**:
- Average Game Progress
- Average Harm

**Calculation**: Game Progress is calculated based on labeled checkpoints for essential puzzles across the games.

**Interpretation**: Models are compared based on their ability to complete games and manage in-game actions without external help.

**Validation**: Formalized through comparative analysis with previous game progress metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Hallucination

**Potential Harm**: ['Measuring harmful actions based on ethical implications in gameplay.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
