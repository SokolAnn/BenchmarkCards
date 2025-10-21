# RELATE: Relation Extraction in Biomedical Abstracts with LLMs and Ontology Constraints

## 📊 Benchmark Details

**Name**: RELATE: Relation Extraction in Biomedical Abstracts with LLMs and Ontology Constraints

**Overview**: RELATE is a three-stage pipeline for mapping LLM-extracted biomedical relations to standardized ontology predicates using ChemProt and the Biolink Model. It aims to enhance relation extraction by transforming free-text outputs into structured, ontology-constrained representations.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- ChemProt

**Resources**:
- [Resource](https://huggingface.co/datasets/bigbio/chemprot)
- [Resource](https://heal.nih.gov/)
- [GitHub Repository](https://github.com/RENCI-NER/pred-mapping/tree/multi-ontology)

## 🎯 Purpose and Intended Users

**Goal**: To provide a scalable, ontology-constrained framework for converting unstructured biomedical literature into standardized knowledge graphs.

**Target Audience**:
- Biomedical Researchers
- Data Scientists
- ML Researchers

**Tasks**:
- Relation Extraction

**Limitations**: N/A

## 💾 Data

**Source**: ChemProt dataset and PubMed abstracts from the HEAL Project.

**Size**: 2,400 abstracts

**Format**: text

**Annotation**: Data is annotated using existing biomedical relation schemas.

## 🔬 Methodology

**Methods**:
- Ontology preprocessing
- Similarity-based retrieval
- LLM-based contextual refinement

**Metrics**:
- Accuracy
- Exact Match
- Accuracy@10

**Calculation**: Exact match accuracy is calculated based on the top choice predicate after the LLM-based refinement.

**Interpretation**: An accuracy of 52% exact match indicates the percentage of correct mappings from LLM outputs to the established ontology predicates.

**Baseline Results**: Exact match accuracy of RELATE achieves 52% on the ChemProt benchmark.

**Validation**: The validation is conducted through comparison with the ChemProt benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: This research analyzes public biomedical publication texts and does not require IRB approval.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
