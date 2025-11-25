# Multi-FAct: Assessing Factuality of Multilingual LLMs using FActScore

## 📊 Benchmark Details

**Name**: Multi-FAct: Assessing Factuality of Multilingual LLMs using FActScore

**Overview**: Multi-FAct introduces a simple pipeline for multilingual factuality evaluation, applying FActScore for diverse languages, validating it using human annotations, and exploring the use of non-English Wikipedia content for factuality evaluation.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- German
- French
- Spanish
- Arabic
- Swahili
- Chinese
- Korean
- Bengali

**Similar Benchmarks**:
- X-Fact
- mFACE

**Resources**:
- [Resource](https://arxiv.org/abs/2402.18045)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the factual accuracy of multilingual LLMs across different languages and geographic regions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Factuality Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Non-English Wikipedia articles and human annotations.

**Size**: N/A

**Format**: N/A

**Annotation**: Human annotations and verification by native speakers.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- FActScore

**Calculation**: FActScore is calculated by breaking down translated generations into atomic facts and measuring accuracy against corresponding English Wikipedia articles.

**Interpretation**: Higher FActScore indicates better factual accuracy in multilingual output.

**Baseline Results**: N/A

**Validation**: Comparison with human-annotated factual data and analysis of correlation with English Wikipedia.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
