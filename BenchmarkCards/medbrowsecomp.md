# MedBrowseComp

## 📊 Benchmark Details

**Name**: MedBrowseComp

**Overview**: MedBrowseComp is the first benchmark that systematically tests an agent’s ability to reliably retrieve and synthesize multi-hop medical facts from live, domain-specific knowledge bases, featuring 1,000+ human-curated questions that mirror clinical scenarios.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- MedQA
- WorldMedQA

**Resources**:
- [Resource](https://huggingface.co/datasets/AIM-Harvard/MedBrowseComp)
- [GitHub Repository](https://github.com/shan23chen/MedBrowseComp)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of AI agents performing complex information retrieval tasks within the medical domain via web browsing.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Model Developers

**Tasks**:
- Information Retrieval
- Medical Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The dataset was curated from HemOnc.org, one of the largest structured wiki information resources maintained by oncologists.

**Size**: 1,000+ questions

**Format**: N/A

**Annotation**: Questions were human-curated by medical professionals.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Evaluation based on agent's ability to retrieve correct answers from web browsing.

**Interpretation**: Accuracy reflects the agent's performance in retrieving medical information.

**Baseline Results**: Initial evaluations reveal that models achieve less than 50% accuracy overall.

**Validation**: Results validated using both automated judges and manual checks for agreement.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data is from publicly available sources with no protected health information exposed.

**Data Licensing**: All datasets are open access and comply with the copyright and terms of service under Apache 2.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
