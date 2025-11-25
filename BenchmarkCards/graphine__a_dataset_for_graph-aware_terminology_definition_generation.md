# Graphine: A Dataset for Graph-aware Terminology Definition Generation

## 📊 Benchmark Details

**Name**: Graphine: A Dataset for Graph-aware Terminology Definition Generation

**Overview**: Graphine encompasses 2,010,648 terminology definition pairs organized in 227 directed acyclic graphs (DAGs), which makes it a unique resource for exploring graph-aware text generation.

**Data Type**: terminology definition pairs

**Domains**:
- Natural Language Processing
- Biomedical

**Languages**:
- English

**Resources**:
- [Resource](https://zenodo.org/record/5320310#.YSxHgI77Q2w)
- [GitHub Repository](https://github.com/zequnl/Graphex)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to study definition generation in the biomedical domain.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Generation
- Definition Generation

**Limitations**: N/A

## 💾 Data

**Source**: Collected from three major biomedical ontology databases: Open Biological and Biomedical Ontology Foundry (OBO), BioPortal, and EMBL-EBI Ontology Lookup Service (OLS).

**Size**: 2,010,648 pairs

**Format**: N/A

**Annotation**: Curation by domain experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU Score
- METEOR
- NIST

**Calculation**: Metrics are calculated comparing generated definitions against true definitions using n-gram overlaps.

**Interpretation**: Higher scores indicate better performance in generating definitions.

**Validation**: Validation through both automatic and human evaluations on generated definitions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
