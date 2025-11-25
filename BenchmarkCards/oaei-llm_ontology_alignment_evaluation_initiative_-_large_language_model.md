# OAEI-LLM (Ontology Alignment Evaluation Initiative - Large Language Model)

## 📊 Benchmark Details

**Name**: OAEI-LLM (Ontology Alignment Evaluation Initiative - Large Language Model)

**Overview**: The OAEI-LLM dataset is an extended version of the Ontology Alignment Evaluation Initiative (OAEI) datasets that evaluate LLM-specific hallucinations in Ontology Matching (OM) tasks. It measures the degree of hallucination by LLMs in OM tasks by comparing original human-labelled results with LLM-generated results and categorizes different types of hallucinations.

**Data Type**: mapping pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://oaei.ontologymatching.org/doc/oaei-deontology.2.html)

## 🎯 Purpose and Intended Users

**Goal**: To measure the degree of hallucination by large language models in ontology matching tasks through an extended dataset.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Ontology Matching

**Limitations**: Demonstrates only one-to-one equivalent mappings; more complex scenarios may cause additional types of LLM hallucinations.

## 💾 Data

**Source**: Extended Ontology Alignment Evaluation Initiative datasets

**Size**: Varied based on usage

**Format**: Extended EDOAL mapping schema

**Annotation**: Annotations based on comparing human-labelled results with LLM-generated results.

## 🔬 Methodology

**Methods**:
- LLM evaluation for mapping assessment

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated by comparing generated mappings against the original OAEI reference.

**Interpretation**: High precision indicates fewer false mappings while high recall indicates fewer missing mappings.

**Validation**: Validation occurs through comparison with the OAEI Reference.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
