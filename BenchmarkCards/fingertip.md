# FingerTip

## 📊 Benchmark Details

**Name**: FingerTip

**Overview**: The FingerTip benchmark evaluates the proactive and personalized capabilities of mobile GUI agents through two tracks: proactive task suggestions based on environmental observations and user intents, and personalized task execution according to user action preferences.

**Data Type**: user interaction episodes

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- Chinese

**Similar Benchmarks**:
- AndroidLab
- AMEX
- AitW

**Resources**:
- [Resource](https://anonymous.4open.science/r/FingerTip-57B8)
- [Resource](https://www.kaggle.com/datasets/qinglongyang/fingertip-20k)

## 🎯 Purpose and Intended Users

**Goal**: To advance mobile GUI agents towards proactive task suggestion and personalized task execution.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Task Suggestion
- Task Execution

**Limitations**: The data collected is primarily from users in mainland China, which may not generalize to other regions. The study also highlights challenges related to data privacy and potential re-identification of users.

## 💾 Data

**Source**: User data collected through the FingerTip application

**Size**: 21,437 episodes

**Format**: JSON, XML, JPG

**Annotation**: Users provided demonstrations of interactions with Android apps based on real scenarios.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Success Rate (SR)
- Similarity Score (Sim)

**Calculation**: Success rates are calculated based on whether the predicted user intents match the actual intents. Similarity scores are computed using cosine similarity for text and Levenshtein distance for action sequences.

**Interpretation**: Higher success rates and similarity scores indicate better predictive accuracy of user intents and personalization of task execution.

**Validation**: The benchmark was validated using a train-validation-test split of the collected data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data, Data privacy rights alignment
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark includes demographic information from users, which is analyzed to understand differences in action sequences among different groups.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User data is anonymized, but there is a risk of re-identification due to unique patterns in interaction.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants signed a data usage agreement and were informed about data usage expectations.

**Compliance With Regulations**: Not Applicable
