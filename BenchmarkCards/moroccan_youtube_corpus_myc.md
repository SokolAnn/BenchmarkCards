# Moroccan YouTube Corpus (MYC)

## 📊 Benchmark Details

**Name**: Moroccan YouTube Corpus (MYC)

**Overview**: Creation of the largest public dataset for Moroccan dialect sentiment analysis that incorporates Moroccan dialect written in Arabic script and Latin letters; assembled a diverse collection of texts with 20,000 manually labeled Moroccan dialect comments and publicly available stop words lists; conducted a comparative study of multiple machine learning models and evaluated generalizability on other Moroccan datasets.

**Data Type**: text (YouTube comments, sentiment-labeled)

**Domains**:
- Natural Language Processing

**Languages**:
- Moroccan Arabic

**Similar Benchmarks**:
- Moroccan Sentiment Analysis Corpus (MSAC)
- MSTD: Moroccan sentiment twitter dataset
- Moroccan Arabic Corpus (MAC)
- Modeling, Simulation and Data Analysis Dataset
- AWATIF
- OCA
- ArSAS
- HARD

**Resources**:
- [GitHub Repository](https://github.com/MouadJb/MYC)

## 🎯 Purpose and Intended Users

**Goal**: Create the first and largest public dialect dataset for Moroccan sentiment analysis covering both Arabic script and Latin script, and identify machine learning models suited to this dataset while evaluating generalizability on other Moroccan datasets.

**Target Audience**:
- Researchers
- Practitioners

**Tasks**:
- Sentiment Analysis
- Text Classification

**Limitations**: Dataset and resources are susceptible to significant noise and inconsistency due to lack of standardized orthography, existence of subdialects, and script variation; emoji distribution in the dataset is biased (positive emojis exceed negative emojis).

## 💾 Data

**Source**: Comments extracted from YouTube channels using the YouTube API; manually selected 50 Moroccan YouTube channels of different topics; comments collected between 2018 and 2022; non-Moroccan-only foreign-language content removed.

**Size**: 20,000 annotated comments (10,000 positive, 10,000 negative); stop words lists contain more than 350 words.

**Format**: N/A

**Annotation**: Manual annotation by five native Moroccan dialect annotators (including two experts); voting technique requiring four out of five votes to determine comment polarity.

## 🔬 Methodology

**Methods**:
- Preprocessing experiments (data cleaning, tokenization, normalization, emoji treatment, stop-word removal, duplicate filtering)
- Feature extraction (TF-IDF, Word2vec embeddings trained on the dataset)
- Comparative model evaluation of supervised classifiers (SVM, Naïve Bayes, KNN) and deep learning models (CNN, LSTM)
- Cross-dataset testing on external Moroccan datasets (MSAC, MAC)

**Metrics**:
- Accuracy
- Precision
- Recall
- F-measure

**Calculation**: Metrics reported as percentages on test sets. For cross-dataset evaluation, 20% of each external dataset was used as the testing set.

**Interpretation**: Higher Accuracy/Precision/Recall/F-measure indicate better classifier performance; deep learning models (CNN, LSTM) achieved higher performance than classical models; preprocessing (stop-word removal, emoji deletion) improves performance.

**Baseline Results**: Selected reported results: (without preprocessing) CNN Accuracy 85%, LSTM 84%, SVM 73.5%, NB 71.5%, KNN 68.6%. (With preprocessing and emojis deleted) CNN Accuracy 92.4%, LSTM 87.2%, SVM 84.7%, NB 83.3%, KNN 75%. Cross-dataset testing: Our Model accuracy on MSAC 99, on MAC 95.

**Validation**: Annotation voting requiring 4/5 annotator agreement for labels; model generalizability evaluated by testing best model on 20% of external public Moroccan datasets (MSAC, MAC).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Data contamination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
