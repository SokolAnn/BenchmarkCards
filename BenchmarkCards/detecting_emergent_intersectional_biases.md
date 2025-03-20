# Detecting Emergent Intersectional Biases

## 📊 Benchmark Details

**Name**: Detecting Emergent Intersectional Biases

**Overview**: This paper presents methods to identify and measure biases in neural language models, particularly focusing on intersectional and emergent biases associated with members of multiple minority groups, such as African American and Mexican American females.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Social Bias Detection

**Languages**:
- English

**Similar Benchmarks**:
- Word Embedding Association Test (WEAT)
- Bias in Bios

**Resources**:
- [GitHub Repository](https://github.com/weiguowilliam/CEAT)

## 🎯 Purpose and Intended Users

**Goal**: To detect and measure intersectional biases in word embeddings and neural language models.

**Target Audience**:
- Researchers in AI and NLP
- Social scientists studying bias
- Policy makers

**Tasks**:
- Identify intersectional biases
- Measure overall bias in language models

**Limitations**: None

## 💾 Data

**Source**: Common Crawl corpus and Reddit comments

**Size**: 840 billion tokens

**Format**: text

**Annotation**: Human subjects provided validation for intersectional attributes.

## 🔬 Methodology

**Methods**:
- Contextualized Embedding Association Test (CEAT)
- Intersectional Bias Detection (IBD)
- Emergent Intersectional Bias Detection (EIBD)

**Metrics**:
- Effect size (Cohen's d)
- Accuracy in detecting biases

**Calculation**: Combined effect sizes from multiple tests using random-effects model.

**Interpretation**: Significant result indicates a substantial bias in the context of measurements.

**Validation**: Validation conducted using previously published datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Potential Harm**: ['Perpetuation of stereotypes', 'Exacerbation of social inequalities']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data handling complies with ethical standards.

**Data Licensing**: Openly available datasets are used.

**Consent Procedures**: Validation sets utilized in accordance with ethical research guidelines.

**Compliance With Regulations**: Meets academic and research compliance standards.
