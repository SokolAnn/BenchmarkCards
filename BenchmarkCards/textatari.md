# TextAtari

## 📊 Benchmark Details

**Name**: TextAtari

**Overview**: TextAtari is a comprehensive benchmark for evaluating language agents on very long-horizon decision-making tasks spanning up to 100,000 steps.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Games

**Languages**:
- English

**Similar Benchmarks**:
- NetHack Learning Environment
- SmartPlay

**Resources**:
- [GitHub Repository](https://github.com/Lww007/Text-Atari-Agents)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate language agents' capacity for coherent decision-making across very long time horizons.

**Target Audience**:
- ML Researchers
- Game Developers
- AI Practitioners

**Tasks**:
- Sequential Decision-Making
- Strategic Planning

**Limitations**: TextAtari has substantial computational demands that may limit accessibility.

## 💾 Data

**Source**: Atari 2600 games transformed into text format

**Size**: 100,000 steps per task

**Format**: JSON

**Annotation**: Automatically generated

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Success Rate
- Performance Metrics

**Calculation**: Performance is evaluated based on completion of tasks within the specified number of decision steps.

**Interpretation**: Performance is measured as a percentage of human player competence.

**Baseline Results**: N/A

**Validation**: Standardized evaluation protocols across different games.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
