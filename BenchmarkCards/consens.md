# ConSens

## 📊 Benchmark Details

**Name**: ConSens

**Overview**: ConSens is a novel metric for evaluating the influence of provided context on LLM-generated responses in open-book QA tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct)
- [GitHub Repository](https://github.com/chroma-core/chroma)

## 🎯 Purpose and Intended Users

**Goal**: To quantify how strongly the output of an LLM is influenced by the provided context.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Open-book Question Answering

**Limitations**: ConSens requires access to raw outputs (i.e., logits) of the model used for evaluation.

## 💾 Data

**Source**: Empirical analysis conducted using various datasets, including WikiEval and biomedical abstracts.

**Size**: 657 examples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Token perplexity calculations

**Metrics**:
- ROC AUC

**Calculation**: Calculates the perplexity of the model output under two conditions: when the context is provided and when it is not.

**Interpretation**: Higher ConSens values indicate stronger reliance on the provided context.

**Validation**: Validated through experiments comparing answers based on provided context versus parametric knowledge.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
