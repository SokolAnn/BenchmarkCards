# CHEW (CHanging Events in Wikipedia)

## 📊 Benchmark Details

**Name**: CHEW (CHanging Events in Wikipedia)

**Overview**: CHEW is a dataset of changing events in Wikipedia, designed to probe language models' timeline understanding of Wikipedia entities and events and assess their capabilities in generating accurate timelines and identifying meaning shifts.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TemporalWiki

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To contribute to research in continual learning, temporal alignment, and LLMs' ability to understand temporal information.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Change Detection
- Timeline Generation

**Limitations**: Our work does not extensively evaluate a wider range of LLMs.

## 💾 Data

**Source**: Wikipedia articles with temporal question-answer pairs.

**Size**: 4,281 examples

**Format**: CSV

**Annotation**: Pairs are derived from manual curation of Wikipedia changes.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metric scores calculated by comparing model outputs with ground truth using SBERT cosine similarity.

**Interpretation**: Higher similarity scores indicate better model performance in understanding timelines.

**Validation**: Models were trained on specific splits of the dataset including Random, No overlap, Time-forward, and Time-reversed.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Transparency

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
