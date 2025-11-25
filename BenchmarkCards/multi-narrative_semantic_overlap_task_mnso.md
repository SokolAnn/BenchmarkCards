# Multi-Narrative Semantic Overlap Task (MNSO)

## 📊 Benchmark Details

**Name**: Multi-Narrative Semantic Overlap Task (MNSO)

**Overview**: The Multi-Narrative Semantic Overlap (MNSO) task involves generating semantic overlaps of multiple narratives and includes the creation of a benchmark dataset. The paper outlines the problem of extracting overlapping information from narratives and introduces a new evaluation metric, SEM-F1.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To introduce a new NLP task called Multi-Narrative Semantic Overlap and create a corresponding benchmark dataset.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Crawled from AllSides.com, with additional ground-truth annotations from human volunteers.

**Size**: 2,925 narrative pairs

**Format**: N/A

**Annotation**: Manual annotations by human annotators to create ground-truth labels.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- SEM-F1

**Calculation**: F1 scores computed by the harmonic mean of precision and recall values derived from cosine similarity between sentences.

**Interpretation**: Higher SEM-F1 scores indicate better alignment with human judgement on semantic overlaps.

**Baseline Results**: ROUGE metrics were initially evaluated but found unsuitable for this task.

**Validation**: N/A

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
