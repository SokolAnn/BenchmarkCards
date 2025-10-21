# SAGE-Eval (SAfety-fact systematic GEneralization evaluation)

## 📊 Benchmark Details

**Name**: SAGE-Eval (SAfety-fact systematic GEneralization evaluation)

**Overview**: SAGE-Eval is the first benchmark designed to assess whether LLMs correctly apply well-established safety facts to naive user queries. It targets implicit safety risks and aims to evaluate LLMs' generalization abilities regarding safety.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AgentHarm
- HELM
- WMDP
- GPQA
- AdvBench
- HarmBench
- SALAD-Bench

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the generalization capability of LLMs regarding safety facts and improve their reliability in addressing safety risks.

**Target Audience**:
- ML Researchers
- AI Developers
- Safety Evaluators

**Tasks**:
- Safety Evaluation
- Generalization Testing

**Limitations**: N/A

## 💾 Data

**Source**: Human-validated prompts formed from safety facts sourced from reputable organizations like the CDC and FDA.

**Size**: 10,428 test scenarios

**Format**: JSON

**Annotation**: Manually verified by 144 human annotators

## 🔬 Methodology

**Methods**:
- Human evaluation
- LLM-as-a-judge

**Metrics**:
- Model-level Safety Score
- Area under Safety Curve
- Fact-level Safety Score

**Calculation**: Metrics are calculated based on the proportion of safety facts that models responded to correctly under varying conditions.

**Interpretation**: A higher safety score indicates better performance in addressing safety concerns in naive queries.

**Validation**: Validated by human annotators with an average reliability rate.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Fairness**: Output bias
- **Robustness**: Evasion attack

**Potential Harm**: ['Potential risk of safety oversights causing harm to vulnerable populations such as children.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
