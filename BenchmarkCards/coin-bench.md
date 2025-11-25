# CoIN-Bench

## 📊 Benchmark Details

**Name**: CoIN-Bench

**Overview**: CoIN-Bench is a new benchmark featuring the challenging multi-instance scenarios of Collaborative Instance Object Navigation (CoIN), supporting evaluation with both human and simulated user-agent interactions for reproducibility.

**Data Type**: navigation episodes

**Domains**:
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- GOAT-Bench

**Resources**:
- [Resource](https://intelligolabs.github.io/CoIN)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the evaluation of the CoIN task by providing a benchmark that assesses the performance of navigation agents in multi-instance scenarios through human-agent dialogues.

**Target Audience**:
- ML Researchers
- Robotics Practitioners

**Tasks**:
- Instance Object Navigation

**Limitations**: N/A

## 💾 Data

**Source**: Constructed as a filtered subset of the GOAT-Bench dataset focusing on multi-instance scenarios.

**Size**: 1,649 evaluation episodes

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Simulated user-agent interactions

**Metrics**:
- Success Rate (SR)
- Success Rate weighted by Path Length (SPL)
- Average Number of Questions asked (NQ)

**Calculation**: Metrics are calculated based on the agent's performance in achieving the navigation goal and the amount of user interaction required.

**Interpretation**: Higher SR indicates successful navigation to the target instance with fewer interactions.

**Baseline Results**: AIUTA performs competitively against state-of-the-art Instance Object Navigation methods.

**Validation**: Evaluated both through real human interactions and simulated interactions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
