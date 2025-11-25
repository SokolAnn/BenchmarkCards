# CONFLICTS

## 📊 Benchmark Details

**Name**: CONFLICTS

**Overview**: CONFLICTS is a high-quality benchmark with expert annotations of conflict types in a realistic RAG setting, enabling tracking progress on how models address a wide range of knowledge conflicts.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ConflictingQA
- FreshQA
- SituatedQA Temp
- SituatedQA Geo

**Resources**:
- [GitHub Repository](https://github.com/google-research-datasets/rag_conflicts)

## 🎯 Purpose and Intended Users

**Goal**: To foster research on knowledge conflict resolution in Retrieval Augmented Generation (RAG) and provide a dataset for evaluating model performance in handling various types of knowledge conflicts.

**Target Audience**:
- ML Researchers
- Academics
- Industry Practitioners

**Tasks**:
- Conflict Type Prediction
- Generating Appropriate Responses

**Limitations**: N/A

## 💾 Data

**Source**: Curated from multiple datasets including ConflictingQA, FreshQA, SituatedQA Temp, and more, encompassing a wide range of knowledge conflict scenarios.

**Size**: 458 examples

**Format**: JSON

**Annotation**: Annotated by expert annotators following a three-stage review process for reliability.

## 🔬 Methodology

**Methods**:
- Conflict type prediction
- Response generation

**Metrics**:
- Factual Grounding
- Answer Recall
- Expected Behavior Adherence

**Calculation**: Metrics calculated based on model outputs compared to expert annotations and benchmarks.

**Interpretation**: Model outputs are evaluated for factual correctness, adherence to expected response behaviors based on conflict types, and overall quality.

**Baseline Results**: Performance metrics vary per model evaluated on CONFLICTS, with the best models achieving over 60% adherence to expected behaviors.

**Validation**: Conducted via a multi-faceted evaluation approach leveraging both automated and human assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Decision bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
