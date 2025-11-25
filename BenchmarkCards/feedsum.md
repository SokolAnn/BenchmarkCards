# FeedSum

## 📊 Benchmark Details

**Name**: FeedSum

**Overview**: FeedSum is a large-scale dataset containing multi-dimensional LLM feedback on summaries of varying quality across diverse domains, focusing on improving summary quality by aligning summaries with human preferences for faithfulness, completeness, and conciseness.

**Data Type**: document-summary pairs with multi-dimensional feedback

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- UniSumEval
- SynFacEdit

**Resources**:
- [Resource](https://huggingface.co/datasets/DISLab/FeedSum)
- [Resource](https://huggingface.co/DISLab/SummLlama3-8B)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of FeedSum is to leverage LLM-generated feedback to improve text summarization by aligning summaries with human preferences regarding faithfulness, completeness, and conciseness.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Generated through LLMs using diverse input documents from 7 different domains, producing summaries with varying quality based on feedback from multiple models.

**Size**: 125,000 document-summary pairs

**Format**: JSON

**Annotation**: Generated feedback by LLMs on the quality of summaries.

## 🔬 Methodology

**Methods**:
- Automated evaluation
- Human evaluation

**Metrics**:
- Faithfulness
- Completeness
- Conciseness

**Calculation**: Scores are calculated based on the proportion of factual sentences, including key-facts and relevant sentence alignment in summaries.

**Interpretation**: Higher scores indicate better alignment with human preferences in summary quality; a score close to 1 signifies nearly perfect alignment.

**Validation**: Evaluated through both human assessments and automated metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
