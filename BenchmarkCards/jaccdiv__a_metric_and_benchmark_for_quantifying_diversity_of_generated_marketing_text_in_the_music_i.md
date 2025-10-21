# JaccDiv: A Metric and Benchmark for Quantifying Diversity of Generated Marketing Text in the Music Industry

## 📊 Benchmark Details

**Name**: JaccDiv: A Metric and Benchmark for Quantifying Diversity of Generated Marketing Text in the Music Industry

**Overview**: This research introduces JaccDiv, a metric to evaluate the diversity of generated marketing texts and establishes a benchmark for assessing the quality and diversity of LLM-based text generation in the music industry.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Marketing

**Languages**:
- English
- German

**Resources**:
- [Resource](https://arxiv.org/abs/2504.20849)

## 🎯 Purpose and Intended Users

**Goal**: To provide a method for quantifying the diversity of generated marketing texts using language models for improving content generation in the music industry.

**Target Audience**:
- ML Researchers
- Content Generation Practitioners

**Tasks**:
- Text Generation
- Diversity Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Industrial dataset acquired from a platform connecting musicians and event organizers.

**Size**: 440 samples

**Format**: N/A

**Annotation**: Manual curation and quality control with human ratings for quality and uniqueness.

## 🔬 Methodology

**Methods**:
- LLM-based metrics
- Jaccard similarity coefficient
- Human evaluation

**Metrics**:
- Quality: Engagingness, Fluency, Naturalness, Informativeness
- Diversity: Jaccard Similarity based metric

**Calculation**: Jaccard similarity score calculated by averaging pairwise similarities of n-grams between generated texts.

**Interpretation**: Scores closer to 0 indicate higher diversity in generated texts.

**Validation**: Manual rating by human annotators for comparing generated texts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Quality
- Diversity

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
