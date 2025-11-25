# BELLS (Benchmarks for the Evaluation of LLM Safeguards)

## 📊 Benchmark Details

**Name**: BELLS (Benchmarks for the Evaluation of LLM Safeguards)

**Overview**: BELLS is a structured collection of tests that evaluate input-output safeguards for Large Language Models (LLMs). It includes established failure tests, emerging failure tests, and next-gen architecture tests, to ensure the robustness of safeguards against both known and unknown failure modes.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark that guides the development of robust safeguards that act as early detection systems for risks of harm arising from new behaviors, use cases, or attacks in LLM applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Anomaly Detection
- Input-Output Safeguards Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Generated traces from two LLM-agents using different steering prompts in the Machiavelli benchmark, capturing various ethical behaviors.

**Size**: 1,200 traces

**Format**: JSON

**Annotation**: Traces annotated with ethical violations and harm scores based on agent actions.

## 🔬 Methodology

**Methods**:
- Baseline Detection
- Automated metrics

**Metrics**:
- Area Under the Precision-Recall Curve (AUPRC)

**Calculation**: AUPRC is calculated based on the classification precision and recall for detecting unethical behavior in agent traces.

**Interpretation**: Higher AUPRC score indicates better detection capability of unethical behavior by the safeguards.

**Baseline Results**: A baseline detection mechanism achieving a 0.97 AUPRC score after 80 steps in the environment.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Privacy
- Accuracy

**Atlas Risks**:
- **Societal Impact**: Impact on Jobs, Impact on affected communities
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
