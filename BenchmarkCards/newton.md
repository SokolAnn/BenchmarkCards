# NEWTON

## 📊 Benchmark Details

**Name**: NEWTON

**Overview**: NEWTON is a repository and benchmark for evaluating the physics reasoning skills of large language models (LLMs), comprising 160K QA questions and 2800 object-attribute pairs to assess physical reasoning capabilities.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- PIQA
- PROST

**Resources**:
- [Resource](https://newtonreasoning.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To enable comprehensive evaluation of language models’ physical reasoning capabilities regarding everyday objects.

**Target Audience**:
- ML Researchers
- Robotic Developers

**Tasks**:
- Physical Reasoning

**Limitations**: The dataset's categories do not encompass the full range of real-world objects, limiting evaluation scenarios.

## 💾 Data

**Source**: Crowdsourced annotations based on object-attribute pairs collected from 3D object datasets.

**Size**: 160,000 questions

**Format**: N/A

**Annotation**: 3-point Likert scale annotations from at least four annotators per object-attribute pair.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Agreement

**Calculation**: Agreement is calculated based on the percentage of responses aligning with the majority human response. Accuracy measures the percentage aligning with the ground truth solution.

**Interpretation**: Higher percentages indicate better alignment with human reasoning.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
