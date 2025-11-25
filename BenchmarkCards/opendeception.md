# OpenDeception

## 📊 Benchmark Details

**Name**: OpenDeception

**Overview**: OpenDeception is a novel evaluation framework featuring 50 real-world inspired scenarios that encompass five types of deception. This is the first benchmark designed to simultaneously assess the deceptive intentions and capabilities of LLMs for agent safety.

**Data Type**: open-ended scenario dataset with simulated dialogues

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- Machiavelli

**Resources**:
- [Resource](https://anonymous.4open.science/r/OpenDeception-C187/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation toolkit on AI deception risks, including the evaluation protocol and the scenario dataset.

**Target Audience**:
- AI Researchers
- Policy Makers
- AI Developers

**Tasks**:
- Deception Evaluation
- Behavior Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Manually collected real-world deception scenarios from sources like Reddit and public criminal case records.

**Size**: 50 scenarios

**Format**: N/A

**Annotation**: Manual curation by researchers to ensure validity and representativeness.

## 🔬 Methodology

**Methods**:
- AI-based simulation
- Scenario analysis

**Metrics**:
- Deception Intention Rate (DIR)
- Deception Success Rate (DeSR)
- Dialogue Success Rate (DiSR)

**Calculation**: Metrics are calculated based on the ratio of successful deceptions to total attempted conversations and deception intentions.

**Interpretation**: High DIR and DeSR values indicate significant risks of deception in evaluated LLMs.

**Validation**: The framework’s validity is established through comparisons with empirical findings from human-subject studies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Fairness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Misinformation', 'Psychological harm from deceptive interactions']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
