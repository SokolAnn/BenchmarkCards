# AssertBench

## 📊 Benchmark Details

**Name**: AssertBench

**Overview**: AssertBench evaluates the self-assertion capabilities of Large Language Models (LLMs) by measuring their ability to maintain consistent truth evaluations across contradictory user assertions about facts.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- FACTOR
- SycEval
- Persuasive-Pairs
- Belief-R
- OpenFactCheck

**Resources**:
- [GitHub Repository](https://github.com/achowd32/assert-bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the epistemic robustness of Large Language Models in the context of user assertions and how effectively they can maintain factual consistency under misleading inputs.

**Target Audience**:
- ML Researchers
- AI Developers

**Tasks**:
- Factual Consistency Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: FEVEROUS dataset

**Size**: 2000 facts

**Format**: CSV

**Annotation**: Facts are verified against evidence and labeled as 'SUPPORTS', 'REFUTES', or 'NOT ENOUGH INFO'.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Assertion Rate
- Calibration Error

**Calculation**: The assertion rate is calculated based on the percentage of facts for which the model maintains consistent evaluations across user framing. Calibration error is measured by the RMS error of confidence scores against factual accuracy.

**Interpretation**: Higher assertion rates indicate greater model robustness in maintaining factual truth under user claims. Lower calibration error suggests better alignment of confidence levels with actual performance.

**Baseline Results**: N/A

**Validation**: Results are stratified by whether the model knew the facts under neutral prompting conditions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
