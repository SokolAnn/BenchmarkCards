# STORY FEEDBACK

## 📊 Benchmark Details

**Name**: STORY FEEDBACK

**Overview**: The STORY FEEDBACK dataset consists of 83,456 story and model-generated feedback pairs used to evaluate how well language models can provide constructive writing feedback on short stories with controlled writing issues.

**Data Type**: story-feedback pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/google-deepmind/igen)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the ability of LLMs to generate meaningful feedback for creative writing, particularly for identifying and addressing writing issues.

**Target Audience**:
- ML Researchers
- Educators
- Creative Writers

**Tasks**:
- Writing Feedback

**Limitations**: The study is limited to English stories and synthetic writing issues, which may not represent naturally occurring errors.

## 💾 Data

**Source**: The dataset comprises stories collected from publicly available datasets including ROCStories and various BIG-bench story datasets.

**Size**: 83,456 story-feedback pairs

**Format**: N/A

**Annotation**: Model-generated feedback evaluated for quality by human annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Correctness
- Error Detection
- Specificity
- Relevance

**Calculation**: Metrics calculated based on human annotation scores and automated evaluations of model outputs.

**Interpretation**: Feedback is evaluated based on its relevance and specificity to the writing issues present in the stories.

**Baseline Results**: N/A

**Validation**: Evaluated by human annotators on multiple dimensions of feedback quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
