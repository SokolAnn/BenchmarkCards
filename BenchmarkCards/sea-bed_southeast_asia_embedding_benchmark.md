# SEA-BED (Southeast Asia Embedding Benchmark)

## 📊 Benchmark Details

**Name**: SEA-BED (Southeast Asia Embedding Benchmark)

**Overview**: SEA-BED is the first large-scale SEA embedding benchmark with 169 datasets across 9 tasks and 10 languages, focusing on the evaluation of sentence embeddings for Southeast Asian languages.

**Data Type**: sentence embeddings

**Domains**:
- Natural Language Processing

**Languages**:
- Indonesian
- Thai
- Vietnamese
- Burmese
- Filipino
- Tamil
- Khmer
- Malay
- Lao
- Tetum

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve sentence embedding models' performance across Southeast Asian languages, addressing the challenges specific to low-resource languages.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Bitext Mining
- Pair Classification
- Toxic Language Detection
- Multi-label Classification
- Semantic Textual Similarity (STS)
- Instruction Retrieval
- Question Answering
- Retrieval
- Clustering

**Limitations**: N/A

## 💾 Data

**Source**: Various datasets curated specifically for SEA languages, primarily created by native speakers.

**Size**: 169 datasets

**Format**: Various formats including, but not limited to, JSON and CSV.

**Annotation**: Annotated primarily by native speakers or through expert curation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Mean Average Precision (MAP)
- Spearman correlation

**Calculation**: Metrics are calculated comparably across different tasks, using standard evaluation strategies.

**Interpretation**: Higher scores indicate better performance in the given tasks.

**Baseline Results**: Results show substantial shifts in model rankings when evaluated against previous benchmark settings, particularly MMTEB.

**Validation**: Through testing 17 embedding models across 6 studies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Accuracy**: Unrepresentative data
- **Privacy**

**Demographic Analysis**: An explicit analysis of linguistic groups within Southeast Asia to ensure equitable representation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Datasets are curated to avoid sensitive data and ensure participant anonymity.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
