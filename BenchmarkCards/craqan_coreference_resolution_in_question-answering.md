# CRaQAn (Coreference Resolution in Question-Answering)

## 📊 Benchmark Details

**Name**: CRaQAn (Coreference Resolution in Question-Answering)

**Overview**: CRaQAn is an open-source dataset that provides over 250 question-answer pairs containing coreferences, specifically designed for evaluating coreference resolution in question-answering tasks.

**Data Type**: question-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Quoref
- HotpotQA

**Resources**:
- [Resource](https://huggingface.co/datasets/Edge-Pyxos/CRaQAn_v1)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for evaluating coreference resolution in question-answering tasks and to establish a methodology for automated dataset creation.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Question Answering

**Limitations**: The initial CRaQAn release contains 261 question-answer pairs; while it demonstrates the potential for automated dataset generation, the dataset's size may limit its utility in extensive evaluations.

## 💾 Data

**Source**: Crafted from 70 Wikipedia articles on modern U.S. laws, selected to contain complex coreference relationships.

**Size**: 261 question-answer pairs

**Format**: Markdown

**Annotation**: Automated with GPT-4 and human reviews.

## 🔬 Methodology

**Methods**:
- Automated dataset generation
- Human evaluation

**Metrics**:
- Quality of question-answer pairs
- Human reviewer acceptance rate

**Calculation**: Metrics are derived from the proportion of QA pairs accepted by human reviewers out of those generated.

**Interpretation**: Higher acceptance rates indicate better quality and more successful coreference resolution.

**Baseline Results**: 348 out of 578 generated QA pairs were reviewed, with a 60.2% acceptance rate.

**Validation**: Human reviewers assessed candidate entries for quality, ensuring adherence to established guidelines.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: The dataset may inherit biases from the underlying Wikipedia content, potentially affecting the fairness of its application.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
