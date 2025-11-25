# FutureX (An Advanced Live Benchmark for LLM Agents in Future Prediction)

## 📊 Benchmark Details

**Name**: FutureX (An Advanced Live Benchmark for LLM Agents in Future Prediction)

**Overview**: FutureX is a dynamic and live evaluation benchmark specifically designed for LLM agents performing future prediction tasks. It supports real-time daily updates and eliminates data contamination through an automated pipeline for question gathering and answer collection.

**Data Type**: future prediction queries

**Domains**:
- Natural Language Processing
- Finance
- Politics
- Economics
- Healthcare
- Sports
- Technology

**Languages**:
- English

**Similar Benchmarks**:
- AgentBench
- WebArena
- GAIA

**Resources**:
- [Resource](https://futurex-ai.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To establish a dynamic, contamination-free evaluation standard that drives the development of LLM agents capable of performing advanced future prediction at the level of professional human analysts.

**Target Audience**:
- ML Researchers
- Data Scientists
- Industry Practitioners

**Tasks**:
- Future Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from 195 curated websites across diverse domains.

**Size**: Approx. 500 future prediction queries per week

**Format**: N/A

**Annotation**: Automated collection and evaluation pipeline

## 🔬 Methodology

**Methods**:
- Automated metrics
- Dynamic live evaluation

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics are calculated based on the agents' predictions against ground-truth outcomes obtained after events resolve.

**Interpretation**: Higher scores indicate better predictive capabilities and reasoning under uncertainty.

**Baseline Results**: N/A

**Validation**: The benchmark is validated through cross-model comparisons, with performance tracked and updated daily.

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

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
