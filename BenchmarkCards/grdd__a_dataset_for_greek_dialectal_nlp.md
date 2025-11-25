# GRDD: A Dataset for Greek Dialectal NLP

## 📊 Benchmark Details

**Name**: GRDD: A Dataset for Greek Dialectal NLP

**Overview**: We present a dataset for the computational study of a number of Modern Greek dialects. It consists of raw text data from four dialects of Modern Greek, Cretan, Pontic, Northern Greek and Cypriot Greek. The dataset is of considerable size, albeit imbalanced, and presents the first attempt to create large scale dialectal resources of this type for Modern Greek dialects. The dataset is then used for a dialect identification task using traditional ML algorithms and simple DL architectures.

**Data Type**: text (raw dialectal text lines; CSV with text and dialect label)

**Domains**:
- Natural Language Processing
- Computational Linguistics

**Languages**:
- Modern Greek

**Similar Benchmarks**:
- Multi-CAST
- Griko (parallel Griko-Italian resource)

**Resources**:
- [GitHub Repository](https://github.com/StergiosCha/Greek_dialect_corpus)
- [Resource](https://arxiv.org/abs/2308.00802)

## 🎯 Purpose and Intended Users

**Goal**: To collect and present a large-scale dataset of Modern Greek dialectal data (Cypriot Greek, Pontic Greek, Cretan Greek, Northern Greek, plus Standard Modern Greek) for computational study, and to use it for a Dialect Identification task.

**Target Audience**:
- Natural Language Processing researchers
- Computational Linguistics researchers

**Tasks**:
- Dialect Identification
- Dialectal NLP tasks

**Limitations**: Imbalanced dataset sizes across dialects; coarse-grained categories collapsing sub-varieties, genres and registers; some errors due to insufficient data cleaning; dataset composition varies by dialect (e.g., blogs for Cypriot, translations and musical declamations for Cretan).

## 💾 Data

**Source**: Freely available web data identified and collected by native speakers and knowledgeable contributors: blogs, websites, online forums, social media platforms, blog posts, freely available literary texts, translations, song lyrics and other online materials. URLs were identified by working groups and text was extracted with Python scripts.

**Size**: Standard Modern Greek: 6.5m words; Cypriot Greek: 2.3m words; Cretan Greek: 880k words; Pontic Greek: 282k words; Northern Greek: 35k words.

**Format**: CSV (two columns: text and dialect label). Data initially extracted as raw text and lightly pre-processed (empty lines removed, character uniformity command, special characters removed, duplicate lines removed, punctuation and extra white spaces removed).

**Annotation**: Dialect labels derived from source grouping; human validation: random sample of 10,000 lines per dialect rated by native speakers on a scale from 1 to 10 (reported average scores per dialect).

## 🔬 Methodology

**Methods**:
- Classical Machine Learning (Ridge classifier, Naive Bayes, Support Vector Machine) using word-gram language models (1-gram and 3-gram)
- Deep Learning (vanilla BiLSTM with embedding and two BiLSTM layers)
- k-fold cross-validation
- Error analysis by sampling misclassified examples
- Human validation of random samples by native speakers

**Metrics**:
- Accuracy
- Loss
- Average native speaker rating (1-10)

**Calculation**: Accuracy and loss reported for models on the full imbalanced dataset and on balanced subsets (5k, 20k, 80k lines per dialect). k-fold validation was used to assess generalization. Exact formulae for metrics are not specified beyond reported numeric values.

**Interpretation**: High Accuracy values (even for simple ML models) indicate the dialects exhibit distinctive characteristics allowing classification. The BiLSTM yields the highest reported accuracy. A portion of classification errors is due to insufficient dataset cleaning and the coarse-grained nature of the dataset.

**Baseline Results**: Classical ML on full dataset: Ridge classifier 0.91 Accuracy; Naive Bayes 0.92 Accuracy; SVM 0.91 Accuracy. Balanced subsets (top-three algorithms): 5k lines: Ridge 0.76, NB 0.76, SVC 0.75; 20k lines: Ridge 0.82, NB 0.81, SVC 0.82; 80k lines: Ridge 0.89, NB 0.90, SVC 0.88. BiLSTM on full dataset: Accuracy 0.97, Loss 0.1; k-fold validation: Accuracy 0.935, Loss 0.17. BiLSTM on balanced sets: 5k Accuracy 0.89 Loss 0.5 (k-fold 0.9/0.32); 20k Accuracy 0.928 Loss 0.21 (k-fold 0.922/0.2); 80k Accuracy 0.94 Loss 0.15 (k-fold 0.936/0.18).

**Validation**: Human validation: random sample of 10,000 lines per dialect rated by native speakers (average scores reported). Model validation: k-fold cross-validation performed for BiLSTM and balanced subsets; comparisons between full dataset and balanced subsets used to evaluate impact of imbalance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
