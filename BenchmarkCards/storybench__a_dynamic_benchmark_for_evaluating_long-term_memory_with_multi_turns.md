# StoryBench: A Dynamic Benchmark for Evaluating Long-Term Memory with Multi Turns

## 📊 Benchmark Details

**Name**: StoryBench: A Dynamic Benchmark for Evaluating Long-Term Memory with Multi Turns

**Overview**: StoryBench is a dynamic benchmark framework based on interactive fiction games that evaluates long-term memory (LTM) capabilities of large language models (LLMs) by simulating complex, multi-turn interactions requiring knowledge retention and sequential reasoning.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate long-term memory capabilities of LLMs through complex, dynamic, and multi-turn narrative environments.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Sequential Reasoning
- Knowledge Retention

**Limitations**: The benchmark scenarios are derived from a single interactive fiction domain, and the number of turns and length of the context are limited.

## 💾 Data

**Source**: The dataset is constructed from the interactive fiction game The Invisible Guardian.

**Size**: 311 scene nodes and 86 choice nodes

**Format**: JSON

**Annotation**: Manual annotation preserves the game's branching logic and causal relationships, ensuring chronological ordering.

## 🔬 Methodology

**Methods**:
- Systematic evaluations on advanced LLMs
- Comparative analysis across different benchmark tasks

**Metrics**:
- Overall Accuracy
- First-Try Accuracy
- Longest Consecutive Correct Sequence
- Accuracy by Difficulty

**Calculation**: Metrics are calculated based on the proportion of correct decisions made during the interactions.

**Interpretation**: Higher scores in metrics indicate better knowledge retention and sequential reasoning capabilities.

**Validation**: The benchmark's effectiveness is validated through detailed experiments and in-depth failure analysis.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
