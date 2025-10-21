# Multi-Turn Puzzles

## 📊 Benchmark Details

**Name**: Multi-Turn Puzzles

**Overview**: The Multi-Turn Puzzles benchmark consists of a suite of multi-turn tasks designed to evaluate the reasoning, interactive dialogue, and information-seeking abilities of large language models (LLMs). It includes tasks such as Word Guess, Movie Recommendation, Circuit Decoding, Word Chaining, and Twenty Questions, aiming to provide insights into the strengths and weaknesses of current LLMs in handling complex, interactive scenarios.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/arianhosseini/mt_puzzles)

## 🎯 Purpose and Intended Users

**Goal**: To assess and enhance the interactive reasoning and strategic dialogue capabilities of large language models through a structured benchmark.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Word Guess
- Movie Recommendation
- Circuit Decoding
- Word Chaining
- Twenty Questions

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic data created through rule-based environments.

**Size**: 400 unique vocabulary configurations for Word Guess, 1000 configurations for Movie Recommendation, 300 configurations for Circuit Decoding, and 400 configurations for Word Chaining and Twenty Questions.

**Format**: N/A

**Annotation**: Automatically evaluated using deterministic scoring rules.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Success Rate
- Normalized attempts

**Calculation**: Metrics are calculated based on deterministic scoring rules associated with each specific task.

**Interpretation**: Higher success rates and lower normalized attempts indicate better performance in reasoning and interaction tasks.

**Baseline Results**: Not explicitly provided.

**Validation**: Evaluation of frontier models demonstrates performance across the tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
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
