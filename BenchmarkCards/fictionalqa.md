# FictionalQA

## 📊 Benchmark Details

**Name**: FictionalQA

**Overview**: The FictionalQA dataset empowers researchers to study the dual processes of fact memorization and verbatim sequence memorization using synthetically-generated documents about fictional events and associated question-answer pairs.

**Data Type**: question-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TriviaQA
- TOFU
- Fictional Knowledge

**Resources**:
- [Resource](https://huggingface.co/datasets/tomg-group-umd/fictionalqa)
- [GitHub Repository](https://github.com/jwkirchenbauer/fictionalqa)

## 🎯 Purpose and Intended Users

**Goal**: To study the processes and dynamics of memorization in language models, particularly focusing on distinguishing fact memorization from verbatim memorization.

**Target Audience**:
- ML Researchers
- Model Developers
- Academic Institutions

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic generation process based on fictional events.

**Size**: 7,500 question-answer pairs

**Format**: JSON

**Annotation**: Automated generation with controlled prompts for question and answer creation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated by evaluating model performance on question-answer pairs derived from the fictional documents.

**Interpretation**: Higher accuracy indicates better memorization and transfer of knowledge from training to inference.

**Baseline Results**: N/A

**Validation**: The dataset includes various validation splits to assess model performance on generalization.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: ['Exposure to inaccurate or fictional information']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
