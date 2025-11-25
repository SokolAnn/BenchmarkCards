# CONFLICT BANK

## 📊 Benchmark Details

**Name**: CONFLICT BANK

**Overview**: CONFLICT BANK is the first comprehensive benchmark developed to systematically evaluate knowledge conflicts in Large Language Models (LLMs) from three aspects: (i) conflicts encountered in retrieved knowledge, (ii) conflicts within the models’ encoded knowledge, and (iii) the interplay between these conflict forms. It includes 7,453,853 claim-evidence pairs and 553,117 QA pairs.

**Data Type**: claim-evidence pairs, question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [Resource](https://huggingface.co/datasets/Warrieryes/CB_claim_evidence)
- [Resource](https://huggingface.co/datasets/Warrieryes/CB_qa)
- [GitHub Repository](https://github.com/zhaochen0110/conflictbank)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale, diverse, and realistic benchmark to study knowledge conflicts in LLMs and how they affect model behavior and reliability.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Wikidata and generated evidence through LLMs.

**Size**: 7,453,853 claim-evidence pairs and 553,117 QA pairs

**Format**: JSON, CSV

**Annotation**: Data was generated and curated through a systematic pipeline including fact-evidence entailment checking.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Memorization Ratio (MR)
- Original Answer Ratio (OAR)
- Counter Answer Ratio (CAR)

**Calculation**: Metrics are calculated based on model performance evaluations comparing default answers to those impacted by conflicting information.

**Interpretation**: Higher memorization ratios indicate greater reliance on internal parametric memory, while lower ratios suggest adoption of conflicting knowledge.

**Baseline Results**: N/A

**Validation**: Pilot experiments conducted on twelve LLMs across four model families.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Misuse**: Spreading disinformation

**Demographic Analysis**: N/A

**Potential Harm**: This benchmark aims to analyze how knowledge conflicts might lead to disinformation and affect model outputs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Public domain license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
