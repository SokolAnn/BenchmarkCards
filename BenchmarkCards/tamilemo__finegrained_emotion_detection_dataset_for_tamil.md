# TamilEmo: Finegrained Emotion Detection Dataset for Tamil

## 📊 Benchmark Details

**Name**: TamilEmo: Finegrained Emotion Detection Dataset for Tamil

**Overview**: We introduce this labeled dataset (a largest manually annotated dataset of more than 42k Tamil YouTube comments, labeled for 31 emotions including neutral) for emotion recognition. The goal of this dataset is to improve emotion detection in multiple downstream tasks in Tamil.

**Data Type**: text (YouTube comments)

**Domains**:
- Natural Language Processing

**Languages**:
- Tamil

**Similar Benchmarks**:
- Empathetic Dialogues
- GoEmotions

**Resources**:
- [Resource](https://youtubecommentsdownloader.com/)
- [Resource](https://pypi.org/project/langdetect/)
- [Resource](https://pypi.org/project/pylev/)
- [Resource](https://www.nltk.org/)
- [Resource](http://www.cs.umass.edu/mccallum/mallet)
- [GitHub Repository](https://github.com/AshokR/TamilNLP/wiki/Stopwords)

## 🎯 Purpose and Intended Users

**Goal**: The goal of this dataset is to improve emotion detection in multiple downstream tasks in Tamil.

**Target Audience**:
- Researchers

**Tasks**:
- Emotion Detection
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: YouTube comments collected from Tamil movie trailers and teasers (monolingual Tamil comments).

**Size**: 42,686 comments

**Format**: N/A

**Annotation**: Manual annotation by volunteer annotators. Each comment was annotated by at least three annotators; if two annotators agreed the label was included, disagreements were resolved by a third annotator and, if needed, two additional annotators.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Baseline machine learning experiments (Logistic Regression, K-Nearest Neighbors, SVM, Decision Trees, Random Forest, Multinomial Naive Bayes)
- Pre-trained model fine-tuning (mBERT, MuRIL)

**Metrics**:
- Precision
- Recall
- F1 Score
- Macro average F1 Score
- Krippendorff's alpha

**Calculation**: Metrics are reported as macro average Precision, Recall, and F1-Score on the test set. Krippendorff's alpha was used to measure inter-annotator agreement (reported as 0.7452).

**Interpretation**: Higher macro average F1 indicates better overall performance. The authors state: "This shows that it is significantly hard for ML models to compare emotions in fine-grained settings."

**Baseline Results**: MuRIL-Base: 0.60 macro average F1 on the 3-class (sentiment) grouping. Random Forest: 0.42 macro average F1 on the 7-class grouping, and 0.29 macro average F1 on the full 31-class taxonomy. (Detailed per-model results reported in Tables 6-9 of the paper.)

**Validation**: Dataset split into Train (80%), Dev (10%), Test (10%). Dev and Test sets used for validation and evaluation. Inter-annotator agreement measured with Krippendorff's alpha = 0.7452.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: Annotator demographics: Language Tamil; Gender: Male 09, Female 07, Transgender 00; Higher Education: Undergraduate 12, Postgraduate 04; Medium of Schooling: English 09, Native language 07.

**Potential Harm**: ['Harmful comments towards religion', 'Harmful comments towards ethnicity', 'Harmful comments towards gender', 'Harmful comments towards sexual orientation', 'Harmful comments towards disability']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: To maintain data privacy, all user-related information was removed from the corpora.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
