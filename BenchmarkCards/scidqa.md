# SCIDQA

## 📊 Benchmark Details

**Name**: SCIDQA

**Overview**: SCIDQA is a new dataset for reading comprehension that challenges language models for a deep understanding of scientific articles, consisting of 2,937 question-answer pairs sourced from peer reviews and answers by paper authors.

**Data Type**: question-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- QASPER
- QASA
- PubMedQA

**Resources**:
- [GitHub Repository](https://github.com/yale-nlp/SciDQA)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research on complex scientific text understanding and to benchmark the performance of language models in comprehending scientific papers.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Peer reviews and author responses from scientific papers on OpenReview.

**Size**: 2,937 pairs

**Format**: JSON

**Annotation**: Manual annotation by domain experts and human revision processes.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- ROUGE score
- BLEURT-20
- BERTScore

**Calculation**: Metrics are calculated based on the similarity of model-generated answers to gold standard answers.

**Interpretation**: Higher scores indicate better performance in generating accurate and relevant responses.

**Baseline Results**: N/A

**Validation**: The dataset undergoes extensive human annotation and filtering for relevance and quality.

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
