# GUM-SAGE (GUM-based Summary Aligned Graded Entities)

## 📊 Benchmark Details

**Name**: GUM-SAGE (GUM-based Summary Aligned Graded Entities)

**Overview**: GUM-SAGE is a novel dataset for graded entity salience prediction, combining human summaries and aligning them to document entities to derive salience scores. It spans multiple genres and provides graded salience scores for named and non-named entities.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/jl908069/gum_sum_salience1)

## 🎯 Purpose and Intended Users

**Goal**: To improve graded salient entity extraction and support further research on entity salience prediction and summarization.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Entity Salience Prediction
- Summarization

**Limitations**: The dataset is limited to English, and relies on multiple high-quality summaries which can introduce scalability challenges.

## 💾 Data

**Source**: GUM corpus (Zeldes, 2017), enriched with human and model-generated summaries.

**Size**: 213 documents, over 200K tokens

**Format**: N/A

**Annotation**: Data was annotated using crowdsourcing methods for summaries and alignment with expert-written quality control.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Spearman correlation

**Calculation**: F1 Score is calculated based on the model's ability to classify entities into graded salience scores (1-5), and Spearman's ρ measures the correlation between predicted and human-aggregated scores.

**Interpretation**: Higher F1 scores indicate better agreement with human judgments on entity salience. Spearman's ρ close to 1 indicates strong correlation.

**Baseline Results**: Position baseline model indicated lower performance in salience ranking with Spearman's ρ of 0.153.

**Validation**: Validation conducted using separate test and development sets from the GUM corpus.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset spans multiple genres but is limited to English.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All summaries were collected with explicit consent.

**Data Licensing**: Released under a CC0 license.

**Consent Procedures**: Annotators consented to data sharing for research purposes.

**Compliance With Regulations**: Not Applicable
