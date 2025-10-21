# GLEE: A Unified Framework and Benchmark for Language-based Economic Environments

## 📊 Benchmark Details

**Name**: GLEE: A Unified Framework and Benchmark for Language-based Economic Environments

**Overview**: GLEE provides a unified framework for standardizing research on two-player, sequential, language-based games, defining three base families of games with consistent parameterization and economic measures to evaluate agents' performance.

**Data Type**: decision-making interactions

**Domains**:
- Economics
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Rational Players
- GAMA-Bench
- GTBench
- Game theoretic LLM
- TMGBench
- CompeteAI

**Resources**:
- [GitHub Repository](https://github.com/eilamshapira/GLEE)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the behavior of Large Language Models (LLMs) in language-based economic games.

**Target Audience**:
- ML Researchers
- Economists
- Behavioral Scientists

**Tasks**:
- Bargaining
- Negotiation
- Persuasion

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from LLM vs. LLM and human vs. LLM interactions across diverse economic games.

**Size**: 80,000 games

**Format**: JSON

**Annotation**: Automatically generated interactions from predefined game scenarios.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Efficiency
- Fairness
- Self-gain

**Calculation**: Metrics are based on game outcomes and normalized for comparison across setups.

**Interpretation**: Higher values signify more efficient and fair outcomes.

**Validation**: Cross-validation using statistical models to assess input feature impacts on outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Safety

**Atlas Risks**:
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: Potential for misuse of LLM behavior modeling in economic contexts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants were required to pass attention checks and were informed about data collection.

**Compliance With Regulations**: The study follows ethical guidelines for the collection of human data.
