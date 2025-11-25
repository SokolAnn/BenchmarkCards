# AVALON BENCH

## 📊 Benchmark Details

**Name**: AVALON BENCH

**Overview**: AVALON BENCH is a comprehensive game environment tailored for evaluating multi-agent LLM Agents in the strategic social deduction game Resistance Avalon. It includes a game environment, rule-based bots as baseline opponents, and ReAct-style LLM agents with tailored prompts for each role.

**Data Type**: game interactions and outcomes

**Domains**:
- Artificial Intelligence
- Game Theory

**Languages**:
- English

**Similar Benchmarks**:
- AgentBench

**Resources**:
- [GitHub Repository](https://github.com/jonathanmli/Avalon-LLM)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate multi-agent LLM Agents in the context of the social deduction game Resistance Avalon.

**Target Audience**:
- Researchers
- Game Developers
- AI Practitioners

**Tasks**:
- Multi-Agent Decision Making
- Game Strategy Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Game interactions between LLM agents and rule-based bots.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Benchmarking against rule-based bots
- Multi-agent interaction simulation

**Metrics**:
- Win rate
- Deduction accuracy

**Calculation**: Win rates are calculated based on the outcomes of games played by LLM agents against deterministic rule-based bots.

**Interpretation**: A higher win rate indicates better performance and strategic capabilities of the LLM agents in the game.

**Baseline Results**: Baseline results indicate that LLM agents like ChatGPT achieved a win rate of 22.2% in good-role and 66.7% in evil-role against naive bots.

**Validation**: Evaluations based on game outcomes and decision-making capabilities observed during game play.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack
- **Fairness**: Decision bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
