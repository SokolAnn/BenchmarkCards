# HalluRAG

## 📊 Benchmark Details

**Name**: HalluRAG

**Overview**: HalluRAG is a dataset designed to detect closed-domain hallucinations in RAG applications by employing recency, focusing on novel information added after a specified cut-off date that could not have been used for training.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/F4biian/HalluRAG)
- [Resource](https://miami.uni-muenster.de/Record/10.17879%2F84958668505/Details)

## 🎯 Purpose and Intended Users

**Goal**: To create a heterogeneous dataset that allows training MLP-based classifiers to detect closed-domain hallucinations in RAG systems.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Hallucination Detection

**Limitations**: N/A

## 💾 Data

**Source**: Wikipedia articles, focusing on recent sentences and their corresponding questions and answers.

**Size**: 19,731 validly annotated sentences

**Format**: JSON

**Annotation**: Auto-labeling using GPT-4o based on a detailed Chain-of-Thought prompt.

## 🔬 Methodology

**Methods**:
- Neural network training using internal states of LLMs

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Classifier outputs are based on the internal states of LLMs to predict hallucination labels.

**Interpretation**: The accuracy of the classifiers indicates the likelihood of hallucination detection based on LLM internal states.

**Baseline Results**: Test accuracies range up to 75%, with Mistral-7B-Instruct-v0.1 achieving the highest test accuracies.

**Validation**: Oversampling techniques were used to balance the dataset across hallucinated and non-hallucinated examples.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No reliance on personal data, using publicly available sources.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
