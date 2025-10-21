# Mind2Web 2

## 📊 Benchmark Details

**Name**: Mind2Web 2

**Overview**: Mind2Web 2 is a benchmark of 130 realistic, high-quality, and long-horizon tasks that require real-time web browsing and extensive information synthesis, constructed with over 1,000 hours of human labor. It aims to evaluate agentic search systems on complex, time-varying tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- BrowseComp

**Resources**:
- [Resource](https://osu-nlp-group.github.io/Mind2Web-2/)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously evaluate agentic search systems on realistic and long-horizon tasks involving real-time web search and browsing.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Information Retrieval
- Web Search

**Limitations**: N/A

## 💾 Data

**Source**: Constructed with over 1,000 hours of human labor across diverse practical domains.

**Size**: 130 tasks

**Format**: Task descriptions and evaluation scripts

**Annotation**: Tasks were validated by experienced annotators.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Partial Completion
- Success Rate

**Calculation**: Metrics are computed based on aggregation of correct evaluations from the rubric.

**Interpretation**: Higher scores indicate better performance in completing complex, time-varying tasks.

**Baseline Results**: The best-performing agent is OpenAI Deep Research, achieving 50-70% human performance in time-varying tasks.

**Validation**: Tasks and evaluation methods underwent multi-stage validation involving expert annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Robustness
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
