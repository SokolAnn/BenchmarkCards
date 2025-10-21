# ChartGalaxy: A Dataset for Infographic Chart Understanding and Generation

## 📊 Benchmark Details

**Name**: ChartGalaxy: A Dataset for Infographic Chart Understanding and Generation

**Overview**: ChartGalaxy is a million-scale dataset designed for advancing the understanding and generation of infographic charts. It includes 1,701,356 synthetic and 61,833 real infographic charts paired with their respective data tables, facilitating applications in infographic chart understanding, code generation, and chart generation.

**Data Type**: synthetic and real infographic charts with data tables

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- InfographicVQA
- ChartQAPro

**Resources**:
- [GitHub Repository](https://github.com/ChartGalaxy/ChartGalaxy)
- [Resource](https://huggingface.co/datasets/ChartGalaxy/ChartGalaxy)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for training models on the understanding and generation of infographic charts.

**Target Audience**:
- ML Researchers
- Model Developers
- Data Visualization Specialists

**Tasks**:
- Infographic Chart Understanding
- Infographic Chart Code Generation
- Example-based Infographic Chart Generation

**Limitations**: N/A

## 💾 Data

**Source**: The dataset comprises both collected real infographic charts from reputable websites and programmatically created synthetic charts based on identified chart types and layouts.

**Size**: 1,701,356 synthetic infographic charts and 61,833 real infographic charts

**Format**: JSON, tabular data

**Annotation**: The data was annotated using a multi-step human-in-the-loop verification pipeline.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- Visual similarity scoring

**Calculation**: Metrics are calculated based on visual alignment and fidelity to the original infographic designs.

**Interpretation**: A higher score indicates better visual reproduction and fidelity to the original chart elements and structure.

**Baseline Results**: N/A

**Validation**: Models were validated on independent benchmarks and through experiments measuring performance across various qualitative and quantitative tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Safety
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All real charts collected from public and reputable sources that permit research use and are filtered to avoid sensitive content.

**Data Licensing**: Real charts are collected under licenses that allow research use, including Creative Commons.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
