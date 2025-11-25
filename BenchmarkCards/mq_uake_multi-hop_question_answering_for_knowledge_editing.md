# MQ UAKE (Multi-hop Question Answering for Knowledge Editing)

## 📊 Benchmark Details

**Name**: MQ UAKE (Multi-hop Question Answering for Knowledge Editing)

**Overview**: MQ UAKE comprises multi-hop questions that assess whether edited models correctly answer questions where the answer should change as an entailed consequence of edited facts.

**Data Type**: multi-hop question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/princeton-nlp/MQuAKE)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate knowledge editing methods for language models via multi-hop questions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from Wikidata and includes user-generated questions via prompts to ChatGPT.

**Size**: 9,218 multi-hop questions for MQ UAKE-CF; 1,868 instances for MQ UAKE-T

**Format**: N/A

**Annotation**: Manually selected fact chains and generated questions via ChatGPT.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Edit-wise success rate
- Instance-wise accuracy
- Multi-hop accuracy

**Calculation**: Calculates the success of knowledge edits based on how many facts can be recalled and how many multi-hop questions can be answered correctly.

**Interpretation**: The ability of the edited model to use newly injected knowledge correctly in answers to multi-hop questions.

**Validation**: Tested against various state-of-the-art knowledge editing approaches.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
