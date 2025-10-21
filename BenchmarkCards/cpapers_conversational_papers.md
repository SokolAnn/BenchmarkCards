# cPAPERS (Conversational Papers)

## 📊 Benchmark Details

**Name**: cPAPERS (Conversational Papers)

**Overview**: cPAPERS is a dataset of conversational question-answer pairs from reviews of academic papers grounded in various components such as equations, figures, and tables. The dataset aims to support the development of conversational assistants capable of situated and multimodal interactive conversations over scientific documents.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/avalab/cPAPERS)

## 🎯 Purpose and Intended Users

**Goal**: To advance the development of conversational assistants capable of situated and multimodal interactive conversation within scientific papers.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: The key limitation of this dataset is the presence of mismatched figures, tables, or equations across different versions of the manuscripts.

## 💾 Data

**Source**: The cPAPERS dataset is sourced from official reviews and rebuttals of academic papers available on OpenReview and their associated LATEX source files from arXiv.

**Size**: 5,030 question-answer pairs

**Format**: JSON

**Annotation**: Annotations are conducted via automated processes utilizing LLMs combined with crowdsourced feedback from Amazon Mechanical Turk.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- ROUGE-1
- ROUGE-2
- ROUGE-L
- METEOR
- BERTScore

**Calculation**: Metrics are calculated based on the generated responses compared to reference answers in the dataset.

**Interpretation**: Higher scores indicate better performance in the model's ability to generate relevant and accurate replies to questions.

**Baseline Results**: Results from initial evaluations showed improvements using neighboring context in question-answering tasks.

**Validation**: The dataset underwent evaluation using various metrics to validate the performance of baseline models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: The dataset aims to prevent harm by ensuring that the extracted question-answer pairs are relevant and technical in nature.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: cPAPERS dataset is released under GNU Public License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
