# SAFEARENA

## 📊 Benchmark Details

**Name**: SAFEARENA

**Overview**: SAFEARENA is the first benchmark to focus on the deliberate misuse of web agents, comprising 250 safe and 250 harmful tasks across four websites. It assesses realistic misuses of web agents in five harm categories: misinformation, illegal activity, harassment, cybercrime, and social bias.

**Data Type**: task pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- VisualWebArena-Adversarial
- ST-WebAgentBench

**Resources**:
- [Resource](https://safearena.github.io)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of SAFEARENA is to evaluate the safety of autonomous web agents against misuse in real-world web environments.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Task Completion
- Task Refusal

**Limitations**: N/A

## 💾 Data

**Source**: Tasks designed as safe and harmful pairs by human curators and through human-in-the-loop methods.

**Size**: 500 tasks

**Format**: JSON

**Annotation**: Manually verified by experts in LLM agents and safety research.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Task Completion Rate
- Refusal Rate
- Normalized Safety Score (NSS)

**Calculation**: Metrics are calculated based on task completion outcomes against predefined performance criteria.

**Interpretation**: Higher task completion rates indicate better performance; lower refusal rates indicate worse safety adherence.

**Baseline Results**: N/A

**Validation**: Validation performed through extensive human review and cross-evaluation between automated and human assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Privacy
- Fairness

**Atlas Risks**:
- **Fairness**: Output bias
- **Privacy**: Data privacy rights alignment
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Misinformation', 'Illegal Activity', 'Harassment', 'Cybercrime', 'Social Bias']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
