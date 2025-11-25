# PSYSCAM

## 📊 Benchmark Details

**Name**: PSYSCAM

**Overview**: PSYSCAM is a benchmark designed to systematically capture and evaluate the psychological techniques employed in real-world scam incidents, addressing a critical gap in scam analysis by grounding psychological technique annotations in authentic scammer-victim interactions.

**Data Type**: scam reports

**Domains**:
- Cybersecurity

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/KiteFlyKid/PsyScam)

## 🎯 Purpose and Intended Users

**Goal**: To capture and evaluate psychological techniques in scams for enhancing detection and prevention strategies.

**Target Audience**:
- Cybersecurity Researchers
- ML Researchers
- Industry Practitioners

**Tasks**:
- PT Classification
- Scam Completion
- Scam Augmentation

**Limitations**: The taxonomy of psychological techniques may not fully encompass the entire psychological landscape in scams.

## 💾 Data

**Source**: Scam reports collected from six prominent scam reporting platforms.

**Size**: 16,658 reports

**Format**: N/A

**Annotation**: Annotated using a human-LLM collaborative framework.

## 🔬 Methodology

**Methods**:
- Human-Language Model collaborative annotation
- Machine Learning classification

**Metrics**:
- Accuracy
- Recall
- Precision
- F1 Score
- ROUGE
- BLEU
- BERTScore

**Calculation**: Metrics calculated as standard for classification tasks, involves performance assessments of models on benchmarking tasks.

**Interpretation**: Higher metrics indicate better performance in detecting and generating scam content.

**Validation**: Extensive experiments using various baseline models to validate benchmark effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All datasets are publicly accessible and do not violate any licenses.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
