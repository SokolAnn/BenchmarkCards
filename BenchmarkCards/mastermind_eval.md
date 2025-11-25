# MASTERMIND EVAL

## 📊 Benchmark Details

**Name**: MASTERMIND EVAL

**Overview**: MASTERMIND EVAL is a simple, scalable, and interpretable deductive reasoning benchmark inspired by the board game Mastermind, which assesses the reasoning capabilities of language models through two evaluation paradigms: agentic evaluation and deductive reasoning evaluation.

**Data Type**: game states

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LogiQA
- ReClor
- FOLIO
- LogicBench

**Resources**:
- [GitHub Repository](https://github.com/flairNLP/mastermind)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the strategic gameplay and deductive reasoning capabilities of language models using the game of Mastermind.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Deductive Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Generated dataset of over 30,000 pre-played game states based on the Mastermind game using Knuth’s algorithm.

**Size**: over 30,000 examples

**Format**: N/A

**Annotation**: Automatically generated

## 🔬 Methodology

**Methods**:
- Agentic evaluation
- Deductive reasoning evaluation
- Multiple-choice evaluation

**Metrics**:
- Solve rate

**Calculation**: The solve rate is defined as the fraction of games in which the model correctly identifies the concealed code within the allowed number of guesses.

**Interpretation**: A higher solve rate indicates better reasoning capabilities of the language model in the game.

**Baseline Results**: N/A

**Validation**: Each model plays 100 games to evaluate their performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
