# SustainableQA: A Comprehensive Question Answering Dataset for Corporate Sustainability and EU Taxonomy Reporting

## 📊 Benchmark Details

**Name**: SustainableQA: A Comprehensive Question Answering Dataset for Corporate Sustainability and EU Taxonomy Reporting

**Overview**: SustainableQA is a novel dataset and a scalable pipeline for generating a comprehensive QA dataset from corporate sustainability reports and annual reports, addressing the critical need for high-quality training and evaluation data in corporate sustainability and EU Taxonomy reporting.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/DataScienceUIBK/SustainableQA)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive QA dataset that enhances model performance in navigating corporate sustainability compliance data.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: 61 corporate reports from German and Austrian companies featuring dedicated sections on EU Taxonomy and ESG.

**Size**: 195,287 QA pairs

**Format**: N/A

**Annotation**: Hybrid span extraction pipeline combining fine-tuned Named Entity Recognition, rule-based methods, and LLM-driven refinement.

## 🔬 Methodology

**Methods**:
- Semantic passage classification
- Hybrid span extraction
- LLM-driven question generation

**Metrics**:
- Exact Match (EM)
- Precision
- Recall
- F1 Score
- BLEU Score
- ROUGE-L

**Calculation**: Metrics calculated using standard evaluation methods for question answering.

**Interpretation**: Higher scores indicate better model performance in extracting relevant information from sustainability reports.

**Validation**: Dataset validated using multiple prompting strategies across state-of-the-art language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
