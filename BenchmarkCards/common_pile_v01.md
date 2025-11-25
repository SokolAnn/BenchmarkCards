# Common Pile v0.1

## 📊 Benchmark Details

**Name**: Common Pile v0.1

**Overview**: Common Pile v0.1 is an 8TB dataset of openly licensed text designed for LLM pretraining, comprising content from 30 diverse sources, demonstrating the feasibility of achieving performant models without using unlicensed text.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Science
- Education

**Languages**:
- English

**Similar Benchmarks**:
- OLC (Open License Corpus)
- Common Corpus
- KL3M
- The Pile

**Resources**:
- [GitHub Repository](https://github.com/username/repo)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large, diverse, and openly licensed dataset for pretraining language models to facilitate more ethical AI developments.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Text Classification
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Common Pile v0.1

**Size**: 8TB

**Format**: text

**Annotation**: Curated and validated by filtering, deduplication, and reweighting of diverse openly licensed sources.

## 🔬 Methodology

**Methods**:
- Model-based evaluation
- Data ablation study

**Metrics**:
- Accuracy
- F1 Score
- MMLU

**Calculation**: Metrics are calculated based on model evaluation against multiple benchmarks after training on the dataset.

**Interpretation**: A higher score is indicative of improved model performance on the tasks evaluated.

**Baseline Results**: N/A

**Validation**: Models were validated through controlled experiments comparing performance across different datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Privacy
- Accuracy
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Data privacy rights alignment
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Ensured filtering to remove personally identifiable information (PII) and inappropriate content.

**Data Licensing**: The dataset is curated from openly licensed texts under various licenses such as CC BY, CC BY-SA, and public domain.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
