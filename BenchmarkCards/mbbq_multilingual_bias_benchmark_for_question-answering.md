# MBBQ (Multilingual Bias Benchmark for Question-answering)

## 📊 Benchmark Details

**Name**: MBBQ (Multilingual Bias Benchmark for Question-answering)

**Overview**: MBBQ is a carefully curated version of the English BBQ dataset extended to Dutch, Spanish, and Turkish, which measures stereotypes commonly held across these languages. It includes a parallel control dataset to independently measure task performance on the question-answering task.

**Data Type**: multiple-choice questions about stereotypes

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Dutch
- Spanish
- Turkish

**Similar Benchmarks**:
- BBQ (Bias Benchmark for Question-answering)

**Resources**:
- [GitHub Repository](https://github.com/Veranep/MBBQ)

## 🎯 Purpose and Intended Users

**Goal**: To investigate whether the social stereotypes exhibited by LLMs differ as a function of the language used to prompt them.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: The dataset cannot cover all stereotypes relevant for any of the languages; it focuses on stereotypes common across the selected languages.

## 💾 Data

**Source**: Translation and adaptation of the BBQ dataset using native speakers for verification.

**Size**: 10,072 samples

**Format**: CSV

**Annotation**: Manually checked by native speakers and automated translations used.

## 🔬 Methodology

**Methods**:
- Evaluation of model responses based on accuracy and bias scores
- Human evaluation for bias scoring

**Metrics**:
- Accuracy
- Bias Score

**Calculation**: Bias scores are calculated based on the difference between ratios of predicting biased and counter-biased answers.

**Interpretation**: Higher bias scores indicate a preference for answers that align with existing stereotypes.

**Validation**: Models were evaluated against control datasets to isolate bias from performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis of differences in bias across demographic groups within languages.

**Potential Harm**: ['Exacerbation of cultural stereotypes across languages.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The dataset will state it should be used for evaluation of models only.

**Consent Procedures**: Participants were warned about encountering stereotypes and biases during evaluations.

**Compliance With Regulations**: Not Applicable
