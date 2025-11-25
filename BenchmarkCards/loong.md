# Loong

## 📊 Benchmark Details

**Name**: Loong

**Overview**: Loong is a novel long-context benchmark designed for evaluating long-context capabilities of large language models (LLMs) with a focus on realistic multi-document question answering scenarios, introducing new task categories and contextual variations.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- LongBench

**Resources**:
- [GitHub Repository](https://github.com/MozerWang/Loong)
- [GitHub Repository](https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/Loong)

## 🎯 Purpose and Intended Users

**Goal**: To assess the long-context modeling capabilities of LLMs in real-world scenarios across multiple documents and varied context lengths.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Spotlight Locating
- Comparison
- Clustering
- Chain of Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Documents were manually collected from official websites, including financial reports, legal cases, and academic papers.

**Size**: 1,600 instances

**Format**: N/A

**Annotation**: Annotations were performed manually by experts and further refined using GPT-4o.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Scores are calculated based on the evaluation of model outputs against the gold standard answers.

**Interpretation**: A high score indicates better overall performance of LLMs on long-context tasks.

**Baseline Results**: N/A

**Validation**: Extensive experiments validated with multiple models showing their performance across different tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
