# QReCC (Question Rewriting in Conversational Context)

## 📊 Benchmark Details

**Name**: QReCC (Question Rewriting in Conversational Context)

**Overview**: QReCC is a new dataset for open-domain conversational QA comprising 14,000 conversations with 80,000 question-answer pairs. It is designed to explore question rewriting in a conversational context, facilitating tasks related to passage retrieval and reading comprehension in conversational settings.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- QuAC
- CoQA
- CAsT

**Resources**:
- [GitHub Repository](https://github.com/apple/ml-qrecc)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale resource for developing and evaluating methods for end-to-end, open-domain conversational question answering.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering
- Question Rewriting
- Passage Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Human-annotated conversations from web searches, combined with passages from the Common Crawl and the Wayback Machine.

**Size**: 14,000 conversations, 80,000 question-answer pairs

**Format**: JSON

**Annotation**: Annotations were produced by human annotators who generated question rewrites and identified relevant web pages for answers.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Exact Match
- ROUGE

**Calculation**: Metrics were calculated based on the alignment of predicted answers with the ground truth answers found in the annotations.

**Interpretation**: Higher scores indicate better performance in retrieving relevant answers and generating accurate question rewrites.

**Baseline Results**: End-to-end QA model achieved an F1 score of 19.10 with a human upper bound of 75.45.

**Validation**: The dataset was evaluated through a systematic approach comparing various metrics to establish baselines.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
