# FlashAdventure

## 📊 Benchmark Details

**Name**: FlashAdventure

**Overview**: FlashAdventure is a benchmark of 34 diverse Flash-based adventure games designed to evaluate GUI agents’ ability to complete full story arcs.

**Data Type**: gameplay actions

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- PokeLLMon
- Cradle
- VisEscape

**Resources**:
- [Resource](https://ahnjaewoo.github.io/flashadventure)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate GUI agents solving full story arcs in diverse adventure games.

**Target Audience**:
- ML Researchers
- Game Developers
- AI Practitioners

**Tasks**:
- Task Completion
- Pathfinding
- Behavior Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: 34 Flash-based adventure games from the FlashPoint Archive.

**Size**: 34 games

**Format**: N/A

**Annotation**: Game state is automatically evaluated via the CUA-as-a-Judge framework.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Success Rate
- Milestone Completion Rate

**Calculation**: Success is evaluated based on whether the final narrative goal is achieved.

**Interpretation**: A higher percentage indicates better performance in completing story arcs.

**Baseline Results**: N/A

**Validation**: Evaluated against human performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All participants provided informed consent.

**Data Licensing**: Games used for non-commercial, academic research purposes only, permissions obtained from rights holders.

**Consent Procedures**: Detailed consent process for human gameplay demonstrations.

**Compliance With Regulations**: Not Applicable
