# FRACAS (FRench Annotated Corpus of Attribution relations in newS)

## 📊 Benchmark Details

**Name**: FRACAS (FRench Annotated Corpus of Attribution relations in newS)

**Overview**: FRACAS is a human-annotated corpus of 10,965 attribution relations annotated over a set of 1,676 newswire texts in French for quotation extraction and source attribution, aimed at tracking gender imbalance in quotations in the media.

**Data Type**: quotation-source attribution relations

**Domains**:
- Natural Language Processing

**Languages**:
- French

**Resources**:
- [Resource](https://zenodo.org/record/8353229)

## 🎯 Purpose and Intended Users

**Goal**: To provide a freely available corpus for the study of quotation extraction and source attribution for French, enabling further research in Natural Language Processing and social sciences.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Quotation Extraction
- Source Attribution

**Limitations**: The gender representation in the annotated quotes is not balanced, with a significant underrepresentation of female speakers.

## 💾 Data

**Source**: Reuters Corpora 2 (RCV2) collection of newswires published between 1996-1997

**Size**: 1,676 documents

**Format**: N/A

**Annotation**: Manual annotation by 8 annotators following detailed guidelines.

## 🔬 Methodology

**Methods**:
- Manual annotation
- Inter-annotator agreement measurement

**Metrics**:
- Inter-Annotator Agreement (IAA)

**Calculation**: IAAs were computed using the γ-score for the annotated data to assess agreement levels across annotators.

**Interpretation**: High agreement levels in direct quotations suggest reliable labeling, but lower levels in indirect quotes highlight the task's complexity.

**Validation**: The corpus was validated by a gold standard comparison with documents annotated by expert annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: The corpus includes gender attribution for speakers but exhibits a significant imbalance with only 5.4% of quoted speakers being women.

**Potential Harm**: The authors aim to address gender imbalance in news quotations.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data is freely distributed from the Reuters corpus under specific usage guidelines.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
