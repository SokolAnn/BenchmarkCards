# WebPuzzle

## 📊 Benchmark Details

**Name**: WebPuzzle

**Overview**: WebPuzzle is designed to foster information-seeking behavior in open-world internet environments, enabling the evaluation of large language models' capabilities in dynamic search intensity scaling.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HotpotQA
- Bamboogle

**Resources**:
- [Resource](https://arxiv.org/abs/2505.24332)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark and evaluate the information-seeking capabilities of large language models in real-world open-web contexts.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Composed of 24,000 training examples and 275 test questions derived from both wiki-based and open-web queries.

**Size**: 24,000 training instances; 275 test questions

**Format**: Mixed (both open-web queries and Wiki-based queries)

**Annotation**: Human-annotated for test set; training set generated through LLMs.

## 🔬 Methodology

**Methods**:
- Reinforcement Learning
- Supervised Fine-Tuning
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated as the proportion of correct answers over total answers.

**Interpretation**: Higher accuracy indicates better performance in information-seeking tasks.

**Validation**: The dataset validation is based on expert annotation of test samples.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
