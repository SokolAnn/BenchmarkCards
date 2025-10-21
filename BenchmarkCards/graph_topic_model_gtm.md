# Graph Topic Model (GTM)

## 📊 Benchmark Details

**Name**: Graph Topic Model (GTM)

**Overview**: GTM is a neural topic model that incorporates document relationship graph to enrich document and word representations.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/AKSW/Palmetto)

## 🎯 Purpose and Intended Users

**Goal**: To introduce a GNN-based neural topic model that enhances document representations using document relationship graphs.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Topic Modeling

**Limitations**: N/A

## 💾 Data

**Source**: Datasets include 20Newsgroups, Grolier, and NYTimes.

**Size**: 11,259 documents (20Newsgroups); 29,762 documents (Grolier); 99,992 documents (NYTimes)

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Topic coherence measures (C_A, C_P, NPMI)

**Calculation**: Metrics calculated based on topic coherence measures related to word co-occurrence statistics.

**Interpretation**: Higher topic coherence scores indicate better performance in topic modeling.

**Baseline Results**: GTM outperformed all baseline models (LDA, NVDM, ProdLDA, GraphBTM, ATM, W-LDA) across datasets.

**Validation**: Extensive experiments conducted on three datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
