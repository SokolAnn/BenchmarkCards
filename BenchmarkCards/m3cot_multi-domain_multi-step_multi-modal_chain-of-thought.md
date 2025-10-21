# M3CoT (Multi-Domain Multi-step Multi-modal Chain-of-Thought)

## 📊 Benchmark Details

**Name**: M3CoT (Multi-Domain Multi-step Multi-modal Chain-of-Thought)

**Overview**: M3CoT introduces a novel benchmark to advance multi-domain, multi-step, and multi-modal Chain-of-Thought reasoning, addressing challenges such as the absence of visual modal reasoning and the need for complex multi-step reasoning across diverse domains.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Mathematics
- Commonsense

**Languages**:
- English

**Similar Benchmarks**:
- ScienceQA
- T-SciQA

**Resources**:
- [GitHub Repository](https://github.com/LightChen233/M3CoT)

## 🎯 Purpose and Intended Users

**Goal**: To serve as a valuable resource for evaluating multi-domain, multi-step, and multi-modal reasoning capabilities in large models.

**Target Audience**:
- ML Researchers
- Domain Experts
- Model Developers

**Tasks**:
- Multi-modal Reasoning
- Chain-of-Thought Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: ScienceQA, MATH, Sherlock datasets

**Size**: 11,459 samples

**Format**: JSON

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the performance of vision large language models on the M3CoT benchmark.

**Interpretation**: Higher accuracy indicates better reasoning performance of models across multi-step and multi-modal contexts.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
