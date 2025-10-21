# InfoChartQA

## 📊 Benchmark Details

**Name**: InfoChartQA

**Overview**: InfoChartQA is a benchmark for evaluating multimodal large language models (MLLMs) on infographic chart understanding. It includes 5,642 pairs of infographic and plain charts, each sharing the same underlying data but differing in visual presentations, along with visual-element-based questions designed to capture unique visual designs and communicative intents.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- InfographicVQA
- ChartQAPro

**Resources**:
- [GitHub Repository](https://github.com/CoolDawnAnt/InfoChartQA)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic benchmark for evaluating multimodal large language models on the understanding of infographic charts and their visual elements.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Question Answering

**Limitations**: While InfoChartQA presents a comprehensive benchmark, it has limitations such as difficulties in constructing metaphor-related questions and reliance on templates that may limit diversity.

## 💾 Data

**Source**: Collected from 11 real-world mainstream visualization platforms.

**Size**: 5,642 infographic and plain chart pairs

**Format**: N/A

**Annotation**: Created by combining automated and manual processes involving expert verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on ANLS score and relaxed accuracy metric for numeric answers.

**Interpretation**: Higher performance indicates better understanding of infographic design elements and data relationships.

**Baseline Results**: Human baseline performance is set as a benchmark for MLLM comparisons.

**Validation**: Thorough evaluation using a diverse set of MLLMs on the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Custom licensing from data sources.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
