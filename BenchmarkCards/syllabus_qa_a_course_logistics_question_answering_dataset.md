# SYLLABUS QA (A Course Logistics Question Answering Dataset)

## 📊 Benchmark Details

**Name**: SYLLABUS QA (A Course Logistics Question Answering Dataset)

**Overview**: We introduce SYLLABUS QA, an open-source dataset with 63 real course syllabi covering 36 majors, containing 5,078 open-ended course logistics-related question-answer pairs that are diverse in both question types and answer formats.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Similar Benchmarks**:
- FAIRYTALE QA
- QUAC
- NARRATIVE QA
- NEWSQA

**Resources**:
- [GitHub Repository](https://github.com/umass-ml4ed/SyllabusQACourse)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to provide a dataset for developing and evaluating automated question answering approaches for logistics-related questions in education.

**Target Audience**:
- ML Researchers
- Educators
- AI Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: 63 unique course syllabi collected from instructors across 12 universities worldwide.

**Size**: 5,078 question-answering pairs

**Format**: PDF

**Annotation**: Crowd annotated by over 200 annotators simulating logistics-related QA pairs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- LLM-based evaluation

**Metrics**:
- Fact-QA Precision
- Fact-QA Recall
- ROUGE-L F1
- BERTScore F1

**Calculation**: Metrics calculated by evaluating factual information overlap between annotator-written ground truth answers and model predictions.

**Interpretation**: Higher scores in Fact-QA metrics indicate accurate and relevant answers, while lower scores suggest hallucination or factual inaccuracies.

**Baseline Results**: Human performance on Fact-QA Precision is 0.707, Recall is 0.664.

**Validation**: Evaluated across various LLM models and compared against human performance metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Privacy**: Data privacy rights alignment

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: To ensure anonymity, personally identifiable information was removed from syllabi.

**Data Licensing**: CC BY-NC-SA (Attribution-NonCommercial-ShareAlike) License.

**Consent Procedures**: Explicit consent collected from all annotators.

**Compliance With Regulations**: Not Applicable
