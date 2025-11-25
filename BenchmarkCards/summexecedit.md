# SummExecEdit

## 📊 Benchmark Details

**Name**: SummExecEdit

**Overview**: SummExecEdit is a novel pipeline and benchmark that leverages executable edits to assess models' abilities to detect factual errors in summarization and provide accurate explanations.

**Data Type**: factual inconsistency summaries

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SummEdits

**Resources**:
- [Resource](https://huggingface.co/datasets/Salesforce/summexecedit)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate large language models on their ability to detect factual inconsistencies and provide explanations for them.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Factual Consistency Detection
- Explanation Generation

**Limitations**: Generating benchmarks with executable edits require availability of ground truth pairs which might not always be the case.

## 💾 Data

**Source**: Generated from large language models using executable prompts.

**Size**: 4,241 samples

**Format**: JSON

**Annotation**: Manually annotated by researchers based on multiple evaluative criteria.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Detection Accuracy
- Explanation Score

**Calculation**: Detection Score is calculated based on the proportion of correct predictions among factually inconsistent summaries.

**Interpretation**: A higher detection accuracy indicates a model's better ability to identify factual inconsistencies.

**Baseline Results**: The best model achieves a Detection Accuracy of 73% on the benchmark.

**Validation**: Manual annotation and error analysis for the generated inconsistencies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Transparency

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Apache-2.0 license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
