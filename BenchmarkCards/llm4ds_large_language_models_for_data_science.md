# LLM4DS (Large Language Models for Data Science)

## 📊 Benchmark Details

**Name**: LLM4DS (Large Language Models for Data Science)

**Overview**: This paper presents a controlled experiment that empirically assesses the performance of four leading LLM-based AI assistants on a diverse set of data science coding challenges sourced from the Stratacratch platform.

**Data Type**: Python coding problems

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- DS-1000

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.14064111)
- [Resource](https://www.stratascratch.com/)

## 🎯 Purpose and Intended Users

**Goal**: To empirically evaluate the effectiveness of LLMs in data science coding tasks across different problem types and difficulty levels.

**Target Audience**:
- ML Researchers
- Data Scientists
- AI Practitioners

**Tasks**:
- Code Generation
- Data Manipulation
- Data Visualization

**Limitations**: N/A

## 💾 Data

**Source**: Stratascratch platform, 100 Python coding problems

**Size**: 100 problems

**Format**: CSV

**Annotation**: Problems sourced from data science coding challenges, categorized by difficulty.

## 🔬 Methodology

**Methods**:
- Controlled experiment
- Hypothesis testing

**Metrics**:
- Success Rate
- Execution Time
- Graph Similarity Scores

**Calculation**: Metrics calculated based on the correctness of generated solutions and comparative analysis.

**Interpretation**: Success rates interpreted against baseline thresholds of 50%, 60%, and 70%.

**Baseline Results**: ChatGPT: 72%, Claude: 70%, Perplexity: 66%, Copilot: 60%

**Validation**: Validated through statistical hypothesis testing including Friedman and Wilcoxon tests.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
