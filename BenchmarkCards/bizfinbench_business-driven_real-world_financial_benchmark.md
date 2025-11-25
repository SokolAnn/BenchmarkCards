# BizFinBench (Business-Driven Real-World Financial Benchmark)

## 📊 Benchmark Details

**Name**: BizFinBench (Business-Driven Real-World Financial Benchmark)

**Overview**: BizFinBench is the first benchmark specifically designed to evaluate large language models (LLMs) in real-world financial applications, consisting of 6,781 well-annotated queries grouped into nine fine-grained categories across five dimensions: numerical calculation, reasoning, information extraction, prediction recognition, and knowledge-based question answering.

**Data Type**: question-answering pairs

**Domains**:
- Finance

**Languages**:
- Chinese

**Similar Benchmarks**:
- FinEval

**Resources**:
- [GitHub Repository](https://github.com/HiThink-Research/BizFinBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating LLMs through a business-driven methodology across various financial tasks.

**Target Audience**:
- ML Researchers
- Finance Professionals
- Model Developers

**Tasks**:
- Financial Prediction
- Information Extraction
- Reasoning
- Numerical Calculation
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Real user queries from iwencai APP and additional context data from internal and external financial sources.

**Size**: 6,781 examples

**Format**: JSON

**Annotation**: Annotated by three senior financial experts to ensure accuracy and relevance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Judge Score

**Calculation**: Metrics are computed based on expert-validated answers compared to model outputs.

**Interpretation**: Higher scores indicate better alignment with correct answers and reasoning quality.

**Baseline Results**: N/A

**Validation**: Performance validated against multiple LLMs in diverse financial contexts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: ['Misleading financial information']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
