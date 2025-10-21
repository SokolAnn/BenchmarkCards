# Intertextual Parallel Detection in Biblical Hebrew: A Transformer-Based Benchmark

## 📊 Benchmark Details

**Name**: Intertextual Parallel Detection in Biblical Hebrew: A Transformer-Based Benchmark

**Overview**: This study provides the first comprehensive benchmark of transformer-based models for detecting parallels in biblical texts, evaluating their effectiveness in creating embeddings for Hebrew verses.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Hebrew

**Resources**:
- [GitHub Repository](https://github.com/dmsmiley/detect-bh)

## 🎯 Purpose and Intended Users

**Goal**: Assess the effectiveness of transformer-based language models in identifying parallel passages within Hebrew texts.

**Target Audience**:
- Biblical Scholars
- NLP Researchers

**Tasks**:
- Text Similarity

**Limitations**: Focuses exclusively on narrative texts and known parallels between Samuel/Kings and Chronicles; may not generalize across all biblical literature genres.

## 💾 Data

**Source**: Biblia Hebraica Stuttgartensia Amstelodamensis corpus, compiled by the Eep Talstra Centre for Bible and Computer at Vrije Universiteit Amsterdam.

**Size**: 558 verses

**Format**: Plain text

**Annotation**: Manual comparison of parallel passages.

## 🔬 Methodology

**Methods**:
- Cosine Similarity
- Wasserstein Distance
- Classification Metrics

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Cosine similarity computed for parallel and non-parallel texts, with statistical tests confirming significance of results.

**Interpretation**: Scores indicate how well models distinguish between parallel and non-parallel passages.

**Baseline Results**: E5 achieved a F1 Score of 0.88, while AlephBERT achieved 0.87.

**Validation**: Performance evaluated through statistical significance tests and comparison of cosine similarities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
