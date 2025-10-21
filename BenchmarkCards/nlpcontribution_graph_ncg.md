# NLPCONTRIBUTION GRAPH (NCG)

## 📊 Benchmark Details

**Name**: NLPCONTRIBUTION GRAPH (NCG)

**Overview**: NLPCONTRIBUTION GRAPH is a novel scheme to annotate research contributions from NLP articles and integrate them in a knowledge graph, facilitating fine-grained semantic knowledge capture over precise information targets modeled as nodes and links.

**Data Type**: sentence, phrase, and triple annotations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/ncg-task/trial-data)
- [Resource](https://doi.org/10.2478/jdis-2021-0023)

## 🎯 Purpose and Intended Users

**Goal**: To create a structured knowledge graph of contributions in Natural Language Processing scholarly articles.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Knowledge Graph Construction

**Limitations**: NLPCONTRIBUTION GRAPH has limited scope for structuring scholarly contributions compared to STEM scholarly knowledge at large.

## 💾 Data

**Source**: 50 NLP scholarly articles randomly selected across five different NLP subfields.

**Size**: 900 contribution sentences, 4,702 phrases, 2,980 triples

**Format**: JSON

**Annotation**: Manual annotation by a single annotator.

## 🔬 Methodology

**Methods**:
- Manual annotation
- Evaluation of intra-annotation agreement

**Metrics**:
- F1 Score

**Calculation**: Intra-annotation agreement metrics calculated between pilot and adjudicated annotations.

**Interpretation**: F1-scores of 67.92% for sentences, 41.82% for phrases, and 22.31% for triples indicating varying degrees of annotation agreement.

**Baseline Results**: N/A

**Validation**: Data validated through pilot and adjudication stages with specific annotation guidelines.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
