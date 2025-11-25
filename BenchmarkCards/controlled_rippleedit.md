# Controlled RippleEdit

## 📊 Benchmark Details

**Name**: Controlled RippleEdit

**Overview**: Controlled RippleEdit is a new dataset designed to evaluate knowledge propagation capabilities of language models, allowing for focused assessment of generalization by testing relations and entities that were unseen during hypernetwork training.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RippleEdit

**Resources**:
- [GitHub Repository](https://github.com/edenbiran/RippleEdits/tree/main/data/benchmark)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate knowledge propagation in language models through a designed set of propagation questions and injected knowledge facts.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Multi-hop Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic generation from structured templates based on fictional stories and well-known entities.

**Size**: 5,000 examples

**Format**: JSON

**Annotation**: Manually designed templates and paired question-answer sets.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- LLM-Score (Accuracy)

**Calculation**: Metrics are calculated based on model performance against validation sets of efficacy and specificity.

**Interpretation**: Higher LLM-Score indicates better ability of the model to propagate knowledge correctly.

**Baseline Results**: PropMEND significantly outperformed baselines like Prepend and MEND in both in-domain and out-of-domain settings.

**Validation**: Performance evaluated using cross-validation on separate validation and test splits.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
