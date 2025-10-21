# MARS-Bench (Multi-turn Athletic Real-world Scenario Dialogue Benchmark)

## 📊 Benchmark Details

**Name**: MARS-Bench (Multi-turn Athletic Real-world Scenario Dialogue Benchmark)

**Overview**: MARS-Bench is constructed from play-by-play text commentary to evaluate multi-turn dialogue robustness and long-context understanding in large language models. It focuses on Ultra Multi-turn, Interactive Multi-turn, and Cross-turn Tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Sports

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- MT-Bench
- MultiChallenge
- MT-Bench-101

**Resources**:
- [Resource](https://syuchin.github.io/MARS-Bench/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of large language models' abilities in handling complex multi-turn dialogues.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Instruction Following
- Context Retrieval
- Information Reasoning
- Task Switching

**Limitations**: Domain specificity may limit generalizability to open-domain dialogues; modality is limited to text.

## 💾 Data

**Source**: Play-by-play text commentary from NBA and NHL games, structured for multi-turn dialogue modeling.

**Size**: 120 games

**Format**: Structured text

**Annotation**: Manually crafted questions based on game records.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are computed based on task-specific checklists comparing model outputs with ground truth.

**Interpretation**: Scores are interpreted to assess dialogue comprehension and reasoning across turns.

**Baseline Results**: Comparative performances against existing benchmarks.

**Validation**: Validated through extensive testing on various LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
