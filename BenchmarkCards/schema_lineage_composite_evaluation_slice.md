# Schema Lineage Composite Evaluation (SLiCE)

## 📊 Benchmark Details

**Name**: Schema Lineage Composite Evaluation (SLiCE)

**Overview**: The Schema Lineage Composite Evaluation (SLiCE) is a novel metric introduced for automated extraction of schema lineage from multilingual enterprise pipeline scripts. It evaluates the structural correctness and semantic fidelity of the extracted lineage, utilizing a benchmark of 1,700 manually annotated schema lineages from real-world scripts.

**Data Type**: schema lineage annotations

**Domains**:
- Data Governance
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2508.07179)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation framework for schema lineage extraction from complex, multilingual data pipelines.

**Target Audience**:
- Data Engineers
- Data Scientists
- ML Researchers

**Tasks**:
- Schema Lineage Extraction
- Data Transformation Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Manually annotated schema lineages from 50 enterprise pipeline scripts in SQL, Python, and C#.

**Size**: 1,700 schema lineage examples

**Format**: JSON

**Annotation**: Manually annotated by domain experts.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- SLiCE (Schema Lineage Composite Evaluation)

**Calculation**: SLiCE combines multiple evaluations (format correctness, source schema match, source table evaluation, transformation, and aggregation evaluations) into a single composite score.

**Interpretation**: Scores express the accuracy of lineage extraction, where 1.0 indicates perfect extraction.

**Baseline Results**: Models evaluated include various open-source small language models (SLMs) and large language models (LLMs), with results indicating model scaling improvements.

**Validation**: Experimentally validated through extensive evaluation on a curated dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
