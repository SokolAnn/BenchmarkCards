# GeoBenchX: Benchmarking LLMs for Multistep Geospatial Tasks

## 📊 Benchmark Details

**Name**: GeoBenchX: Benchmarking LLMs for Multistep Geospatial Tasks

**Overview**: This paper establishes a benchmark for evaluating large language models (LLMs) on multi-step geospatial tasks relevant to commercial GIS practitioners, assessing various models with a tool-calling agent equipped with geospatial functions.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Geospatial Analysis

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Solirinai/GeoBenchX)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of LLMs on multi-step geospatial tasks using a standardized benchmark set.

**Target Audience**:
- GIS Practitioners
- ML Researchers
- Industry Practitioners

**Tasks**:
- Geospatial Analysis
- Mapping
- Data Visualization

**Limitations**: The benchmark set size is moderate.

## 💾 Data

**Source**: Created from panel data and geometrical data with labeled tasks derived from industry-specific needs.

**Size**: 200+ tasks

**Format**: CSV, GeoJSON, Shapefile

**Annotation**: Manually annotated with ground-truth reference solutions

## 🔬 Methodology

**Methods**:
- LLM-as-Judge Evaluation
- Matching-based Evaluation

**Metrics**:
- Accuracy
- Token Usage

**Calculation**: Evaluation based on matching candidate solutions to reference solutions using LLM judges.

**Interpretation**: The performance is judged based on semantic equivalence and efficiency in terms of token usage.

**Baseline Results**: Results indicate differences in performance across various LLMs with Sonnet 3.5 and GPT-4o achieving the best overall performance.

**Validation**: Tuning the evaluator using a set of 44 tasks sampled with stratification.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
