# Hierarchical Knowledge Preference Benchmark (HIERPREF)

## 📊 Benchmark Details

**Name**: Hierarchical Knowledge Preference Benchmark (HIERPREF)

**Overview**: This benchmark evaluates the ability of language models to follow a defined hierarchy of knowledge preference among instruction knowledge, contextual knowledge, and parametric knowledge, while synthesizing diverse question-answer pairs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- IfQA
- MQuAKE
- MRQA

**Resources**:
- [Resource](https://arxiv.org/abs/2407.13048)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and enhance the ability of LLMs to prioritize knowledge correctly based on user instructions and contextual information.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Sourced from Wikipedia and Wikidata, synthesized to create diverse question-answer pairs with user assumptions.

**Size**: 9,000 examples

**Format**: N/A

**Annotation**: Automatically generated and synthesized without human annotation.

## 🔬 Methodology

**Methods**:
- Fine-tuning with synthesized instruction-tuning data
- Evaluation on various existing benchmarks

**Metrics**:
- F1 Score
- Exact Matching (EM)

**Calculation**: F1 Score is calculated based on the comparison of predicted answers with the ground truth.

**Interpretation**: Higher F1 Scores indicate better adherence to the knowledge preference hierarchy.

**Baseline Results**: Mistral-v0.3-7B fine-tuned with HIERPREF outperformed other models in question answering tasks.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
