# KILT (Knowledge Intensive Language Tasks)

## 📊 Benchmark Details

**Name**: KILT (Knowledge Intensive Language Tasks)

**Overview**: KILT is a benchmark for knowledge-intensive language tasks aimed at facilitating research on models that condition on specific knowledge from a single Wikipedia snapshot. It encompasses multiple tasks such as open-domain question answering and fact-checking, using a uniform interface and a common knowledge source to lower entry barriers for research.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SQuAD
- TriviaQA
- HotpotQA

**Resources**:
- [GitHub Repository](https://github.com/facebookresearch/KILT)
- [Resource](https://huggingface.co/datasets?search=kilt)

## 🎯 Purpose and Intended Users

**Goal**: To provide a unified benchmark for evaluating models on knowledge-intensive tasks leveraging a single Wikipedia snapshot and facilitating comparisons across a variety of NLP tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Fact Checking
- Open Domain Question Answering
- Entity Linking
- Slot Filling
- Dialogue

**Limitations**: N/A

## 💾 Data

**Source**: KILT provides a unified knowledge source based on a snapshot of Wikipedia taken on 2019/08/01 with 5.9M articles.

**Size**: 3.2M instances

**Format**: JSONL

**Annotation**: Annotated via Amazon Mechanical Turk to increase provenance coverage.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Retrieval evaluation

**Metrics**:
- Accuracy
- Exact Match (EM)
- ROUGE-L
- F1 Score

**Calculation**: Metrics are calculated based on system outputs compared to ground truth, considering both accuracy and the ability to provide provenance.

**Interpretation**: Higher scores indicate better performance on the tasks performed, especially with regard to the quality of provenance provided.

**Baseline Results**: Comparative results across various models including BART, T5, RAG, and BERT with DPR.

**Validation**: Models are validated using predefined evaluation sets, ensuring that knowledge used is from the designated Wikipedia snapshot.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
