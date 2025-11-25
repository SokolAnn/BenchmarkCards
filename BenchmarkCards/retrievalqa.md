# RetrievalQA

## 📊 Benchmark Details

**Name**: RetrievalQA

**Overview**: RetrievalQA is a benchmark comprising 1,271 short-form questions designed to assess adaptive retrieval-augmented generation (ARAG) methods for open-domain question answering, focusing on new world and long-tail knowledge.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/hyintell/RetrievalQA)

## 🎯 Purpose and Intended Users

**Goal**: To assess the effectiveness of ARAG methods in open-domain question answering by ensuring questions cannot be answered using LLMs' parametric knowledge.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The dataset primarily focuses on short-form QA and does not assess long-form generation tasks.

## 💾 Data

**Source**: Collected from RealTimeQA, FreshQA, ToolQA, PopQA, and TriviaQA datasets.

**Size**: 1,271 questions

**Format**: N/A

**Annotation**: Questions filtered to ensure they cannot be answered without retrieval.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Retrieval accuracy
- Match accuracy

**Calculation**: Match accuracy measures if gold answers are included in the model predictions.

**Interpretation**: Higher retrieval accuracy indicates more effective methods.

**Validation**: Evaluated using various sizes of language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data is obtained from publicly available sources with no personally identifiable information.

**Data Licensing**: Data constructed using datasets that comply with licensing agreements.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Aligned with institutional, national, and global ethical standards.
