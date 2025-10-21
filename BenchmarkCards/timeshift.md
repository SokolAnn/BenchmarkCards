# TimeShift

## 📊 Benchmark Details

**Name**: TimeShift

**Overview**: TimeShift is a novel framework and dataset designed to evaluate large language models' (LLMs) ability to handle time-sensitive facts, comprising over 8,000 events annotated with day-level granularity from 2018 to 2024, sourced globally across various domains.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/hereldav/TimeAware)

## 🎯 Purpose and Intended Users

**Goal**: To provide a structured framework for testing models' temporal awareness by evaluating their ability to correctly associate events with their respective time periods.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Temporal Reasoning
- Question Answering

**Limitations**: The dataset is exclusively in English, which may limit applicability to multilingual LLMs. It primarily focuses on open-source models requiring log probability access for evaluation.

## 💾 Data

**Source**: Constructed using a custom web-scraping pipeline from major global news outlets, academic journals, and government publications.

**Size**: 8,000 events

**Format**: N/A

**Annotation**: Automated filtering mechanisms cross-referenced timestamps and removed duplicates, while heuristic-based checks discarded ambiguous events.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- Stability

**Calculation**: Accuracy is evaluated based on the model's probability of correctly predicting the year, month, and day of an event.

**Interpretation**: A higher accuracy percentage indicates a better performance in associating a given event with its correct temporal context.

**Validation**: Evaluation is performed by measuring log probabilities against known time-sensitive facts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: The dataset includes a diverse range of events but may have an overrepresentation of Western events.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
