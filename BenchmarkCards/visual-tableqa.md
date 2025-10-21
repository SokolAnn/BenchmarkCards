# Visual-TableQA

## 📊 Benchmark Details

**Name**: Visual-TableQA

**Overview**: Visual-TableQA is a large-scale, open-domain multimodal dataset specifically designed to evaluate and enhance visual reasoning over complex tabular data, consisting of 2.5k LaTeX-rendered tables and 6k reasoning-intensive question-answer pairs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- ChartQA
- ReachQA
- MATH-Vision

**Resources**:
- [GitHub Repository](https://github.com/AI-4-Everyone/Visual-TableQA)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously evaluate visual reasoning capabilities over complex table images through challenging question-answering tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generative pipeline utilizing reasoning-oriented language models to produce LaTeX-rendered tables and corresponding question-answer pairs.

**Size**: 2,500 tables and 6,000 question-answer pairs

**Format**: LaTeX

**Annotation**: Human validation by annotators and automated reasoning quality checks using LLMs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- ROSCOE reasoning score

**Calculation**: Metrics are computed based on the model's performance on test sets, ensuring alignment with visual reasoning capabilities.

**Interpretation**: Higher accuracy and ROSCOE scores indicate effective reasoning and understanding of complex visual structures.

**Validation**: The dataset is validated through a jury of high-performing reasoning LLMs and manual human evaluation of QA pairs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
