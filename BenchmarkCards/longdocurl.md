# LongDocURL

## 📊 Benchmark Details

**Name**: LongDocURL

**Overview**: LongDocURL is a comprehensive benchmark integrating three primary tasks: Long Document Understanding, Numerical Reasoning, and Cross-Element Locating, comprising 20 sub-tasks and utilizing a dataset of 2,325 question-answering pairs covering more than 33,000 pages of documents.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- DocVQA
- MP-DocVQA
- DUDE

**Resources**:
- [GitHub Repository](https://github.com/dengc2023/LongDocURL)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating the document understanding capabilities of large vision language models (LVLMs) and to address the limitations of existing benchmarks in handling long documents and complex elements.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Document Understanding
- Numerical Reasoning
- Cross-Element Locating

**Limitations**: The types of documents in this benchmark are limited, and a broader range of data sources could enhance evaluation.

## 💾 Data

**Source**: Collection of over 396 documents crawled from CommonCrawl and other sources.

**Size**: 33,000 pages

**Format**: JSON

**Annotation**: Semi-automated pipeline with both automated and human verification phases.

## 🔬 Methodology

**Methods**:
- QA Generation
- Automated Verification
- Human Verification

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the correct answers extracted from the predicted responses.

**Interpretation**: A higher score indicates better performance in understanding and reasoning over document elements.

**Validation**: Comprehensive evaluation experiments conducted with 26 different configurations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Proper measures have been taken for data anonymity and user privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
