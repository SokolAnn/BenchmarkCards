# MixtureVitae

## 📊 Benchmark Details

**Name**: MixtureVitae

**Overview**: MixtureVitae is an open-access pretraining corpus built to minimize legal risk while providing strong model performance. It combines public-domain and permissively licensed text with low-risk additions, alongside targeted instruction, reasoning and synthetic data.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- C4
- The Pile
- FineWeb-Edu

**Resources**:
- [GitHub Repository](https://github.com/ontocord/mixturevitae)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale, high-performance permissive-first organic-synthetic pretraining dataset built with a transparent, risk-mitigated approach to sourcing.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Combination of public-domain and permissively licensed text, government works, EU TDM-eligible sources, and synthetic data.

**Size**: 211.1 billion tokens

**Format**: N/A

**Annotation**: Data sourced from various publicly available and explicitly licensed sources.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Evaluation based on the LM Evaluation Harness across various downstream tasks.

**Interpretation**: Scores are interpreted based on the accuracy on standard evaluation tasks.

**Validation**: Trained using the open-sci-ref training protocol with systematic control of factors affecting benchmark scores.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**
- **Accuracy**
- **Privacy**

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Dataset includes texts with clear and permissive licenses (e.g., CC-BY, Apache 2.0).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
