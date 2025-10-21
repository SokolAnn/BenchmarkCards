# TAXI (Taxonomic Inference)

## 📊 Benchmark Details

**Name**: TAXI (Taxonomic Inference)

**Overview**: TAXI is a new benchmark dataset specifically created to evaluate consistency in categorical knowledge edits in language models. It contains 11,120 multiple-choice queries for 976 edits spanning 41 categories, 164 subjects, and 183 properties.

**Data Type**: multiple-choice queries

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- COUNTER FACT
- RIPPLEEDITS
- MQuAKE

**Resources**:
- [GitHub Repository](https://github.com/derekpowell/taxi)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate knowledge editors' ability to consistently and coherently edit large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Knowledge Editing Evaluation

**Limitations**: The categories, subjects, and properties included in TAXI were manually selected and may not be fully representative of broader natural language categories.

## 💾 Data

**Source**: Manually created dataset of categorical edits.

**Size**: 11,120 queries

**Format**: JSON

**Annotation**: Manually created with expert verification.

## 🔬 Methodology

**Methods**:
- Knowledge Editing with model editing techniques

**Metrics**:
- Edit Success
- Property Success
- Consistency
- Invariance

**Calculation**: Accuracy scores computed over a set of query prompts with expected continuations associated with the newly-assigned category.

**Interpretation**: Higher scores indicate better consistency and accuracy in categorical knowledge editing.

**Baseline Results**: Human subjects achieve approximately 86.8% accuracy on the same tasks.

**Validation**: Validation through human evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The human study included diverse participants but did not focus on demographic analysis.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: The human study was conducted under the approval of the Institutional Review Board at Arizona State University.

**Compliance With Regulations**: Not Applicable
