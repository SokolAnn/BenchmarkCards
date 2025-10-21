# BD-SHS: A Benchmark Dataset for Learning to Detect Online Bangla Hate Speech in Different Social Contexts

## 📊 Benchmark Details

**Name**: BD-SHS: A Benchmark Dataset for Learning to Detect Online Bangla Hate Speech in Different Social Contexts

**Overview**: A large manually labeled Bangla hate speech dataset (BD-SHS) of 50,281 comments crawled from social media and online streaming sites, annotated with a three-level hierarchical scheme (Level 1: Hate Speech identification; Level 2: Target identification; Level 3: Hate Speech type categorization). The dataset contains 24,156 comments labeled as hate speech and is intended to support training and benchmarking of hate speech detection models in different social contexts.

**Data Type**: text (social media and online streaming comment texts)

**Domains**:
- Natural Language Processing
- Social Media

**Languages**:
- Bangla

**Similar Benchmarks**:
- OffensEval (SemEval-2019 Task 6)

**Resources**:
- [GitHub Repository](https://github.com/naurosromim/hate-speech-dataset-for-Bengali-social-media)
- [Resource](https://hatespeechdata.com/)
- [GitHub Repository](https://github.com/strohne/Facepager)
- [Resource](https://www.statista.com/statistics/268136/top-15-countries-based-on-number-of-facebook-users/)
- [Resource](https://www.statista.com/forecasts/1146236/youtube-users-in-bangladesh)
- [Resource](https://www.wikipedia.org/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large, linguistically diverse, manually annotated Bangla hate speech dataset covering multiple social contexts and a three-level hierarchical annotation scheme to support development and benchmarking of hate speech detection models.

**Target Audience**:
- Machine Learning Researchers
- Model Developers
- Social Media Safety Analysts

**Tasks**:
- Hate Speech Identification (Binary Classification)
- Hate Speech Target Identification (Multi-label Classification)
- Hate Speech Type Categorization (Multi-label Classification)

**Limitations**: Level 2 and Level 3 annotations were performed by a single annotator per comment in the current dataset; annotators had conflicting annotations at Level 1 even with detailed guidelines; dataset contains noisy text (mixed dialects, spelling and grammatical errors, unfinished sentences); class distributions for some labels are imbalanced (e.g., slander disproportionately more frequent).

## 💾 Data

**Source**: Comments crawled from comment sections of social media and online streaming platforms (Facebook, YouTube, Bangla TikTok and similar video comment sections) using Facepager and keyword-based searches of contentious topics since 2017; duplicates removed using Jaccard index filtering.

**Size**: 50,281 comments (24,156 labeled as Hate Speech); initially collected >100,000 comments before deduplication

**Format**: N/A

**Annotation**: Manual annotation by 50 undergraduate annotators (32 males, 18 females). Level 1: each comment annotated by three annotators with majority vote; inter-annotator agreement (Fleiss Kappa) for Level 1 = 0.658. Level 2 and Level 3: treated as multi-label; in current dataset each comment for Levels 2 and 3 was annotated by a single annotator. Annotators received a 3-hour training session and a detailed hierarchical annotation guideline.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (training classifiers: linear SVM, Bi-LSTM)
- Automated metrics (Precision, Recall, F1, weighted average F1)
- Train/validation/test split (70% / 15% / 15%)

**Metrics**:
- Precision
- Recall
- F1 Score
- Weighted Average F1
- Fleiss Kappa (inter-annotator agreement)

**Calculation**: Standard Precision, Recall and F1-score calculations. For multi-class/multi-label tasks the weighted average of scores is reported. Dataset split into train (70%), validation (15%), and test (15%); hyperparameters tuned on validation set.

**Interpretation**: Higher Precision/Recall/F1 indicate better classifier performance. The paper highlights F1 (and weighted average F1 for imbalanced tasks) as primary performance indicators and reports that embeddings trained on informal social media text (IFT) consistently outperform formal-text pretrained embeddings for these tasks.

**Baseline Results**: Task A (Hate Speech Identification): BiLSTM + IFT achieved F1 = 91.0%. Task B (Target Identification): BiLSTM + IFT achieved weighted average F1 = 77.5%. Task C (HS Type Categorization): SVM + char-ngrams achieved weighted average F1 = 89.1% (BiLSTM + IFT achieved 88.9%).

**Validation**: Dataset split into train/validation/test (70/15/15). Hyperparameters tuned on validation set. Inter-annotator agreement for Level 1 measured using Fleiss Kappa = 0.658. Duplicate/highly similar comments removed using Jaccard Index cutoff of 0.8.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Accuracy
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: The paper reports distributional analyses showing that females are disproportionately targeted on the basis of gender; tables provide breakdowns of HS targets (Individual, Male, Female, Group) and HS types across these targets.

**Potential Harm**: ['Cyberbullying', 'Aggression identification (calls to violence)', 'Marginalization of individuals and groups based on protected attributes']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All commentators' names, affiliations, and other identifying information were excluded from the dataset to ensure anonymity.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
