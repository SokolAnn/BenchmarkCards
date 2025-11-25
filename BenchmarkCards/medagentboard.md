# MedAgentBoard

## 📊 Benchmark Details

**Name**: MedAgentBoard

**Overview**: MedAgentBoard serves as a comprehensive benchmark for the evaluation of multi-agent collaboration, single LLM and conventional methods across diverse medical tasks, addressing gaps in generalizability and completeness.

**Data Type**: text, medical images, structured EHR data

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MedHELM
- MedAgentsBench
- MAST
- Multi-agent Debate

**Resources**:
- [Resource](https://medagentboard.netlify.app/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation of multi-agent collaboration, single large language models, and conventional approaches across various medical tasks.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- AI Developers

**Tasks**:
- Medical (Visual) Question Answering
- Lay Summary Generation
- EHR Predictive Modeling
- Clinical Workflow Automation

**Limitations**: The study highlights that multi-agent collaboration does not universally outperform advanced single LLMs or specialized conventional methods.

## 💾 Data

**Source**: Publicly available datasets for medical tasks including MedQA, PubMedQA, PathVQA, VQA-RAD, Cochrane, eLife, PLOS, Med-EASi, and TJH.

**Size**: N/A

**Format**: Varies by dataset (e.g., CSV, JSON)

**Annotation**: Data annotation methods vary depending on the dataset (e.g., expert-annotated summaries, structured clinical data).

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Comparative analysis

**Metrics**:
- Accuracy
- ROUGE-L
- BLEU Score
- AUROC

**Calculation**: Metrics calculated according to standard evaluation protocols for the respective tasks.

**Interpretation**: The results can be interpreted by comparing the performance of multi-agent collaboration and LLMs against strong conventional baselines.

**Baseline Results**: Comprehensive results across all evaluated tasks, showcasing the strengths and weaknesses of each method.

**Validation**: Extensive experiments designed to ensure the robustness and validity of the benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All datasets used are publicly available or accessible upon request and were employed under their respective licenses.

**Data Licensing**: Datasets are used following their respective licenses.

**Consent Procedures**: None applicable as no new patient data was collected.

**Compliance With Regulations**: Not Applicable
