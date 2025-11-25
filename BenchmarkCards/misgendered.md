# MISGENDERED+

## 📊 Benchmark Details

**Name**: MISGENDERED+

**Overview**: MISGENDERED+ is an enhanced and updated benchmark for evaluating large language models' ability to handle inclusive pronoun usage, particularly focusing on nonbinary pronouns and the ability to infer gender identity from pronoun usage in context.

**Data Type**: templated instances for pronoun fidelity evaluation

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MISGENDERED

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive testbed for evaluating the handling of inclusive pronouns by language models and identify biases in their usage.

**Target Audience**:
- ML Researchers
- Gender Studies Scholars
- Ethics in AI Practitioners

**Tasks**:
- Pronoun Resolution
- Gender Identity Inference

**Limitations**: N/A

## 💾 Data

**Source**: Constructed using diverse names and pronoun categories with a focus on inclusive pronouns.

**Size**: 3.8 million templated instances

**Format**: N/A

**Annotation**: Manually annotated with varied context and pronoun usage scenarios.

## 🔬 Methodology

**Methods**:
- Zero-shot prompting
- Few-shot prompting

**Metrics**:
- Accuracy

**Calculation**: Metrics calculated based on models' performance on different pronoun types and inference tasks.

**Interpretation**: Higher accuracy indicates better understanding and handling of gender-inclusive language by LLMs.

**Baseline Results**: Previously measured results on the MISGENDERED benchmark.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Misgendering risks in language models leading to potential social and emotional harm.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
