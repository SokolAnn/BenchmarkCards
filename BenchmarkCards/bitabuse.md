# BitAbuse

## 📊 Benchmark Details

**Name**: BitAbuse

**Overview**: The BitAbuse dataset includes real-world phishing cases of visually perturbed texts to aid in the defense against phishing attacks. It consists of a total of 325,580 visually perturbed texts designed to help restore original sentences for defense against social engineering attacks.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Cybersecurity

**Languages**:
- English

**Similar Benchmarks**:
- BitCore
- BitViper

**Resources**:
- [GitHub Repository](https://github.com/CAU-AutoML/Bitabuse)
- [Resource](https://huggingface.co/datasets/AutoML/bitaubse)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset that aids in the research and development of defenses against phishing attacks by restoring visually perturbed texts.

**Target Audience**:
- ML Researchers
- Cybersecurity Experts
- Industry Practitioners

**Tasks**:
- Text Restoration
- Adversarial Attack Defense

**Limitations**: The BitAbuse dataset only includes data related to Bitcoin scams, limiting its ability to reflect a variety of phishing attack scenarios.

**Out of Scope Uses**:
- Using the dataset for malicious purposes to execute phishing attacks

## 💾 Data

**Source**: Collected from bitcoinabuse.com, providing real-world phishing emails.

**Size**: 325,580 sentences

**Format**: N/A

**Annotation**: Manually annotated with ground truth for the restoration process.

## 🔬 Methodology

**Methods**:
- Character BERT-based
- SimChar DB
- OCR
- Spell Checker
- GPT-4o mini

**Metrics**:
- Word Level Accuracy
- Word Level Jaccard
- BLEU Score

**Calculation**: Metrics are calculated based on the restoration accuracy of the methods applied to the dataset.

**Interpretation**: Higher scores indicate better performance in accurately restoring the original texts.

**Validation**: Performance validated using training, validation, and test splits.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Need for careful consideration on dataset misuse leading to more sophisticated phishing attacks.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected from users while ensuring personal information remains masked.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
