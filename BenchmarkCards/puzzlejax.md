# PuzzleJAX

## 📊 Benchmark Details

**Name**: PuzzleJAX

**Overview**: PuzzleJAX is a GPU-accelerated puzzle game engine and description language designed for benchmarking tree search, reinforcement learning, and LLM reasoning abilities. It allows the dynamic compilation of games expressible in its domain-specific language, supporting a wide variety of puzzle games.

**Data Type**: environment dynamics and objectives

**Domains**:
- Artificial Intelligence

**Languages**:
- English

**Similar Benchmarks**:
- PuzzleScript

**Resources**:
- [GitHub Repository](https://github.com/smearle/script-doctor)

## 🎯 Purpose and Intended Users

**Goal**: To provide a diverse and challenging benchmark for evaluating AI agents in puzzle-solving tasks across various cognitive skills.

**Target Audience**:
- AI Researchers
- Game Developers
- Machine Learning Practitioners

**Tasks**:
- Reinforcement Learning
- Tree Search Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Generated from human-authored games and self-defined puzzles in PuzzleJAX's description language.

**Size**: 951 total games, 7957 total levels

**Format**: Various game formats defined in a domain-specific language

**Annotation**: Games are validated through breadth-first search and replaying actions to ensure consistent behavior.

## 🔬 Methodology

**Methods**:
- Breadth-First Search
- Reinforcement Learning

**Metrics**:
- Win Rate

**Calculation**: Performance metrics are evaluated based on the success of agents in solving a variety of puzzle games within specified iteration limits.

**Interpretation**: A higher win rate indicates better problem-solving capabilities of the AI agents tested in the benchmark.

**Validation**: Games were validated by comparing outcomes from the JavaScript implementation of PuzzleScript with results from PuzzleJAX.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
