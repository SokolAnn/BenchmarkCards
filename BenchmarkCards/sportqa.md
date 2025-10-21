# SportQA

## 📊 Benchmark Details

**Name**: SportQA

**Overview**: SportQA is a comprehensive benchmark specifically designed for evaluating Large Language Models (LLMs) in sports understanding, featuring over 70,000 multiple-choice questions across three distinct difficulty levels.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BIG-bench
- LiveQA

**Resources**:
- [GitHub Repository](https://github.com/haotianxia/SportQA)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dedicated sports-focused question-answering dataset for evaluating and improving LLMs' comprehension of sports.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: The primary limitation lies in the complexity of creating scenario-based questions for level-3, which limits the volume and range of sports covered.

## 💾 Data

**Source**: Originally sourced from various QA datasets including Trivia QA, QUASAR, and content from Wikipedia, with additional manual input from sports experts.

**Size**: 70,592 questions

**Format**: JSON

**Annotation**: Hybrid approach combining automated templates and expert-driven modifications.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the ratio of correctly answered questions to the total number of questions.

**Interpretation**: A higher accuracy indicates better sports understanding by the LLM.

**Validation**: Extensively validated through expert reviews and pilot testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: The dataset includes relevant demographic breakdowns, ensuring fair representation across various sports.

**Potential Harm**: ['Misleading information affecting sports understanding.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
