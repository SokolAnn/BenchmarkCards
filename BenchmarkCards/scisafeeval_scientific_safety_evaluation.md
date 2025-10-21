# SCISAFEEVAL (Scientific Safety Evaluation)

## 📊 Benchmark Details

**Name**: SCISAFEEVAL (Scientific Safety Evaluation)

**Overview**: SCISAFEEVAL is a comprehensive benchmark designed to evaluate the safety alignment of large language models (LLMs) across a range of scientific tasks, encompassing multiple scientific languages including textual, molecular, protein, and genomic. It challenges LLMs to assess their safety and robustness in scientific applications.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SciMT-Safety
- SciKnowEval-L4

**Resources**:
- [Resource](https://arxiv.org/abs/2410.03769)

## 🎯 Purpose and Intended Users

**Goal**: To assess the safety alignment of LLMs in scientific tasks and to facilitate responsible development and deployment of LLMs, promoting alignment with safety and ethical standards in scientific research.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Text Classification
- Named Entity Recognition

**Limitations**: SCISAFEEVAL may not fully capture evolving threats or novel hazards beyond curated datasets, limiting its applicability to emerging real-world scenarios.

## 💾 Data

**Source**: Designed to evaluate LLMs across a variety of scientific domains with content sourced from established scientific and hazard databases.

**Size**: 31,840 samples

**Format**: N/A

**Annotation**: Data curated from established scientific and hazard databases.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Chain-of-thought reasoning
- Zero-shot evaluation
- Few-shot evaluation

**Metrics**:
- Harmlessness
- Helpfulness
- Refusal rate

**Calculation**: Scores are based on assessments of safety alignment across multiple queries in scientific domains.

**Interpretation**: Higher scores indicate better safety and compliance with ethical standards.

**Baseline Results**: Competition against existing benchmarks including a reported notable performance improvement in key safety metrics.

**Validation**: The benchmark was critically validated through expert review and automated checks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness
- Ethical Compliance

**Atlas Risks**:
- **Robustness**: Prompt injection attack, Evasion attack
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: SCISAFEEVAL includes both harmful and benign samples, facilitating a balanced assessment of model safety.

**Potential Harm**: ['Potential for misuse in scientific tasks leading to harmful outcomes.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The paper did not discuss specific privacy measures or anonymization procedures.

**Data Licensing**: Not Applicable

**Consent Procedures**: The paper did not mention consent procedures for data collection.

**Compliance With Regulations**: Ensures compliance with AI safety regulations and ethical standards in scientific domains.
