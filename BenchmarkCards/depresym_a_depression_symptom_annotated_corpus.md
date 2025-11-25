# DepreSym (A Depression Symptom Annotated Corpus)

## 📊 Benchmark Details

**Name**: DepreSym (A Depression Symptom Annotated Corpus)

**Overview**: DepreSym is a dataset consisting of 21,580 sentences annotated for their relevance to the 21 symptoms of the Beck Depression Inventory-II (BDI-II), aimed at fostering research on new depression screening models that rely on symptom markers at the sentence level.

**Data Type**: annotated sentences

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- PsySym
- eRisk2019

**Resources**:
- [Resource](https://erisk.irlab.org/depresym_dataset.html)

## 🎯 Purpose and Intended Users

**Goal**: To encourage the development of models that rely on symptom-level screening of depression.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Domain Experts

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Sentences extracted from a pool of user posts on Reddit, selected through a top-k pooling approach from participant rankings.

**Size**: 21,580 sentences

**Format**: text

**Annotation**: Annotated by three expert assessors, including an expert psychologist.

## 🔬 Methodology

**Methods**:
- Human evaluation
- LLM-based evaluation

**Metrics**:
- Cohen’s Kappa
- Krippendorff’s Alpha

**Calculation**: Inter-rater agreement calculated using Cohen’s Kappa and Krippendorff’s Alpha for assessing the agreement between human annotators and LLMs.

**Interpretation**: Higher Kappa values indicate better agreement among annotators; Cohen's Kappa below 0.67 suggests unreliable annotations.

**Baseline Results**: N/A

**Validation**: Inter-rater agreement analysis and comparison between human and LLM annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Misrepresentation of mental health states.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Annotated sentences came from publicly available user posts on Reddit; users provided consent for their data to be used.

**Data Licensing**: Creative Commons License Attribution 4.0 International (CC BY 4.0).

**Consent Procedures**: Users consented to access their publication histories on Reddit.

**Compliance With Regulations**: Not Applicable
