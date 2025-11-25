# QuRe (Quantifier Reasoning)

## 📊 Benchmark Details

**Name**: QuRe (Quantifier Reasoning)

**Overview**: QuRe is a crowd-sourced dataset of human-annotated generalized quantifiers in Wikipedia sentences featuring percentage-equipped predicates. It is designed to evaluate the quantifier understanding capabilities of foundation models in natural language processing.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HVD (Hierarchical Quantifier Dataset)

**Resources**:
- [GitHub Repository](https://github.com/Nativeatom/PRESQUE)

## 🎯 Purpose and Intended Users

**Goal**: To investigate quantifier understanding in foundation models and provide a dataset for evaluating their capabilities.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Quantifier Understanding
- Natural Language Inference

**Limitations**: Despite the value of our dataset and the promising results from the PRESQUE framework, our analysis and findings have some notable limitations.

## 💾 Data

**Source**: Crowd-sourced from Wikipedia sentences with percentage annotations.

**Size**: 744 sentences

**Format**: JSON

**Annotation**: Crowd-sourced via Amazon Mechanical Turk and hybrid annotations with GPT-3.5-turbo.

## 🔬 Methodology

**Methods**:
- Natural Language Inference
- Human evaluation

**Metrics**:
- Span-based F1 Score
- Mean Reciprocal Rank (MRR)
- Cross-Entropy

**Calculation**: Metrics are calculated based on the comparison between predicted percentage scopes and the gold standard.

**Interpretation**: Scores higher than the baseline indicate better quantifier understanding performance.

**Baseline Results**: PRESQUE achieves better performance than L0 in several metrics including higher HIT@1 and lower cross-entropy.

**Validation**: Validated through human evaluations and quantitative metrics on model performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: The dataset does not currently analyze demographic factors.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personally identifiable information about the annotators was collected.

**Data Licensing**: Not Applicable

**Consent Procedures**: All annotators were informed about the study and compensated fairly.

**Compliance With Regulations**: Not Applicable
