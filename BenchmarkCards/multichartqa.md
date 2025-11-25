# MultiChartQA

## 📊 Benchmark Details

**Name**: MultiChartQA

**Overview**: MultiChartQA is a benchmark that evaluates MLLMs' capabilities in four key areas: direct question answering, parallel question answering, comparative reasoning, and sequential reasoning, particularly in multi-chart scenarios.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Zivenzhu/Multi-chart-QA)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the reasoning capabilities of Multimodal Large Language Models in multi-chart scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The overall scale of the multi-chart sets is relatively limited due to the labor-intensive data collection process.

## 💾 Data

**Source**: The benchmark draws from a diverse set of public resources containing multi-chart articles, including Arxiv, OECD, Our World in Data, among others.

**Size**: 1,370 unique charts and 2,000 questions

**Format**: N/A

**Annotation**: All questions and answers in the benchmark are manually annotated.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is evaluated using relaxed accuracy for numerical answers and exact match for non-numeric answers.

**Interpretation**: Higher accuracy indicates better multi-chart reasoning capabilities of MLLMs.

**Baseline Results**: Human performance averaged at 90.11% across all tasks.

**Validation**: Evaluated through performance measurements against human results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
