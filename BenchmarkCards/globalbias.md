# GlobalBias

## 📊 Benchmark Details

**Name**: GlobalBias

**Overview**: GlobalBias is a dataset of 876,000 sentences that incorporates 40 distinct gender-by-ethnicity groups to study harmful stereotypes and evaluate language models' outputs.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- StereoSet
- HOLISTICBIAS

**Resources**:
- [GitHub Repository](https://github.com/groovychoons/GlobalBias)

## 🎯 Purpose and Intended Users

**Goal**: To conduct a comprehensive study of intersectional stereotypes and evaluate how these stereotypes are represented in language models.

**Target Audience**:
- ML Researchers
- Ethics in AI Developers

**Tasks**:
- Bias Analysis
- Stereotype Evaluation

**Limitations**: The dataset excludes critical aspects such as age, disability, and socioeconomic status and focuses on a fixed set of gender-by-ethnicity groups.

## 💾 Data

**Source**: Generated from clustering techniques applied on a seed dataset of names annotated with ethnicity and gender.

**Size**: 876,000 sentences

**Format**: JSON

**Annotation**: Automatically generated using clustering techniques.

## 🔬 Methodology

**Methods**:
- Evaluation of language models using perplexity and a novel metric Adjusted Perplexity across Descriptors (APX).

**Metrics**:
- Perplexity
- Adjusted Perplexity

**Calculation**: Perplexity is calculated using tokenized sentences or pseudo-likelihood for masked language models.

**Interpretation**: Lower perplexity scores indicate strong likelihood and more consistent stereotype associations within model outputs.

**Validation**: Validation through human evaluation of outputs against expected stereotypical narratives.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Social Bias

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Societal Impact**: Human exploitation

**Demographic Analysis**: The dataset examines biases across various intersectional demographic groups.

**Potential Harm**: Potential reinforcement of stereotypes could exacerbate societal inequalities.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
