# WebUIBench

## 📊 Benchmark Details

**Name**: WebUIBench

**Overview**: WebUIBench is a benchmark systematically designed to evaluate Multimodal Large Language Models (MLLMs) in four key areas: WebUI Perception, HTML Programming, WebUI-HTML Understanding, and WebUI-to-Code, comprising 21K high-quality question-answer pairs derived from over 0.7K real-world websites.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Web2Code
- Design2Code

**Resources**:
- [GitHub Repository](https://github.com/MAIL-Tele-AI/WebUIBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the WebUI-to-Code capabilities of Multimodal Large Language Models (MLLMs).

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- WebUI-to-Code
- WebUI Perception
- HTML Programming
- WebUI-HTML Understanding

**Limitations**: Imbalanced data distribution across subtasks; lack of mobile webpage evaluation datasets; absence of page functionality interaction evaluation.

## 💾 Data

**Source**: High-quality website data collected from 719 full webpages and 2488 webpage slices.

**Size**: 21,793 question-answer pairs

**Format**: JSON, HTML, PNG

**Annotation**: Automatically generated and manually verified.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- String similarity
- Cosine similarity

**Calculation**: For multiple-choice tasks, accuracy is the scoring metric, and for open-ended tasks, string similarity is calculated.

**Interpretation**: Higher scores indicate better model performance in generating correct HTML code or accurately matching webpage elements.

**Baseline Results**: Performance comparisons with closed-source models like GPT-4o and open-source models like InternVL2.5 reported.

**Validation**: Validation performed through extensive evaluation of 29 mainstream MLLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Output bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Open-source data available under standard licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
