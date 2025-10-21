# ChartCheck

## 📊 Benchmark Details

**Name**: ChartCheck

**Overview**: ChartCheck is the first large-scale dataset for explainable fact-checking against real-world charts, consisting of 1.7k charts and 10.5k human-written claims and explanations. It provides explanations as justifications for claim verification.

**Data Type**: chart-image and text pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ChartFC

**Resources**:
- [GitHub Repository](https://github.com/mubasharaak/ChartCheck)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for explainable fact-checking against data visualizations, enabling the evaluation and development of models for chart reasoning and claim verification.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Fact Checking
- Explainability

**Limitations**: The dataset is limited to English-only charts and excludes certain types of visualizations such as heat maps and scatter plots.

## 💾 Data

**Source**: Wikimedia Commons

**Size**: 1,683 charts and 10,480 claims and explanations

**Format**: JSON

**Annotation**: Crowdsourced from annotators with expert verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Crowdsourced annotation

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- ROUGE

**Calculation**: Model performance is measured by accuracy and F1 score for claim classification and BLEU/ROUGE for explanation generation.

**Interpretation**: Higher accuracy indicates better performance in predicting claim veracity, while higher BLEU/ROUGE scores reflect better explanation quality.

**Baseline Results**: The best-performing model achieves 73.8% accuracy, which lags far behind human performance of 95.7%.

**Validation**: The collected data was validated through multiple crowdsourcing tasks and expert checks to ensure quality and accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Transparency
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency
- **Robustness**: Data poisoning

**Demographic Analysis**: Analysis of demographic factors is not explicitly conducted in the dataset.

**Potential Harm**: ['Potential for misuse of fact-checking models in misinformation contexts.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All annotators were informed about data collection and its purpose, with options to withdraw.

**Data Licensing**: Data is intended for research purposes only, with no statements made regarding the truthfulness of claims in real-world contexts.

**Consent Procedures**: Ethical clearance was obtained prior to crowdsourcing.

**Compliance With Regulations**: Not Applicable
