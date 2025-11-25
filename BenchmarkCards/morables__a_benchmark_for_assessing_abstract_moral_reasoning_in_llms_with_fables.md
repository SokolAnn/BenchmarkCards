# MORABLES: A Benchmark for Assessing Abstract Moral Reasoning in LLMs with Fables

## 📊 Benchmark Details

**Name**: MORABLES: A Benchmark for Assessing Abstract Moral Reasoning in LLMs with Fables

**Overview**: MORABLES is a human-verified benchmark built from fables and short stories drawn from literature, structured as multiple-choice questions targeting moral inference, including adversarial variants to test model robustness.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)
- SQuAD

**Resources**:
- [Resource](https://huggingface.co/datasets/cardiffnlp/Morables)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate moral reasoning capabilities of Large Language Models using literature-based benchmarks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Moral Reasoning
- Multiple Choice Question Answering

**Limitations**: Models may encounter memorization issues due to the pre-training data overlap.

## 💾 Data

**Source**: Public web resources under licenses that allow use and redistribution for research purposes.

**Size**: 709 pairs of fables and morals

**Format**: CSV

**Annotation**: Manual verification by human annotators

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics calculated based on predictions against ground truth.

**Interpretation**: Models are assessed on their ability to accurately infer morals from provided fables.

**Validation**: Human validation included for multiple-choice answers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All fables were screened for offensive content.

**Data Licensing**: Public resource usage with permissions as specified.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
