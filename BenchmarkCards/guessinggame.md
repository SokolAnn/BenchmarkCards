# GuessingGame

## 📊 Benchmark Details

**Name**: GuessingGame

**Overview**: GuessingGame is a protocol for evaluating large language models (LLMs) as strategic question-askers in open-ended, open-domain settings. It involves a Guesser LLM identifying a hidden object by posing free-form questions to an Oracle LLM, measuring the performance based on the success rate and average number of questions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/cincynlp/GuessingGameLLMs)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate how effectively models gather information through questioning in an open-ended guessing game.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: Limited to evaluating question-asking behavior in the context of an object guessing game.

## 💾 Data

**Source**: An object corpus consisting of 858 distinct everyday objects.

**Size**: 858 objects

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Success Rate (SR)
- Average Number of Questions (ANQ)
- Information Gain (IG)

**Calculation**: Success Rate is calculated as the proportion of games in which the Guesser successfully identifies the target object. Average Number of Questions is calculated as the mean number of questions asked in successful games. Information Gain is estimated via a Bayesian belief-tracking method and an entropy-based method.

**Interpretation**: Higher success rates and lower average number of questions indicate more effective question-asking. Information Gain predicts task efficiency.

**Baseline Results**: LLaMA-3.3 70B achieved a success rate of 39.4% under open-ended questioning.

**Validation**: Validated via empirical evaluation across 858 games.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Enumeration leading to ineffective questioning.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
