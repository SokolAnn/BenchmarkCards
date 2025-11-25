# FDM-Bench

## 📊 Benchmark Details

**Name**: FDM-Bench

**Overview**: FDM-Bench is a benchmark dataset designed to evaluate LLMs on FDM-specific tasks, including user queries and G-code anomaly detection.

**Data Type**: question-answering pairs, G-code samples

**Domains**:
- Natural Language Processing
- Additive Manufacturing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/AhmadrezaNia/FDM-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the effectiveness of LLMs on a range of FDM-specific tasks.

**Target Audience**:
- Researchers in Additive Manufacturing
- Developers of Large Language Models
- Industry Practitioners in 3D Printing

**Tasks**:
- User Query Response
- G-code Anomaly Detection

**Limitations**: N/A

## 💾 Data

**Source**: G-codes are generated from 3D printing processes, and questions are curated from industry experts and educational resources.

**Size**: N/A

**Format**: N/A

**Annotation**: G-codes and user queries are designed to represent various FDM contexts and expertise levels.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Response relevance

**Calculation**: Metrics are calculated based on human evaluator scores for free-form questions and accuracy percentages for MCQs.

**Interpretation**: Accuracy reflects how well the model's responses match expected answers, while precision evaluates focus and relevance.

**Baseline Results**: Prior model evaluations included GPT-4o, Claude 3.5 Sonnet, Llama-3.1-70B, and Llama-3.1-405B.

**Validation**: Validation is done through expert evaluations and automatic scoring of multiple-choice questions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Safety
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
