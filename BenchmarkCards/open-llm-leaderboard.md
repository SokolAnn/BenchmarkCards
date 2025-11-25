# Open-LLM-Leaderboard

## 📊 Benchmark Details

**Name**: Open-LLM-Leaderboard

**Overview**: This work aims to tackle the difficulties of evaluating large language models (LLMs) through entirely open-style questions, establishing a new benchmark to reflect their true capabilities.

**Data Type**: open-style questions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- HellaSwag
- ARC

**Resources**:
- [GitHub Repository](https://github.com/VILA-Lab/Open-LLM-Leaderboard)

## 🎯 Purpose and Intended Users

**Goal**: To refine the assessment process of large language models using open-style questions and eliminate issues found in multiple-choice questions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The performance metrics used may not fully capture the nuanced capabilities of each model.

## 💾 Data

**Source**: Evaluated from multiple datasets including MMLU, ARC, HellaSwag, WinoGrande, PIQA, CommonsenseQA, Race, MedMCQA, and OpenbookQA.

**Size**: 42,000 questions evaluated, 23,839 suitable for open-style answering

**Format**: N/A

**Annotation**: Automatically annotated for suitability as open-style questions

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is derived based on comparison of model-generated responses to a validated ground truth.

**Interpretation**: A significant drop in accuracy was observed for open-style questions compared to multiple-choice questions, with an average reduction of about 25%.

**Validation**: The automatic evaluation strategy was validated against human checks with an error rate of less than 5%.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User privacy concerns are minimal since the benchmark utilizes public datasets and questions.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
