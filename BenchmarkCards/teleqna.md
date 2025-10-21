# TeleQnA

## 📊 Benchmark Details

**Name**: TeleQnA

**Overview**: TeleQnA is the first benchmark dataset designed to evaluate the knowledge of Large Language Models (LLMs) in telecommunications, consisting of 10,000 questions and answers drawn from diverse sources including standards and research articles.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Telecommunications

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/netop-team/TeleQnA)

## 🎯 Purpose and Intended Users

**Goal**: To provide a specialized benchmark dataset for evaluating LLMs' telecom knowledge and to highlight the need for a specialized telecom foundation model.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The dataset generation process is inherently subjective, as it relies on human judgment to evaluate the correctness of questions.

## 💾 Data

**Source**: Comprehensive collection from open-access telecom standards, research articles, and technical documentation.

**Size**: 10,000 questions

**Format**: JSON

**Annotation**: Automated question generation framework with human verification.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is defined as the percentage of questions where the entity selected the correct option.

**Interpretation**: Higher accuracy indicates better performance in understanding telecom-related knowledge.

**Baseline Results**: GPT-3.5 averaged an accuracy of 67%, while GPT-4 achieved an accuracy of 74%.

**Validation**: The questions were validated using LLM-based framework and human experts for correctness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
