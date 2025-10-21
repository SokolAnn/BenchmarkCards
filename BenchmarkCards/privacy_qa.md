# PRIVACY QA

## 📊 Benchmark Details

**Name**: PRIVACY QA

**Overview**: We present PRIVACY QA, a corpus consisting of 1750 questions about the privacy policies of mobile applications, and over 3500 expert annotations of relevant answers. The goal of this effort is to kickstart the development of question-answering methods for this domain and to shed light on challenges to question answerability.

**Data Type**: question-answering pairs (questions paired with evidence sentences from privacy policy documents)

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- English

**Similar Benchmarks**:
- PolisisQA
- NarrativeQA
- InsuranceQA
- TriviaQA
- SQuAD 1.0
- SQuAD 2.0
- MS Marco
- MC Test
- NewsQA

**Resources**:
- [GitHub Repository](https://github.com/AbhilashaRavichander/PrivacyQA_EMNLP)
- [Resource](https://arxiv.org/abs/1911.00841)

## 🎯 Purpose and Intended Users

**Goal**: Kickstart the development of question-answering methods for the privacy-policy domain and to enable users to selectively explore privacy issues salient to them.

**Target Audience**:
- Natural Language Processing researchers
- Privacy researchers and practitioners
- Model developers
- General public (as end users of privacy assistants) 

**Tasks**:
- Question Answering
- Answer Sentence Selection
- Answerability Identification (binary classification)

**Limitations**: All privacy policies in this corpus are in English. The corpus contains privacy policies collected from 35 mobile applications and was collected before April 1, 2018 (predating many GDPR-focused updates). Crowdworkers were recruited from the United States and had "master" status on Amazon Mechanical Turk.

## 💾 Data

**Source**: Privacy policies collected from 35 mobile applications from the Google Play Store (policies collected before April 1, 2018). Questions were elicited from crowdworkers on Amazon Mechanical Turk; answers and evidence selection were provided by seven experts with legal training.

**Size**: # Questions: 1,750 questions; # Policies: 35 policies; # Sentences: 4,947 sentences; # Annotations: over 3,500 expert annotations. Training/Test split: 1,350 training questions (27 policies) and 400 test questions (8 policies).

**Format**: N/A

**Annotation**: Manual annotation by legal experts (seven experts). Every question answered by at least one expert; every question in the test set answered by at least three experts. Experts identify relevant evidence sentences and provide meta-annotations (relevance, subjectivity, OPP-115 category, likelihood that a policy contains the answer).

## 🔬 Methodology

**Methods**:
- Automated metrics (sentence-level F1 evaluation for answer-sentence selection)
- Human evaluation (human performance baseline computed from annotator agreements)
- Model-based evaluation (baselines: SVM variants, CNN, BERT; binary answerability classification and extractive evidence identification)

**Metrics**:
- Sentence-level F1
- Precision
- Recall
- Accuracy
- F1 Score

**Calculation**: Sentence-level F1 implemented similar to Choi et al. (2018) and Rajpurkar et al. (2016). Precision and recall measure overlap between predicted sentences and sets of gold-reference sentences. The reported metric is the average of the maximum F1 from each n-1 subset in relation to the held-out reference.

**Interpretation**: Higher sentence-level F1 indicates better evidence identification. The best automatic baseline (BERT + Unanswerable) achieves 39.8 F1 on the corpus, the No-Answer baseline achieves 28.0 F1, and human performance is ~68.9 F1, indicating substantial headroom for improvement.

**Baseline Results**: Answer-sentence selection baselines (Table 6): No-Answer (NA) baseline: F1 = 28.0. Word Count baselines: varying F1s (top-2/top-3/top-5). BERT: Precision 44.2%, Recall 34.8%, F1 = 39.0. BERT + Unanswerable: Precision 44.3%, Recall 36.1%, F1 = 39.8. Human: Precision 68.8%, Recall 69.0%, F1 = 68.9. Answerability classification (Table 5) shows BERT achieves highest performance for binary answerability identification among tested baselines.

**Validation**: Dataset partitioned so documents in training and test splits are mutually exclusive (training: 27 applications, 1,350 questions; test: 8 applications, 400 questions). Each question in the test set has annotations from at least three experts to estimate annotation reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Crowdworkers recruited were located within the United States and had "master" status on Amazon Mechanical Turk. Expert annotators are legal experts. No further demographic breakdown is provided.

**Potential Harm**: ['Information misuse (explicitly discussed as a privacy concern in the paper)', 'User privacy concerns arising from misunderstanding or lack of awareness of privacy policy content']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All privacy policies in this corpus are publicly available and in English. Crowdworkers consented to participate in the study.

**Data Licensing**: Not Applicable

**Consent Procedures**: Crowdworkers participating in question elicitation consented to participate; annotators and crowdworkers are acknowledged in the paper.

**Compliance With Regulations**: The corpus was collected before April 1, 2018, predating many companies' GDPR-focused updates; the paper notes this and leaves analysis of GDPR impacts to future work.
