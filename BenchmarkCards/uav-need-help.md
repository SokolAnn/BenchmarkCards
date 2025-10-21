# UAV-Need-Help

## 📊 Benchmark Details

**Name**: UAV-Need-Help

**Overview**: UAV-Need-Help is an assistant-guided UAV object search benchmark that helps UAVs navigate to target objects using descriptions and guidance. It provides varying levels of assistance to improve performance in realistic VLN tasks.

**Data Type**: trajectory-instruction pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- R2R
- TouchDown
- AerialVLN

**Resources**:
- [GitHub Repository](https://github.com/prince687028/OpenUAV)

## 🎯 Purpose and Intended Users

**Goal**: To promote research and development in UAV vision-language navigation tasks through realistic trajectories and assistant-guided object searches.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Domain Experts

**Tasks**:
- Vision-Language Navigation
- Object Search

**Limitations**: N/A

## 💾 Data

**Source**: Constructed using the OpenUAV platform with real flight simulation data and human control.

**Size**: 12,149 trajectories

**Format**: N/A

**Annotation**: Human annotators conducted a continuous flight on the OpenUA V platform, generating descriptions using GPT-4 and reviewing for quality.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Success Rate (SR)
- Oracle Success Rate (OSR)
- Success weighted by Path Length (SPL)
- Navigation Error (NE)

**Calculation**: Metrics are calculated based on UAV's success in navigating to target objects as per provided instructions in various scenarios.

**Interpretation**: Higher metrics indicate better navigation performance and efficiency in reaching target locations.

**Baseline Results**: Compared against Random, Fixed Action, and CMA models with results indicating significant improvements over baselines.

**Validation**: Validated through closed-loop evaluations and comparisons across metrics in seen and unseen environments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness
- Fairness

**Atlas Risks**:
- **Fairness**: Output bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
