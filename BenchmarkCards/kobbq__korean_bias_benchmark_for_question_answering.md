# KoBBQ: Korean Bias Benchmark for Question Answering

## 📊 Benchmark Details

**Name**: KoBBQ: Korean Bias Benchmark for Question Answering

**Overview**: KoBBQ is a dataset designed to evaluate social biases of language models (LMs) in the Korean context, adapting the English BBQ benchmark to reflect cultural nuances unique to South Korea.

**Data Type**: Question-Answering

**Domains**:
- Social Bias
- Cultural Adaptation

**Languages**:
- Korean

**Similar Benchmarks**:
- BBQ
- CBBQ

**Resources**:
- [Resource](https://jinjh0123.github.io/KoBBQ)

## 🎯 Purpose and Intended Users

**Goal**: To measure and analyze social biases in Korean language models through a culturally adapted benchmark.

**Target Audience**:
- Researchers
- Developers of LMs
- Social scientists

**Tasks**:
- Evaluate bias in LMs
- Assess accuracy in QA tasks

**Limitations**: The perception of social bias can be subjective; further research is needed to explore other bias categories.

**Out of Scope Uses**:
- Training models to generate biased content
- Non-research related applications

## 💾 Data

**Source**: KoBBQ Dataset

**Size**: 76,048 samples

**Format**: Multiple-choice QA format

**Annotation**: Templates and samples reflect cultural biases in South Korea

## 🔬 Methodology

**Methods**:
- Large-scale survey for bias validation
- Cultural-sensitive translation
- Template categorization

**Metrics**:
- Accuracy
- Bias score

**Calculation**: Accuracy is calculated based on correct responses given ambiguous and disambiguated contexts. Bias scores measure model tendencies toward biased answers.

**Interpretation**: Higher accuracy correlates with lower bias scores; a balanced assessment combines both aspects.

**Validation**: Templates validated through a survey of 100 South Koreans for demographic representation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Cultural bias
- Translation inaccuracies
- Representation of stereotypes

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: Demographic details were collected to ensure broad representation in survey validation.

**Potential Harm**: Misinterpretations of the biases could perpetuate stereotypes or reinforce biases in LMs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Participants in surveys were ensured privacy and anonymity.

**Data Licensing**: Dataset usage is restricted to non-malicious applications.

**Consent Procedures**: Informed consent was obtained from all participants involved in the survey.

**Compliance With Regulations**: Study conducted under approval from KAIST IRB.
