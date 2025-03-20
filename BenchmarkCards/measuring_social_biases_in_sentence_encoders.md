# Measuring Social Biases in Sentence Encoders

## 📊 Benchmark Details

**Name**: Measuring Social Biases in Sentence Encoders

**Overview**: This study extends the Word Embedding Association Test (WEAT) to measure bias in sentence encoders, testing biases against gender, race, and other social constructs across various state-of-the-art models in natural language processing.

**Data Type**: Sentences

**Resources**:
- [GitHub Repository](http://github.com/W4ngatang/sent-bias)

## 🎯 Purpose and Intended Users

**Goal**: To measure the degree to which pretrained sentence encoders capture a range of social biases and explore the effectiveness of different experimental designs.

**Target Audience**:
- Researchers in natural language processing
- Ethics and fairness in AI communities

**Tasks**:
- Measure bias in sentence encoders
- Advocate for considerations of bias in NLP systems

**Limitations**: Results are preliminary and cannot definitively conclude absence of bias.

## 💾 Data

**Source**: Various sentence templates generated for tests

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Sentence Encoder Association Test (SEAT)
- Word Embedding Association Test (WEAT)

**Metrics**:
- Effect size
- P-value

**Calculation**: The SEAT uses cosine similarity to compare sets of sentence embeddings.

**Interpretation**: Higher effect size indicates stronger bias; the presence of a significant p-value indicates an association.

**Validation**: The results were validated by applying Holm-Bonferroni multiple testing correction.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias evaluation validity
- Intersectional biases in NLP

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Focused on U.S. contexts including race and gender.

**Potential Harm**: Potential reinforcement of stereotypes through bias in NLP systems.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
