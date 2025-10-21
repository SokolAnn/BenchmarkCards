# MMDocBench

## 📊 Benchmark Details

**Name**: MMDocBench

**Overview**: MMDocBench is a benchmark designed to holistically assess the fine-grained visual understanding capability of Large Vision-Language Models (LVLMs) through various OCR-free document understanding tasks. It consists of 15 main tasks and 48 sub-tasks, involving 2,400 document images, 4,338 QA pairs, and 11,353 supporting regions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MMVet
- MME
- MMT-Bench

**Resources**:
- [Resource](https://MMDocBench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to comprehensively evaluate LVLMs’ fine-grained visual perception and reasoning capabilities via various OCR-free document understanding tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Recognition
- Table Recognition
- Text Localization
- Table Cell Localization
- Key Information Extraction
- Document Forgery Detection
- Document Question Answering
- Chart Question Answering
- Infographic Question Answering
- Arithmetic Reasoning
- Logical Reasoning
- Spatial Reasoning
- Comparison
- Sorting
- Counting

**Limitations**: N/A

## 💾 Data

**Source**: The data comes from 21 document understanding datasets covering a variety of document image types, including research papers, receipts, financial reports, and infographics.

**Size**: 4,338 QA pairs and 11,353 supporting regions

**Format**: N/A

**Annotation**: Annotations of supporting regions in the images for each QA pair are provided.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match (EM)
- F1 Score
- Intersection over Union (IOU)

**Calculation**: Metrics are calculated based on the performance of LVLMs on the provided QA pairs across various tasks.

**Interpretation**: Results are interpreted using EM, F1 scores, and IOU scores to gauge the effectiveness in answer and region predictions.

**Baseline Results**: Struggles in identifying supporting regions with the best model achieving only 11.44% in IOU.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
