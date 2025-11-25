# The Children’s Book Test (CBT)

## 📊 Benchmark Details

**Name**: The Children’s Book Test (CBT)

**Overview**: A new test of how well language models capture meaning in children’s books by distinguishing the task of predicting syntactic function words from predicting lower-frequency words that carry greater semantic content. Each example consists of 20 context sentences and a 21st query sentence with one missing word; models must select the correct word from 10 candidate answers drawn from the context and query.

**Data Type**: cloze-style question-answering pairs (context + query with one missing word and 10 candidate answers)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Microsoft Research Sentence Completion Challenge (MSRCC)
- CNN/Daily Mail (CNN QA)
- MCTest

**Resources**:
- [Resource](https://www.gutenberg.org/)
- [Resource](http://fb.ai/babi/)
- [GitHub Repository](https://github.com/facebook/MemNN)
- [Resource](http://arxiv.org/abs/1506.03340)

## 🎯 Purpose and Intended Users

**Goal**: To measure how well language models can exploit wider linguistic context to make predictions about different types of missing words in children’s stories, separating prediction of syntactic function words from semantically informative terms.

**Target Audience**:
- Machine Learning Researchers
- Model Developers

**Tasks**:
- Language Modeling
- Question Answering
- Machine Reading / Reading Comprehension

**Limitations**: N/A

## 💾 Data

**Source**: Children's books from Project Gutenberg; examples formed from 21 consecutive sentences (first 20 sentences as context, 21st sentence as query with one missing word); candidate answers selected from words appearing in the context and query with candidate selection algorithm provided with the dataset.

**Size**: 669,343 training questions; 8,000 validation questions; 10,000 test questions; 98 training books; 5 validation books; 5 test books; vocabulary size 53,628; distinct candidates: 37,242 (train), 5,485 (validation), 7,108 (test); average words in contexts ~465 (train), ~435 (validation), ~445 (test); average words in queries ~31 (train), ~27 (validation), ~29 (test).

**Format**: N/A

**Annotation**: Automatically annotated with part-of-speech tags and named-entity labels using the Stanford CoreNLP Toolkit; candidate selection and question construction performed algorithmically; human annotations were collected for a human performance evaluation (15 native English speakers) on a sampled subset.

## 🔬 Methodology

**Methods**:
- Automated metrics (model accuracy on multiple-choice cloze questions)
- Human evaluation
- Model comparison (evaluation of multiple baseline and neural architectures)

**Metrics**:
- Accuracy

**Calculation**: Accuracy is computed as the proportion of questions for which the model-selected candidate (arg max over the 10 candidates) equals the true answer. Human performance measured as proportion correct on a sampled subset (10% of test set for humans).

**Interpretation**: Higher accuracy indicates better exploitation of wider context and greater semantic coherence in predicting content-bearing words; differences in accuracy across word classes (Named Entities, Common Nouns, Verbs, Prepositions) indicate whether models capture semantic vs. syntactic information.

**Baseline Results**: Selected results on CBT test set: Humans (Context+Query) - Named Entities 0.816, Common Nouns 0.816, Verbs 0.828, Prepositions 0.708. Best reported model on CBT: Memory Network (Window memory + self-supervision) - Named Entities 0.666, Common Nouns 0.630, Verbs 0.690, Prepositions 0.703. On CNN QA, Memory Network (Window memory + self-supervision + ensemble + exclude co-occurrences) - Test 0.694.

**Validation**: Hyperparameters tuned via grid search on the validation set; held-out test set used for final evaluation; ablation studies and anonymization experiments conducted (reported in appendices).

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Entities are not anonymised in the CBT (unlike the CNN QA dataset); the paper includes experiments analyzing the effects of anonymising entities on performance (Appendix D).

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
