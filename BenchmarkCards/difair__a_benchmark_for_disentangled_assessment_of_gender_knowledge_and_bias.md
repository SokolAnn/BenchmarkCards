# DIFAIR: A Benchmark for Disentangled Assessment of Gender Knowledge and Bias

## 📊 Benchmark Details

**Name**: DIFAIR: A Benchmark for Disentangled Assessment of Gender Knowledge and Bias

**Overview**: DIFAIR is a manually curated dataset aimed at assessing gender bias in language models by measuring their performance on gender-specific and gender-neutral instances while retaining useful gender knowledge. It introduces a gender invariance score that quantifies biased behavior and preservation of gender knowledge.

**Data Type**: gender-specific and gender-neutral sentences

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/mzakizadeh/difair_public)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating gender bias in language models and assess the trade-off between fairness and factual gender knowledge.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Bias Assessment
- Knowledge Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: English Wikipedia and Reddit

**Size**: 2,506 instances

**Format**: N/A

**Annotation**: Manually annotated by trained annotators based on criteria for gender-specific and gender-neutral sentences.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Performance metrics based on gender invariance score

**Metrics**:
- Gender Invariance Score (GIS)

**Calculation**: The gender invariance score is calculated as the harmonic mean of gender-specific score (GSS) and gender-neutral score (GNS).

**Interpretation**: Scores range from 0 to 1, with higher scores indicating better performance in balancing gender fairness and knowledge retention.

**Validation**: The dataset was validated with inter-annotator agreement of 86.6%.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution-ShareAlike 3.0 license and the GNU Free Documentation License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
