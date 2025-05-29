# MedHallBench

## 📊 Benchmark Details

**Name**: MedHallBench

**Overview**: A comprehensive benchmark framework for evaluating and mitigating hallucinations in Medical Large Language Models (MLLMs).

**Data Type**: Textual Case Scenarios

**Domains**:
- Healthcare
- Medical Imaging

**Languages**:
- English

**Similar Benchmarks**:
- MedQA
- MedMCQA
- MultiMedQA
- Med-HALT

**Resources**:
- [Resource](Assessment of Caption Hallucinations in Medical Imagery (ACHMI))

## 🎯 Purpose and Intended Users

**Goal**: To assess and mitigate hallucinations in medical large language models.

**Target Audience**:
- Researchers
- Medical Professionals
- AI Developers

**Tasks**:
- Evaluating model outputs
- Mitigating hallucinations
- Improving clinical decision-making

**Limitations**: None

## 💾 Data

**Source**: Expert validated medical case scenarios and established medical databases.

**Size**: N/A

**Format**: N/A

**Annotation**: Expert-validated annotations using structured protocols.

## 🔬 Methodology

**Methods**:
- Automated annotation
- Expert evaluations
- Reinforcement learning with human feedback

**Metrics**:
- ACHMI
- BLEU
- ROUGE-1
- ROUGE-2
- METEOR
- BertScore

**Calculation**: Metrics are calculated based on comparisons with expert evaluations and existing medical benchmarks.

**Interpretation**: Scores indicate the degree of accuracy and hallucination in model outputs.

**Baseline Results**: Comparison with state-of-the-art models established various benchmark results.

**Validation**: Multi-tiered evaluation system combining expert assessments and quantitative metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Data contamination
- Model accuracy
- Hallucinations

**Atlas Risks**:
- **Accuracy**: Data contamination, Poor model accuracy
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: Potentially harmful misdiagnoses or inappropriate treatment arising from hallucinations in medical domain outputs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data privacy is ensured through expert-validation and compliance with consultation standards.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Dataset ensures compliance with international consultation standards.
