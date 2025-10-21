# BrowseComp-Plus

## 📊 Benchmark Details

**Name**: BrowseComp-Plus

**Overview**: BrowseComp-Plus is a benchmark designed for evaluating Deep-Research Agents with a fixed, curated corpus and human-verified supporting and challenging negative documents, allowing controlled experimentation and fair comparisons.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BrowseComp

**Resources**:
- [Resource](https://texttron.github.io/BrowseComp-Plus/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a fair and transparent evaluation framework for Deep-Research Agents, fostering insights into retrieval effectiveness and reasoning capabilities.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Curated corpus derived from the original BrowseComp dataset including human-verified supporting and challenging negative documents.

**Size**: 100,195 documents

**Format**: N/A

**Annotation**: Human-verified documentation with labeled supporting evidence.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Recall

**Calculation**: Metrics are calculated based on end-to-end effectiveness of deep research systems against ground truth using evaluation prompts.

**Interpretation**: Higher metrics indicate better performance of retrieval and integrated AI systems in providing accurate answers.

**Baseline Results**: Various open- and closed-source models are evaluated with different retrieval agents, showing a range of accuracies from 3.86% to 70.12%.

**Validation**: Comprehensive evaluations using human-verified documents and automated metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Reproducibility
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
