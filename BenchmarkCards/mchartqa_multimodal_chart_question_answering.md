# mChartQA (Multimodal Chart Question Answering)

## 📊 Benchmark Details

**Name**: mChartQA (Multimodal Chart Question Answering)

**Overview**: mChartQA is a universal benchmark for multimodal chart question answering based on vision-language alignment and reasoning, facilitating effective processing and integration of complex visual and textual information.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- ChartQA
- PlotQA
- FigureQA

**Resources**:
- [Resource](https://arxiv.org/abs/2404.01548)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating and enhancing multimodal chart question answering systems.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The benchmark includes data from various multimodal and question-answering datasets such as ChartQA, PlotQA, and FigureQA.

**Size**: 300,000 pairs

**Format**: JSON

**Annotation**: The data is derived from existing datasets and is curated to fit the requirements for the chart question-answering tasks.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on exact matching for textual answers and a tolerance level for numeric answers.

**Interpretation**: Predictions must match the correct answer exactly for textual responses, while numeric answers have a tolerance of up to 5% error.

**Baseline Results**: mChartQA's performance is benchmarked against various few-shot and fully-supervised models.

**Validation**: The model's performance is validated using metrics from the ChartQA, PlotQA, and FigureQA datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Misinterpretation of critical chart details', 'Ambiguities leading to incorrect answers']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
