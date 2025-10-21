# ICE-ID (Identity Resolution Benchmark)

## 📊 Benchmark Details

**Name**: ICE-ID (Identity Resolution Benchmark)

**Overview**: ICE-ID is a novel benchmark dataset for historical identity resolution, comprising 220 years (1703–1920) of Icelandic census records. It captures name variations, demographic changes, and genealogical links, focusing on long-term person-entity matching in a real-world population.

**Data Type**: tabular

**Domains**:
- Natural Language Processing
- History

**Languages**:
- Icelandic

**Resources**:
- [Resource](https://huggingface.co/datasets/goldpotatoes/ice-id)

## 🎯 Purpose and Intended Users

**Goal**: To enable reproducible benchmarking of identity resolution approaches in longitudinal settings and stimulate cross-disciplinary research in data linkage and historical analytics.

**Target Audience**:
- ML Researchers
- Historians
- Data Scientists
- Social Scientists

**Tasks**:
- Identity Resolution
- Entity Matching

**Limitations**: Snapshot waves only; kinship signal sparsity; label noise in early records; modalities and unstructured data are not included.

## 💾 Data

**Source**: Digitized Icelandic census records from varying years combined with auxiliary data.

**Size**: 984,028 raw rows with 200,000 high-confidence cluster labels

**Format**: CSV

**Annotation**: Expert-curated cluster labels and normalization of names.

## 🔬 Methodology

**Methods**:
- Machine Learning ensembles
- Non-Axiomatic Reasoning System (NARS)
- Deterministic Rules

**Metrics**:
- Precision
- Recall
- F1 Score
- Accuracy
- AUC
- Adjusted Rand Index (ARI)

**Calculation**: Metrics calculated using pairwise comparisons and clustering quality assessments based on thresholds.

**Interpretation**: Scores are interpreted with respect to their roles in defining matching efficiency and clustering coherence.

**Baseline Results**: F1 Score of 0.9613 on combined tasks with ML ensemble.

**Validation**: Evaluated through temporal splits mirroring real archival workflows.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Safety

**Atlas Risks**:
- **Privacy**: Personal information in data

**Demographic Analysis**: The dataset includes population demographic shifts over the analyzed period.

**Potential Harm**: ['Potential privacy breaches from individual linkage.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: There is a risk of exposing sensitive personal information through linked genealogical data.

**Data Licensing**: Open-access license for shared data and artifacts.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
