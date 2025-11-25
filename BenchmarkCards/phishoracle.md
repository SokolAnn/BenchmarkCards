# PhishOracle

## 📊 Benchmark Details

**Name**: PhishOracle

**Overview**: PhishOracle is a tool that generates adversarial phishing webpages by embedding diverse content-based and visual-based phishing features into legitimate webpages. It evaluates the robustness of existing phishing webpage detection models against these adversarial phishing webpages.

**Data Type**: webpage samples

**Domains**:
- Natural Language Processing
- Cyber Security

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/LetsBeSecure/PhishOracle-Project)
- [GitHub Repository](https://github.com/LetsBeSecure/PhishOracle-Webapp)

## 🎯 Purpose and Intended Users

**Goal**: To develop a tool that generates adversarial phishing webpages for evaluating the robustness of existing phishing detection models.

**Target Audience**:
- Cybersecurity Researchers
- Phishing Detection Model Developers

**Tasks**:
- Phishing Detection
- Adversarial Attack Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: The dataset includes 9,067 legitimate webpage screenshots which are manually labeled, as well as adversarial phishing webpages generated using PhishOracle.

**Size**: 9,067 legitimate webpage screenshots, multiple adversarial phishing webpage samples generated.

**Format**: N/A

**Annotation**: Manual labeling of identity logos on legitimate webpage screenshots.

## 🔬 Methodology

**Methods**:
- Automated metrics
- User study

**Metrics**:
- Precision
- Recall
- F1 Score
- Accuracy
- Mean Average Precision (MAP)

**Calculation**: Metrics calculated based on true positives, true negatives, false positives, and false negatives as outlined in the confusion matrix.

**Interpretation**: High precision indicates the model's ability to correctly identify legitimate webpages, while high recall signifies identifying most phishing webpages.

**Baseline Results**: Stack model achieves a precision of 98.61% and recall of 70.86% on adversarial phishing webpages.

**Validation**: The generated phishing webpages were validated by evaluating their performance against existing phishing detection models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Privacy**: Exposing personal information
- **Robustness**: Evasion attack
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential misuse in phishing activities']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
