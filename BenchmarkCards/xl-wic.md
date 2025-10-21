# XL-WiC

## 📊 Benchmark Details

**Name**: XL-WiC

**Overview**: XL-WiC is a large multilingual benchmark for evaluating semantic contextualization, featuring gold standards in 12 languages and allowing for evaluation in scenarios such as zero-shot cross-lingual transfer.

**Data Type**: sentence pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Bulgarian
- Chinese
- Croatian
- Danish
- Dutch
- Estonian
- Farsi
- French
- German
- Italian
- Japanese
- Korean

**Similar Benchmarks**:
- WiC (Word-in-Context)
- SuperGLUE

**Resources**:
- [Resource](https://pilehvar.github.io/xlwic/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reliable evaluation framework for contextualized models across multiple languages, addressing the limitations of existing benchmarks that rely on sense inventories.

**Target Audience**:
- ML Researchers
- Model Developers
- Linguistic Researchers

**Tasks**:
- Word Sense Disambiguation
- Cross-Lingual Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: The dataset includes examples extracted from Multilingual WordNet and Wiktionary, curated to form positive (same sense) and negative (different senses) instances.

**Size**: 80,000 instances

**Format**: N/A

**Annotation**: Instances were curated and validated with the aid of native speakers for each target language.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: The accuracy is calculated as the ratio of correctly predicted instances (true positives or true negatives) to the total number of instances.

**Interpretation**: Accuracy is used to evaluate model performance on the task of distinguishing different meanings of words in context.

**Baseline Results**: Models trained on English WiC data were evaluated on XL-WiC with reported performance metrics.

**Validation**: Manual evaluation was conducted on a subset of instances for reliability checking.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Safety

**Atlas Risks**:
- **Fairness**
- **Accuracy**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
