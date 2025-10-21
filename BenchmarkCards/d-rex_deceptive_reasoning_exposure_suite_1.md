# D-REX (Deceptive Reasoning Exposure Suite)

## 📊 Benchmark Details

**Name**: D-REX (Deceptive Reasoning Exposure Suite)

**Overview**: D-REX is a benchmark designed to evaluate the discrepancy between a model's internal reasoning process and its final output, addressing the problem of deceptive reasoning in large language models.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AILuminate
- StrongReject
- TruthfulQA
- OpenDeception

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the safety and alignment of large language models by detecting deceptive reasoning that results in benign outputs with hidden malicious intent.

**Target Audience**:
- ML Researchers
- Safety Engineers
- AI Alignment Researchers

**Tasks**:
- Safety Evaluation
- Deception Detection

**Limitations**: N/A

## 💾 Data

**Source**: Data constructed through a competitive red-teaming exercise where adversarial system prompts were crafted to induce deceptive behaviors.

**Size**: 8,162 samples

**Format**: N/A

**Annotation**: Crowdsourced via competitive exercises.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Detection Evasion
- Output Camouflage
- Malicious Internal Reasoning

**Calculation**: Models are evaluated based on their responses to adversarial prompts by comparing their internal reasoning to expected patterns of deceptive behavior.

**Interpretation**: High scores indicate a model's strong deceptive behavior, where benign outputs mask malicious internal reasoning.

**Validation**: Evaluation against a range of criteria using multiple judge LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Accuracy**: Unrepresentative data

**Potential Harm**: ['Promotion of harmful conspiratorial thinking', 'Erosion of trust in factual historical accounts']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
