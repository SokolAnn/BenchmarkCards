# Annotated Literary Dialect Corpus

## 📊 Benchmark Details

**Name**: Annotated Literary Dialect Corpus

**Overview**: We present a dataset of 19th century American literary orthovariant tokens with a novel layer of human-annotated dialect group tags designed to serve as the basis for computational experiments exploring literarily meaningful orthographic variation.

**Data Type**: orthovariant token pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/comp-int-hum/orthography-embedding-clustering)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the multidimensional signaling pathways of dialect effects in literary orthographic variation using an annotated corpus.

**Target Audience**:
- ML Researchers
- Linguists
- Humanities Scholars

**Tasks**:
- Dialect Analysis
- Language Modeling

**Limitations**: The primary limitation of this study emerges from the data which is restricted to 19th century American authors, limiting the depth of analysis due to the granularity of the tags.

## 💾 Data

**Source**: 19th century American literature subset of the Project Gutenberg corpus

**Size**: 4,032 tokens

**Format**: N/A - Not specified

**Annotation**: Human-annotated dialect group tags

## 🔬 Methodology

**Methods**:
- Token-level contextual modeling
- Character-level contextual modeling

**Metrics**:
- Purity
- Overall accuracy
- SO accuracy
- Cluster semantic coherency
- Mphone similarity

**Calculation**: Purity is calculated over the clustering of the full relative token set to gain insight into each model’s ability to distinguish between synthetic and observed variants.

**Interpretation**: Models exhibit varying abilities to capture dialect effects, with character-level models generally performing better in distinguishing orthographic variations.

**Baseline Results**: N/A

**Validation**: Initial experiments conducted to evaluate the performance of various models on the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis included varying demographic factors based on the dialect tags assigned to tokens.

**Potential Harm**: The dataset may reinforce stereotypes by explicitly tagging dialect forms, which must be handled with care.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
