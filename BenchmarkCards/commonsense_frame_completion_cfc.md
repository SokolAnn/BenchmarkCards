# Commonsense Frame Completion (CFC)

## 📊 Benchmark Details

**Name**: Commonsense Frame Completion (CFC)

**Overview**: Commonsense Frame Completion (CFC) is a novel generative task that evaluates common sense via multiple open-ended generations, capturing the probabilistic nature of common sense by allowing for multiple correct answers to questions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ProtoQA

**Resources**:
- [GitHub Repository](https://github.com/qxc101/PROBEVAL_CFC)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate implicit common sense in various contexts through a generative question answering task with multiple correct answers.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Commonsense Reasoning

**Limitations**: The collected answers may be biased towards English speakers in the US, and the framework may not capture commonsense across diverse cultures.

## 💾 Data

**Source**: CommonGen dataset, which provides sentences with implicit commonsense knowledge.

**Size**: 63,788 context sentences, resulting in 228,170 pairs of context questions with missing slots.

**Format**: JSON

**Annotation**: Collected via human annotators on platforms like Amazon MTurk.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- KL Divergence

**Calculation**: The common sense evaluation is calculated by deriving a categorical distribution over answer clusters and measuring KL divergence between the ground truth and the model-generated answers.

**Interpretation**: A lower KL divergence indicates a better performance of the model in capturing the common sense knowledge distribution.

**Validation**: Verified through correlations of PROBEVAL with human judgments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Privacy**: Personal information in data

**Demographic Analysis**: The dataset may not adequately represent diverse global populations due to its focus on English speakers in the US.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
