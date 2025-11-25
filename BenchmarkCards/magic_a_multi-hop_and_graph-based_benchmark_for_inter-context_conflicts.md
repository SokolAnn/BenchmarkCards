# MAGIC (A Multi-Hop and Graph-Based Benchmark for Inter-Context Conflicts)

## 📊 Benchmark Details

**Name**: MAGIC (A Multi-Hop and Graph-Based Benchmark for Inter-Context Conflicts)

**Overview**: MAGIC is a benchmark designed to evaluate inter-context knowledge conflict detection, leveraging knowledge graphs to generate complex conflict patterns, including multi-hop conflicts. It provides insights into the performance of large language models (LLMs) in identifying contradictions across multiple contexts.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ECON
- WikiContradict

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating the ability of LLMs to detect knowledge conflicts across various contexts.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Knowledge Conflict Detection

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from Wikidata5M knowledge graphs.

**Size**: 1,080 examples

**Format**: N/A

**Annotation**: Includes human-in-the-loop quality control for conflict generation and selection.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Identification Score (ID Score)
- Localization Score (LOC Score)

**Calculation**: ID Score is calculated based on the model's ability to detect conflicts, while LOC Score evaluates performance on pinpointing exact locations of conflicts.

**Interpretation**: Higher ID Scores indicate better detection performance, while higher LOC Scores represent better localization abilities.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
