# Unified Entrez Gene Identifier Dataset and Benchmarks (UniEntrezDB)

## 📊 Benchmark Details

**Name**: Unified Entrez Gene Identifier Dataset and Benchmarks (UniEntrezDB)

**Overview**: UniEntrezDB is the first systematic effort to unify large-scale public Gene Ontology Annotations (GOA) from various databases using unique gene identifiers. It includes a pre-training dataset and four downstream tasks designed to comprehensively evaluate gene embedding performance from gene, protein, and cell levels.

**Data Type**: gene ontology annotations with unique gene identifiers

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To address the challenges of integrating large-scale domain knowledge into gene-related research and enhance the reliability and applicability of LLMs in gene research and other professional settings.

**Target Audience**:
- ML Researchers
- Biologists
- Data Scientists

**Tasks**:
- Gene Interaction Prediction
- Protein-Protein Interaction
- Pathway Co-present Prediction
- Single-Cell Type Annotation

**Limitations**: N/A

## 💾 Data

**Source**: UniEntrezGOA consolidates annotations from multiple public databases including RefSeq, Ensembl, and UniProtKB.

**Size**: Over 1,000 species with manually annotated GOA

**Format**: Gene Annotation File (GAF)

**Annotation**: Annotations are gathered from 21 databases and are manually reviewed or automatically generated based on gene identifiers.

## 🔬 Methodology

**Methods**:
- 5-fold cross-validation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is reported as the average result of 5-fold cross-validation across various benchmark tasks.

**Interpretation**: Higher accuracy indicates better gene embedding performance and effectiveness in capturing biological relationships.

**Baseline Results**: Performance of various gene embedding models such as Gene2Vec and OntoProtein are explored, with significant improvements noted when combining functional and expression data.

**Validation**: Validation was performed through structured training and testing datasets with non-overlapping gene information.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
