# VideoGameBench

## 📊 Benchmark Details

**Name**: VideoGameBench

**Overview**: VideoGameBench is a benchmark consisting of 10 popular video games from the 1990s that vision-language models (VLMs) directly interact with in real-time to complete game objectives, without any game-specific scaffolding or auxiliary information.

**Data Type**: gameplay interaction data

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- Gemini Plays Pokemon
- Gemini Plays Doom

**Resources**:
- [Resource](https://vgbench.com)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of vision-language models in completing complex video games and challenge their performance in real-time environments.

**Target Audience**:
- ML Researchers
- Game Developers
- AI Researchers

**Tasks**:
- Game Playing
- Interactive Decision Making

**Limitations**: Limited to games from the 1990s, may not adequately represent modern gaming challenges.

## 💾 Data

**Source**: Players and walkthrough data used to construct checkpoints for evaluation.

**Size**: 23 games

**Format**: N/A

**Annotation**: Data scraping from YouTube video walkthroughs for checkpoint detection.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Percentage of game completed
- Checkpoint achievement

**Calculation**: Each game is scored based on the percentage of checkpoints reached against the total number of checkpoints.

**Interpretation**: Scores represent the percentage of each game completed, with higher scores indicating better performance.

**Baseline Results**: Gemini 2.5 Pro reached up to 0.48% on VideoGameBench.

**Validation**: Games were manually verified by human players to ensure they can be completed.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
