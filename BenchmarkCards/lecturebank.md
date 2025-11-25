# LectureBank

## 📊 Benchmark Details

**Name**: LectureBank

**Overview**: We introduce LectureBank, a dataset containing 1,352 English lecture files collected from university courses which are each classified according to an existing taxonomy as well as 208 manually-labeled prerequisite relation topics, which is publicly available. The dataset will be useful for educational purposes such as lecture preparation and organization as well as applications such as reading list generation.

**Data Type**: text (lecture slide files / extracted slide text)

**Domains**:
- Natural Language Processing
- Machine Learning
- Artificial Intelligence
- Deep Learning
- Information Retrieval

**Languages**:
- English

**Similar Benchmarks**:
- TutorialBank
- ACL Anthology

**Resources**:
- [GitHub Repository](https://github.com/Yale-LILY/LectureBanknew)
- [Resource](https://arxiv.org/abs/1811.12181)

## 🎯 Purpose and Intended Users

**Goal**: To answer the question of "what should one learn first," by applying an embedding-based method to learn prerequisite relations for course concepts in the domain of NLP and to provide a lecture-slide corpus (LectureBank) annotated for taxonomy labels and prerequisite relations.

**Target Audience**:
- Students (educational users)
- Entry-level researchers
- NLP Engineers
- Educators

**Tasks**:
- Prerequisite Relation Learning
- Link Prediction
- Topic Classification
- Topic Modeling

**Limitations**: For copyright reasons, we are releasing only the links to the individual lectures. The annotations may be subjective (e.g., how to treat "long dependencies"); annotators were directed to refer to standard university curricula for unclear pairs. The dataset has a topical bias toward deep learning and recent work, reflecting available resources.

## 💾 Data

**Source**: Manually collected online lecture files (PDF/PPT) from 60 university-level courses covering five domains (NLP, ML, AI, Deep Learning, Information Retrieval). TutorialBank (Fabbri et al. 2018) was used as complementary training data and the list of 208 concepts for prerequisite annotation was taken from Fabbri et al. (2018).

**Size**: 1,352 lecture files (51,939 slides) from 60 courses; 3,443,076 tokens; vocabulary of 1,221 terms; 208 concept vertices with 921 labeled prerequisite edges.

**Format**: Original lecture files (PDF or PPT); text extracted using PDFMiner and python-pptx. Annotations provided as labeled prerequisite relation pairs (binary) and taxonomy labels for lecture files.

**Annotation**: Lecture files manually classified into the TutorialBank 305-topic taxonomy. Prerequisite relations: binary (yes/no) annotations by two PhD student annotators on 208 concepts; Cohen's kappa of 0.7; intersection of annotators' labels used to produce a directed concept graph with 921 edges.

## 🔬 Methodology

**Methods**:
- Embedding-based concept representation using Doc2Vec
- Binary classification (Naive Bayes, SVM with linear kernel, Logistic Regression, Random Forest)
- Graph Autoencoder (GAE)
- Variational Graph Autoencoder (VGAE)
- 5-fold cross-validation with oversampling

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: 5-fold cross-validation where the test set contains 10% of the positive prerequisite labels; an equal number of negative samples were added to the test set. The rest of the samples were used as training data. During each run, oversampling was applied on the training set. Reported scores are averages over 5 runs.

**Interpretation**: High recall is preferred for downstream tasks such as a search engine to ensure potential prerequisites are not missed; basic classifiers (e.g., SVM) tended to have higher precision and F1, while GAE/VGAE showed high recall and lower precision. Oversampling substantially improves classifier performance in this imbalanced setting.

**Baseline Results**: Table 4 results (Precision / Recall / F1) with Doc2Vec concept representations trained on three settings:
- TutorialBank: NB 0.761 / 0.453 / 0.567; SVM 0.832 / 0.703 / 0.761; LR 0.819 / 0.604 / 0.693; RF 0.871 / 0.459 / 0.599; GAE 0.634 / 0.884 / 0.725; VGAE 0.599 / 0.895 / 0.717
- LectureBank: NB 0.853 / 0.611 / 0.710; SVM 0.835 / 0.668 / 0.740; LR 0.840 / 0.640 / 0.724; RF 0.831 / 0.624 / 0.712; GAE 0.577 / 0.905 / 0.705; VGAE 0.545 / 0.921 / 0.684
- TutorialBank + LectureBank: NB 0.614 / 0.670 / 0.641; SVM 0.824 / 0.688 / 0.748; LR 0.794 / 0.613 / 0.690; RF 0.787 / 0.519 / 0.625; GAE 0.594 / 0.899 / 0.715; VGAE 0.578 / 0.916 / 0.708
Total labeled pairs before oversampling: 921 positive, 41,829 negative.

**Validation**: 5-fold cross-validation with test set selection ensuring 10% of positives in test; average scores over 5 runs. Inter-annotator agreement measured via Cohen's kappa of 0.7 for prerequisite annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Intellectual Property
- Transparency

**Atlas Risks**:
- **Fairness**: Data bias
- **Intellectual Property**: Data usage rights restrictions
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
