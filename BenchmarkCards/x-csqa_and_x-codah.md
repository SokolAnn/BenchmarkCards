# X-CSQA and X-CODAH

## 📊 Benchmark Details

**Name**: X-CSQA and X-CODAH

**Overview**: X-CSQA and X-CODAH are two cross-lingual commonsense reasoning datasets created for evaluating multilingual language models in question answering and scene completion tasks, respectively.

**Data Type**: question-answering pairs, scene completion pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- German
- Spanish
- French
- Italian
- Dutch
- Russian
- Vietnamese
- Hindi
- Polish
- Arabic
- Japanese
- Portuguese
- Swahili
- Urdu

**Similar Benchmarks**:
- CSQA
- CODAH
- SWAG

**Resources**:
- [Resource](https://inklab.usc.edu/XCSR/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve multilingual language models (ML-LMs) for advancing commonsense reasoning beyond English.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering
- Scene Completion

**Limitations**: N/A

## 💾 Data

**Source**: MickeyCorpus, a multilingual parallel corpus created by translating existing English commonsense datasets.

**Size**: 561,000 sentences

**Format**: N/A

**Annotation**: Automatically generated via translation methods.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Cross-lingual transfer

**Metrics**:
- Accuracy

**Calculation**: Hit@k accuracy is calculated based on the position of the correct answer in the ranked list of plausible sentences.

**Interpretation**: Higher accuracy indicates better performance in commonsense reasoning tasks.

**Validation**: Comparative analysis against state-of-the-art multilingual language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: Possibility of biased responses influenced by the multilingual training data.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
