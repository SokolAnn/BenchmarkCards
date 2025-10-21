# TUR[K]INGBENCH

## 📊 Benchmark Details

**Name**: TUR[K]INGBENCH

**Overview**: TURKING BENCH is a benchmark consisting of tasks presented as web pages with textual instructions and multi-modal contexts, aimed at evaluating models' ability to perform complex web-based tasks found on crowdsourcing platforms.

**Data Type**: web-based tasks with textual and visual instructions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MiniWoB++
- CompWoB
- WebShop
- Mind2Web
- WebArena

**Resources**:
- [Resource](https://turkingbench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized evaluation for web-based agents and facilitate research on multimodal interactive web-based tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Web-based Task Completion

**Limitations**: The benchmark is limited to tasks involving data annotation and does not require navigation between web pages.

## 💾 Data

**Source**: Crowdsourced tasks from Amazon Mechanical Turk

**Size**: 36.2K instances

**Format**: HTML with integrated text and visual elements

**Annotation**: Annotated output labels provided by crowd workers

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- ROUGE
- Exact Match
- Intersection over Union

**Calculation**: Metrics are calculated based on the type of input field: ROUGE for text fields, exact match for radio/select fields, intersection over union for checkbox fields, and L1 distance for range fields.

**Interpretation**: Scores are averaged across different field types to assess model performance.

**Baseline Results**: GPT4 achieved a top score of 41.7%, significantly above random chance but below the maximum achievable performance.

**Validation**: Evaluation is conducted iteratively, where models interact with web pages and provide responses to input fields.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
