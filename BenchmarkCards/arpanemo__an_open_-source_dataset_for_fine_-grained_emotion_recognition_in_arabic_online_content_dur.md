# ArPanEmo: An Open -Source Dataset for Fine -Grained Emotion Recognition in Arabic Online Content during COVID -19 Pandemic

## 📊 Benchmark Details

**Name**: ArPanEmo: An Open -Source Dataset for Fine -Grained Emotion Recognition in Arabic Online Content during COVID -19 Pandemic

**Overview**: Presents the ArPanEmo dataset, a novel dataset for fine-grained emotion recognition of online posts in Arabic. The dataset comprises 11,128 online posts manually labeled for ten emotion categories or neutral, focuses on the Saudi dialect and topics related to the COVID-19 pandemic, and was collected from Twitter, YouTube, and online newspaper comments between March 2020 and March 2022. The final dataset is formatted as CSV with three columns: post identifier, post text, and emotion label.

**Data Type**: text (online posts in CSV)

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- Arabic (Saudi Arabic dialect)

**Similar Benchmarks**:
- NRC Affect Intensity Lexicon (NRC-AIL)
- SemEval-2018 Task 1: Affect in Tweets

**Resources**:
- [Resource](https://data.mendeley.com/datasets/d9yy8w52ns)
- [Resource](https://www.tweepy.org/)
- [Resource](https://lxml.de/)
- [Resource](https://docs.python.org/3/library/urllib.html#module-urllib)
- [Resource](https://beautiful-soup-4.readthedocs.io/en/latest/)
- [Resource](https://developer.twitter.com/en/developer-terms/agreement-and-policy)
- [Resource](https://al-marsd.com/)

## 🎯 Purpose and Intended Users

**Goal**: To enrich Arabic NLP resources by providing a fine-grained emotion-annotated dataset of Arabic online posts (focused on the Saudi dialect and COVID-19 topics) to support the development of machine learning and deep learning tools for emotion recognition and systems that monitor online suspicious behaviors or mental health disorders.

**Target Audience**:
- Machine learning researchers
- Deep learning researchers
- Arabic Natural Language Processing researchers
- Developers of systems for monitoring online behavior and mental health

**Tasks**:
- Emotion Recognition
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Collected from Twitter (using Tweepy and Twitter API targeting users in Saudi Arabia), YouTube comments (using urllib and lxml), and online newspaper comments (using BeautifulSoup) between March 2020 and March 2022; data filtered initially with the Arabic translation of the NRC Affect Intensity Lexicon (NRC-AIL) and then manually annotated.

**Size**: 11,128 online posts; 223,008 tokens total; Training set: 8,901 examples; Test set: 2,227 examples.

**Format**: CSV (three columns: Number [Twitter ID or 0], Post [text], Label [emotion])

**Annotation**: Semi-automatic pipeline: lexicon-based filtering using the Arabic NRC Affect Intensity Lexicon to preselect emotion-related posts, followed by manual annotation. Final manual labeling: 80 college-educated Saudi native Arabic speakers; each post labeled by three annotators; majority vote used; posts with three different labels were neglected (290 posts); Fleiss' kappa for inter-annotator agreement = 0.71232.

## 🔬 Methodology

**Methods**:
- Semi-automatic lexicon-based filtering (NRC-AIL)
- Manual human annotation (three annotators per post; majority voting)
- Model-based evaluation: Support Vector Machine (SVM), Bidirectional Gated Recurrent Unit (BiGRU), BERT-based (AraBERTv0.2-Twitter-large) fine-tuning

**Metrics**:
- Accuracy
- Macro-average F1 Score
- Weighted-average F1 Score
- Precision
- Recall
- Fleiss' Kappa
- Percent Agreement

**Calculation**: Fleiss' kappa computed according to the standard formula (reported with standard error and 95% CI). Macro-average metrics compute per-class metrics then average equally across classes; weighted-average metrics weight class metrics by class support. Classification metrics (Accuracy, Precision, Recall, F1) computed on the defined test set (20% split).

**Interpretation**: Fleiss' kappa κ = 0.7123 interpreted per Landis and Koch as 'substantial agreement'. The BERT-based model achieved the best performance among tested models with a weighted-average F1-score of 0.67; comparable macro- and weighted-average metrics indicate a relatively balanced class distribution.

**Baseline Results**: BERT-based: Accuracy 0.67; Macro-average F1 0.66; Macro-average Precision 0.68; Macro-average Recall 0.67; Weighted-average F1 0.67; Weighted-average Precision 0.69; Weighted-average Recall 0.67. BiGRU: Accuracy 0.40; Macro-average F1 0.38; Macro-average Precision 0.44; Macro-average Recall 0.39; Weighted-average F1 0.40; Weighted-average Precision 0.48; Weighted-average Recall 0.39. SVM: Accuracy 0.58; Macro-average F1 0.55; Macro-average Precision 0.69; Macro-average Recall 0.52; Weighted-average F1 0.58; Weighted-average Precision 0.68; Weighted-average Recall 0.58.

**Validation**: Inter-annotator agreement measured using Fleiss' kappa (κ = 0.7123). Dataset split into training (80%) and test (20%) sets with stratification per domain (healthcare and Impacted Life Aspects) and per emotion category to balance distributions. Dataset validity further assessed by training and evaluating SVM, BiGRU, and BERT-based models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Data Laws

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Data Laws**: Data usage restrictions

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The ArPanEmo dataset is completely anonymized and does not contain any personally identifiable information. For the portion obtained from Twitter, only Tweet IDs and annotations are provided due to Twitter's Service Terms restricting distribution of tweet contents.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Complies with Twitter's Service Terms by distributing only Tweet IDs for Twitter-derived content; no other regulatory compliance (e.g., GDPR) is explicitly discussed.
