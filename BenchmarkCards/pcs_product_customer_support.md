# PCS (Product Customer Support)

## 📊 Benchmark Details

**Name**: PCS (Product Customer Support)

**Overview**: The PCS dataset is a new TOD dataset studied in this work that captures real-world customer-human expert interactions, focusing on behavioral analysis and performance evaluation of LLM agents in complex task-oriented dialogs.

**Data Type**: dialog pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MultiWOZ
- SpokenWOZ

**Resources**:
- [GitHub Repository](https://github.com/intuit-ai-research/behavior-gap)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the behavioral performance gaps between LLM agents and human experts in task-oriented dialogs.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Task-Oriented Dialog System Evaluation

**Limitations**: The accuracy of the analysis depends on the reliability of the LLM-based classifiers used in the framework.

## 💾 Data

**Source**: Real-world transcribed spoken conversations between customers and human expert agents.

**Size**: 832 dialogs

**Format**: Text

**Annotation**: Classifiers evaluated on the precision of dialog act recognition and tool usage.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: Micro-F1 scores quantified dialog act and tool usage alignment.

**Interpretation**: Higher F1 scores indicate better alignment between LLM agents and human expert responses.

**Validation**: Validation of classifiers against established dialog act and tool usage benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: Analysis focused on behavioral gaps across different task complexities.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
