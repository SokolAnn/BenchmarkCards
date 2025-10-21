# SQuAD 2.0 (Stanford Question Answering Dataset)

## 📊 Benchmark Details

**Name**: SQuAD 2.0 (Stanford Question Answering Dataset)

**Overview**: SQuAD 2.0 combines existing SQuAD data with over 50,000 unanswerable questions written adversarially by crowdworkers so that systems must both answer questions when possible and determine when no answer is supported by the paragraph and abstain from answering.

**Data Type**: question-answering pairs (extractive, text)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- SQuAD 1.1
- TriviaQA
- NewsQA
- WikiQA
- MS MARCO
- RACE
- MCTest

**Resources**:
- [Resource](https://bit.ly/2rDHBgY)

## 🎯 Purpose and Intended Users

**Goal**: To create a challenging, diverse, and large-scale dataset that forces models to determine when a question cannot be answered given the context (i.e., to 'know what they don’t know') and to encourage development of reading comprehension systems that abstain when no answer is supported.

**Target Audience**:
- Machine Learning Researchers
- Model Developers

**Tasks**:
- Question Answering
- Reading Comprehension (Extractive)

**Limitations**: N/A

## 💾 Data

**Source**: Existing SQuAD 1.1 data combined with 53,775 new unanswerable questions written adversarially by crowdworkers on the Daemo platform; crowdworkers were asked to write questions referencing entities in the paragraph and to highlight a plausible answer span.

**Size**: Train: 130,319 examples (43,498 negative examples); Development: 11,873 examples (5,945 negative examples); Test: 8,862 examples (4,332 negative examples); 53,775 new unanswerable questions.

**Format**: N/A

**Annotation**: Crowdsourced via the Daemo platform: workers wrote unanswerable questions and highlighted plausible answer spans. For development and test sets, multiple human answers were collected and final answers selected by majority vote (average 4.8 answers per question).

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- Threshold tuning for abstention

**Metrics**:
- Exact Match
- F1 Score

**Calculation**: Following prior SQuAD work, report average Exact Match and F1 scores. For negative examples, abstaining receives a score of 1 and any other response receives 0 for both Exact Match and F1. Models tune an abstention threshold on the development set (threshold chosen to maximize F1 on dev) and use that threshold at test time.

**Interpretation**: Higher Exact Match and F1 scores indicate better performance; human F1 on SQuAD 2.0 is reported as 89.5% (test). A baseline that always abstains gets 48.9 test F1; strong models are much closer to the baseline than to human performance, indicating room for improvement.

**Baseline Results**: DocQA + ELMo: 66.3% F1 on SQuAD 2.0 test. Human: 89.5% F1 on SQuAD 2.0 test. Baseline that always abstains: 48.9% test F1. (Detailed EM and F1 scores for multiple models reported in Table 3 of the paper.)

**Validation**: Collected multiple human answers for each question in development and test sets and selected final answers by majority vote (avg 4.8 answers per question). Manual inspection of 100 randomly chosen negative examples found 93% were indeed unanswerable.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-SA 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
