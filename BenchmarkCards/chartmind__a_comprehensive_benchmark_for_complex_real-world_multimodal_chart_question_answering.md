# ChartMind: A Comprehensive Benchmark for Complex Real-world Multimodal Chart Question Answering

## 📊 Benchmark Details

**Name**: ChartMind: A Comprehensive Benchmark for Complex Real-world Multimodal Chart Question Answering

**Overview**: ChartMind is a new benchmark designed for complex CQA tasks in real-world settings, covering seven task categories, incorporating multilingual contexts, supporting open-domain textual outputs, and accommodating diverse chart formats. It bridges the gap between real-world applications and traditional academic benchmarks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- ChartQA
- OpenCQA
- Chart-to-Text

**Resources**:
- [Resource](https://arxiv.org/abs/2505.23242)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation for complex chart question answering in real-world contexts.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Chart Classification
- Chart Summarization
- Chart Assistance
- Suggestions
- Chart Conversion
- Chart OCR Recognition
- Information Positioning

**Limitations**: The dataset relies on publicly available charts, potentially introducing biases, and future work will explore multi-turn dialogues and cross-chart reasoning.

## 💾 Data

**Source**: Over 1,200 charts collected from open-source platforms, including GitHub repositories and public datasets.

**Size**: 757 question-answering pairs

**Format**: N/A

**Annotation**: Each QA pair is reviewed by at least two annotators with experience in chart QA.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- CIDEr
- GPT-4o Score

**Calculation**: Metrics are calculated based on model performance against human reference answers.

**Interpretation**: Good performance is considered in terms of alignment with human judgments and coherence.

**Baseline Results**: N/A

**Validation**: Comprehensive evaluation across seven task categories using various models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The charts were collected under permissive licenses (e.g., CC BY 4.0, MIT).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
