# DebateSum

## 📊 Benchmark Details

**Name**: DebateSum

**Overview**: DebateSum is a large-scale argument mining and summarization dataset consisting of 187,386 unique pieces of evidence with corresponding arguments and extractive summaries. It was created using data compiled by competitors within the National Speech and Debate Association over a 7-year period, aiming to facilitate the automation of research work in competitive policy debate.

**Data Type**: argument-evidence-summary triplets

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Hellisotherpeople/DebateSum)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for argument mining and summarization in the context of competitive policy debate, enabling the development of natural language processing systems for assisting debaters.

**Target Audience**:
- ML Researchers
- Debate Competitors

**Tasks**:
- Summarization
- Argument Mining

**Limitations**: N/A

## 💾 Data

**Source**: Gathered from evidence produced during debate camps and competitions under the National Speech and Debate Association, leveraging the Open Evidence Project.

**Size**: 187,386 documents

**Format**: N/A

**Annotation**: Manually produced and annotated by competitors and coaches.

## 🔬 Methodology

**Methods**:
- Token classification
- Fine-tuning transformer models

**Metrics**:
- ROUGE

**Calculation**: Metrics are calculated based on the ROUGE score applied to the summaries generated compared to the ground truth summaries.

**Interpretation**: Higher ROUGE scores indicate better summarization quality, with models evaluated based on F1 scores.

**Validation**: The models were validated against a test split of 18,738 documents.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**
- **Accuracy**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution 4.0 International License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
