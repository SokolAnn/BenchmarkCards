# E DITSET

## 📊 Benchmark Details

**Name**: E DITSET

**Overview**: E DITSET is a dataset specifically designed to evaluate Knowledge Element Overlap (KEO) in knowledge editing tasks. It contains KEO triplets to facilitate comprehensive exploration of KEO in Knowledge Editing (KE) scenarios.

**Data Type**: knowledge triplets

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- zsRE
- PARA REL
- MQ UAKE-T
- MQ UAKE-CF
- COUNTER FACT

**Resources**:
- [Resource](https://anonymous.4open.science/r/SetKE-11B4)

## 🎯 Purpose and Intended Users

**Goal**: To provide a focused evaluation environment for exploring Knowledge Element Overlap (KEO) within knowledge editing tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Knowledge Editing

**Limitations**: N/A

## 💾 Data

**Source**: Knowledge triplets collected from Wikidata.

**Size**: 40,904 instances

**Format**: N/A

**Annotation**: Automatically generated question prompts using GPT-4.

## 🔬 Methodology

**Methods**:
- Bipartite matching
- Knowledge editing techniques

**Metrics**:
- Efficacy Score (ES)
- Generalization Score (GS)
- Locality Score (LS)

**Calculation**: Metrics are calculated based on the model's predictions following edits, comparing them to expected outputs.

**Interpretation**: Higher Efficacy, Generalization, and Locality scores indicate better performance of the editing method.

**Baseline Results**: SetKE outperformed existing methods, achieving state-of-the-art performance in KEO scenarios.

**Validation**: Validated through experiments comparing SetKE's performance to other editing methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
