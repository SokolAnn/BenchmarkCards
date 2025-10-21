# DASHBOARD QA

## 📊 Benchmark Details

**Name**: DASHBOARD QA

**Overview**: DASHBOARD QA is the first benchmark explicitly designed to assess how vision-language GUI agents comprehend and interact with real-world dashboards, including 405 question-answer pairs with interactive dashboards spanning five categories: multiple-choice, factoid, hypothetical, multi-dashboard, and conversational.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- FigureQA
- PlotQA
- ChartQA

**Resources**:
- [GitHub Repository](https://github.com/vis-nlp/DashboardQA)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate question answering over interactive dashboards and to enhance the capabilities of vision-language and GUI agents in realistic analytical reasoning tasks.

**Target Audience**:
- ML Researchers
- AI Developers
- Data Analysts

**Tasks**:
- Question Answering

**Limitations**: The benchmark is tableau-centric, limiting visual and topic diversity.

## 💾 Data

**Source**: Collected interactive dashboards from Tableau Public

**Size**: 405 question-answer pairs

**Format**: N/A

**Annotation**: Expert-authored questions reviewed for accuracy.

## 🔬 Methodology

**Methods**:
- Evaluation of GUI agents
- Interactive navigation within virtual environments

**Metrics**:
- Accuracy

**Calculation**: Accuracy is based on the proportion of correct answers to questions across multiple observations.

**Interpretation**: Higher accuracy indicates better performance in navigating and reasoning over dashboards.

**Validation**: Inter-annotator agreement was measured at 74.93%, with revisions for inconsistencies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Dashboards collected were non-controversial, focusing on neutral and academic sources.

**Data Licensing**: All dashboards were taken from Tableau Public, which are publicly available.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
