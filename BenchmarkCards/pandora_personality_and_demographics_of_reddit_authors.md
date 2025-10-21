# PANDORA (Personality ANd Demographics Of Reddit Authors)

## 📊 Benchmark Details

**Name**: PANDORA (Personality ANd Demographics Of Reddit Authors)

**Overview**: PANDORA is the first dataset of Reddit comments of 10k+ users partially labeled with three personality models (Big 5, MBTI, Enneagram) and demographics (age, gender, and location). It comprises over 17M comments (17,640,062 comments) written by 10,288 users, including 1,608 users with Big 5 labels, and is made available to the research community for computational sociolinguistics and NLP research.

**Data Type**: text (Reddit comments; user-level comment collections)

**Domains**:
- Natural Language Processing
- Computational Sociolinguistics
- Social Sciences

**Languages**:
- English
- Spanish
- French
- Italian
- German
- Portuguese
- Dutch
- Esperanto
- Swedish
- Polish

**Similar Benchmarks**:
- MBTI9k
- MyPersonality

**Resources**:
- [Resource](https://psy.takelab.fer.hr)

## 🎯 Purpose and Intended Users

**Goal**: Introduce PANDORA, a Reddit dataset labeled with personality (Big 5, MBTI, Enneagram) and demographic (age, gender, location, language) variables to support sociolinguistic research and development/evaluation of NLP models for personality and demographic prediction.

**Target Audience**:
- Computational Sociolinguistics Researchers
- Natural Language Processing Researchers
- Social Science Researchers
- Model Developers

**Tasks**:
- Text-based Personality Prediction
- Age Prediction (Regression)
- Gender Classification (Text Classification)
- Region/Geolocation Classification
- MBTI/Enneagram Classification
- Author Profiling

**Limitations**: Dataset may not be representative of Reddit users or the general population due to selection biases; Big 5 labels are limited in number (1,608 users); distributions of MBTI types are skewed (four MBTI types account for 75% of users); normalization of Big 5 scores required dealing with heterogeneous test formats.

## 💾 Data

**Source**: Reddit comments retrieved via the Pushshift Reddit dataset; MBTI labels adopted from MBTI9k (extracted from flairs using regular expressions); Enneagram labels manually labeled from flairs; Big 5 labels extracted from comments reporting online test results (from various online tests such as Truity and HEXACO) using a semi-automatic approach (candidate retrieval, regex-based extraction per test, manual verification, and a test-identification classifier).

**Size**: 17,640,062 comments written by 10,288 users; 1,608 users with Big 5 labels; 9,084 users reported MBTI; 793 users reported Enneagram.

**Format**: N/A

**Annotation**: MBTI: extracted from user flairs using regular expressions (from MBTI9k). Enneagram: manually labeled from flairs. Big 5: semi-automatic extraction from comments (retrieve candidate comments, identify test via links or a trained test-identification classifier, use regex per test to extract scores, manual verification for extracted scores, normalization to 0–100 percentiles). Demographics (age, gender, location): manually inspected and normalized from flairs and self-reports in comments.

## 🔬 Methodology

**Methods**:
- Semi-automatic data extraction with manual verification
- Regular expressions for flair-based label extraction
- Train a test-identification classifier (character n-grams) for Big 5 reports
- Domain adaptation (Daumé III, 2007) to transfer MBTI/Enneagram to Big 5
- Machine learning benchmarks: Logistic Regression and Neural Networks (BERT-based comment encodings)
- 5-fold cross-validation with stratified splits
- 80/20 train-test split for the gender classifier
- Hierarchical regression analysis for sociolinguistic study
- Bias analysis using statistical tests (two-proportion Z-test, Kruskal-Wallis H-test)

**Metrics**:
- Macro-averaged F1 Score
- F1-macro
- Accuracy
- Pearson correlation coefficient
- F1-macro (test-identification classifier)

**Calculation**: Classification metrics (macro-averaged F1, accuracy) and regression metric (Pearson correlation) computed using 5-fold cross-validation with stratified splits for each target; gender classifier used an 80%–20% train-test split; test-identification classifier performance reported as F1-macro on held-out data; regression F-tests used for feature selection; hyperparameters optimized on held-out data per fold.

**Interpretation**: Higher macro-averaged F1 and higher Pearson correlation indicate better model performance; performance for logistic regression models plateaus at around 1,000 comments per user; authors note poor performance of deep learning baselines relative to logistic regression on n-gram features.

**Baseline Results**: Logistic Regression (LR) with N-grams: Introverted F1-macro 0.649, Intuitive 0.599, Thinking 0.730, Perceiving 0.626; Enneagram F1-macro 0.155 (varied with features); Gender classification accuracy/F1: accuracy ~89.9% (test), LR gender F1-macro 0.889; Region classification LR F1-macro 0.206. Regression (Pearson correlation) results with LR (N-grams): Agreeableness 0.181, Openness 0.235, Conscientiousness 0.194, Neuroticism 0.194, Extraversion 0.271, Age 0.704. Test-identification classifier (for Big 5 reports) reached F1-macro 81.4% on held-out data.

**Validation**: 5-fold cross-validation with stratified splits for each target was used; regression F-tests for feature selection; hyperparameters optimized on held-out development data per fold; manual verification of extracted Big 5 scores (about 80% extracted correctly automatically, remaining 20% extracted manually); test-identification classifier validated on held-out data (F1-macro 81.4%).

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Privacy**: Personal information in data, Data privacy rights alignment
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: The paper includes demographic breakdowns (age, gender, location, language) and analyzes biases across groups (e.g., gender classification errors differ by personality traits; geographical distributions in Table 9; language distributions in Table 10).

**Potential Harm**: ['Societal biases in model predictions (bias in gender classification traced to psycho-demographic variables)', 'Misinterpretation or misuse due to non-representative dataset']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Authors follow ethical code for archival psychological research; use public Reddit comments exposed via API; users may request content removal and such requests are removed (future requests will be handled and escalated to Reddit); the study was approved by an academic IRB.

**Data Licensing**: Not Applicable

**Consent Procedures**: Authors note that per Reddit User Agreement users consent to public availability of their comments; the authors rely on archival research norms and IRB approval rather than individual informed consent for each participant.

**Compliance With Regulations**: Study approved by an academic IRB; data collection and use described as following Reddit User Agreement; no explicit mention of GDPR or CCPA compliance in the paper.
