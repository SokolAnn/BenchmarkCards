# BBQ (Bias Benchmark for Question Answering)

## 📊 Benchmark Details

**Name**: BBQ (Bias Benchmark for Question Answering)

**Overview**: BBQ is a dataset of question sets constructed to highlight social biases in model outputs for question answering tasks across nine social dimensions relevant for U.S. English-speaking contexts.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- UnQover

**Resources**:
- [GitHub Repository](https://github.com/nyu-mll/BBQ)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to measure social biases in question answering models and assess model behavior in various contexts.

**Target Audience**:
- Researcher
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The dataset is not designed to cover all possible social biases and is limited to contexts relevant to U.S. English-speaking cultures.

## 💾 Data

**Source**: Hand-written contexts and questions targeting social biases.

**Size**: 58,492 examples

**Format**: JSON

**Annotation**: Templates were validated by crowdworkers and experts through multiple-choice tasks.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Bias Score

**Calculation**: Bias scores reflect the degree to which a model systematically produces answers that align with social biases.

**Interpretation**: Higher accuracy in disambiguated contexts compared to ambiguous contexts; models show different reliance on biases depending on context.

**Baseline Results**: Various models tested including UniﬁedQA, RoBERTa, and DeBERTaV3.

**Validation**: Examples were validated via Amazon Mechanical Turk with a threshold of 4/5 annotators agreeing with gold labels for inclusion.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: BBQ includes demographic breakdowns of the targeted biases.

**Potential Harm**: Potential for reinforcing harmful stereotypes during QA tasks.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC-BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
