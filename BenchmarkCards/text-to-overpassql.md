# Text-to-OverpassQL

## 📊 Benchmark Details

**Name**: Text-to-OverpassQL

**Overview**: OverpassNL is a dataset of 8,352 queries with corresponding natural language inputs designed to facilitate a natural language interface for querying geodata from OpenStreetMap (OSM) using the Overpass Query Language (OverpassQL).

**Data Type**: natural language input and Overpass queries

**Domains**:
- Natural Language Processing
- Geospatial Data Analysis

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/raphael-sch/OverpassNL)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for the Text-to-OverpassQL task and establish a systematic evaluation protocol for natural language interfaces to query OpenStreetMap data.

**Target Audience**:
- ML Researchers
- Geospatial Analysts
- Developers of Natural Language Processing Systems

**Tasks**:
- Semantic Parsing

**Limitations**: N/A

## 💾 Data

**Source**: Natural language inputs collected from users on Overpass Turbo and corresponding OverpassQL queries authored by the OpenStreetMap community.

**Size**: 8,352 instances

**Format**: JSON

**Annotation**: Natural language descriptions were written by trained annotators after providing tutorials on OverpassQL.

## 🔬 Methodology

**Methods**:
- Baseline evaluation using finetuning of sequence-to-sequence models and large language models.
- In-context learning strategies for black-box LLMs.

**Metrics**:
- Overpass Query Similarity (OQS)
- Execution Accuracy (EX)
- Soft Execution Accuracy (EX SOFT)

**Calculation**: OQS includes character F-score (chrF), key-value similarity (KVS), and tree similarity (TreeS) computed from the generated and reference queries.

**Interpretation**: Values close to 1 for execution metrics indicate high accuracy of the generated queries compared to the reference.

**Baseline Results**: The best model for our task is ByT5-base, achieving notable execution accuracy compared to other models.

**Validation**: The quantitative performance is validated by executing queries against the OpenStreetMap database and comparing the outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
