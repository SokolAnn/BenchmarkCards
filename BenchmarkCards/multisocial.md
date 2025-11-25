# MultiSocial

## 📊 Benchmark Details

**Name**: MultiSocial

**Overview**: MultiSocial is the first multilingual (22 languages) and multi-platform (5 social media platforms) dataset for benchmarking machine-generated text detection in the social-media domain, containing 472,097 texts including human-written and machine-generated instances.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Spanish
- Chinese
- Arabic
- Bulgarian
- Catalan
- Czech
- Dutch
- German
- Greek
- Hungarian
- Irish
- Polish
- Portuguese
- Romanian
- Russian
- Slovak
- Slovenian
- Ukrainian

**Similar Benchmarks**:
- MULTITuDE
- M4GT-Bench

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.13846152)
- [GitHub Repository](https://github.com/kinit-sk/multisocial)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark dataset for machine-generated text detection methods on social-media texts.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Machine Generated Text Detection

**Limitations**: The dataset primarily consists of texts from five social-media platforms and is limited to 7 text generators.

## 💾 Data

**Source**: The dataset contains human-written data from five different social-media platforms (Telegram, Twitter, Gab, Discord, and WhatsApp) combined with machine-generated texts from 7 SOTA LLMs.

**Size**: 472,097 texts

**Format**: JSON

**Annotation**: Annotated with human and machine-generated text labels.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- AUC ROC
- Macro Average F1 Score

**Calculation**: Metrics are calculated using models trained on the MultiSocial dataset.

**Interpretation**: Higher AUC ROC indicates better detection capability.

**Validation**: Each method is validated on separate subsets of the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset is anonymized and does not contain sensitive user data.

**Data Licensing**: Published in accordance with the licenses of the six existing datasets it is based on.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
