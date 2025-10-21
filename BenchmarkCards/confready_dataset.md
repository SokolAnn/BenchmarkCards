# ConfReady Dataset

## 📊 Benchmark Details

**Name**: ConfReady Dataset

**Overview**: The ConfReady dataset contains a curated collection of 1975 checklist responses from ACL conference papers, enabling analysis of the quality of checklist submissions and benchmarking of retrieval-augmented generation (RAG) and language model systems.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/gtfintechlab/ConfReady)
- [Resource](https://confready-docs.vercel.app/docs/walkthrough)

## 🎯 Purpose and Intended Users

**Goal**: To assist authors in reflecting on their work and improving the quality of checklist responses for conference submissions.

**Target Audience**:
- Researchers
- Authors
- Conference Organizers

**Tasks**:
- Checklist Compliance Evaluation
- Response Generation

**Limitations**: The dataset may contain inconsistencies from human responses such as identical answers or inaccuracies.

## 💾 Data

**Source**: Curated from 1975 ACL conference papers with responses to the ARR Responsible NLP Research checklist.

**Size**: 1,975 examples

**Format**: Excel

**Annotation**: Responses were manually reviewed and verified for quality and completeness.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is measured against human-provided checklist responses in comparative evaluations.

**Interpretation**: Higher accuracy indicates better alignment with human responses, suggesting a more reliable checklist assistance system.

**Baseline Results**: CRAG framework achieved an average accuracy of over 81% on ACL papers.

**Validation**: The dataset was validated for completeness and correctness through manual review.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: The dataset captures a range of demographics based on various conferences represented.

**Potential Harm**: Potential for checklist response inaccuracies impacting research integrity.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: AGPL-3.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
