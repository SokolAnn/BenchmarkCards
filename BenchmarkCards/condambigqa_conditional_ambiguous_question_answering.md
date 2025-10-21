# CondAmbigQA (Conditional Ambiguous Question Answering)

## 📊 Benchmark Details

**Name**: CondAmbigQA (Conditional Ambiguous Question Answering)

**Overview**: CondAmbigQA is a benchmark comprising 2,000 ambiguous queries with condition-aware evaluation metrics to improve accuracy in question-answering tasks by identifying implicit assumptions and providing contextual constraints.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AmbigQA
- ASQA
- ALCE

**Resources**:
- [Resource](https://huggingface.co/datasets/Apocalypse-AGI-DAO/CondAmbigQA-2K)

## 🎯 Purpose and Intended Users

**Goal**: To address ambiguity in question-answering by incorporating explicit conditions that help clarify interpretations and enhance answer accuracy.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: Despite the promising results, certain types of ambiguity may still be underrepresented.

## 💾 Data

**Source**: Constructed from ambiguous queries and Wikipedia fragments.

**Size**: 2,000 examples

**Format**: JSON

**Annotation**: Human-LLM interactive annotation with GPT-4o assistance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- G-Eval
- Condition Score
- Answer Score
- Citation Score
- Combined Score

**Calculation**: Metrics are calculated based on comparisons of model outputs to the ground-truth answers and conditions.

**Interpretation**: Higher scores indicate better condition identification and answer accuracy.

**Baseline Results**: Model performances were evaluated across multiple LLMs, with API models like GPT-4o achieving higher scores than local models.

**Validation**: The scores correlate strongly with human evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data

**Demographic Analysis**: The dataset includes a diverse range of ambiguous questions but may not fully represent all demographic contexts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data is anonymized and does not include personal information.

**Data Licensing**: The dataset will be released under the CC BY-SA 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
