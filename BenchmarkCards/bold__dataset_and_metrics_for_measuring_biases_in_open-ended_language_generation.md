# BOLD: Dataset and Metrics for Measuring Biases in Open-Ended Language Generation

## 📊 Benchmark Details

**Name**: BOLD: Dataset and Metrics for Measuring Biases in Open-Ended Language Generation

**Overview**: BOLD is a large-scale dataset that consists of 23,679 English text generation prompts for bias benchmarking across five domains: profession, gender, race, religion, and political ideology. It proposes new automated metrics for toxicity, psycholinguistic norms, and text gender polarity to measure social biases in open-ended text generation.

**Data Type**: English text generation prompts

**Domains**:
- profession
- gender
- race
- religion
- political ideology

**Languages**:
- English

**Similar Benchmarks**:
- StereoSet
- GAP dataset
- Equity Evaluation Corpus (EEC)

**Resources**:
- [GitHub Repository](https://github.com/jwaladhamala/BOLD-Bias-in-open-ended-language-generation)

## 🎯 Purpose and Intended Users

**Goal**: To systematically study and benchmark social biases in open-ended language generation.

**Target Audience**:
- researchers
- practitioners
- developers of language generation models

**Tasks**:
- evaluate bias in language models
- benchmark biases
- assist in improving fairness in language generation

**Limitations**: The dataset considers a limited set of demographics and groups, particularly binary gender and a small subset of racial identities.

**Out of Scope Uses**:
- applications beyond language generation
- evaluations outside the defined demographic categories

## 💾 Data

**Source**: Wikipedia

**Size**: 23,679 prompts

**Format**: text

**Annotation**: Data includes prompts addressing biases in language generation across various social groups.

## 🔬 Methodology

**Methods**:
- automated bias metrics
- crowd-sourced human evaluation

**Metrics**:
- sentiment analysis
- toxicity classification
- gender polarity metrics

**Calculation**: Metrics are calculated based on the outputs from language models when prompted with carefully selected texts.

**Interpretation**: Results indicate the presence and extent of biases in generated texts, showing discrepancies between machine-generated and human-written texts.

**Validation**: Validation was performed using crowd-sourced annotators on a subset of the dataset to ensure metrics align with human judgments.

## ⚠️ Targeted Risks

**Risk Categories**:
- social bias
- gender bias
- racial bias
- religious bias
- political bias

**Atlas Risks**:
- **Fairness**: Data bias
- **Value Alignment**: Harmful output

**Demographic Analysis**: Analysis conducted across various demographic groups within the dataset.

**Potential Harm**: ['reinforcement of negative stereotypes', ' disparate treatment of historically disadvantaged groups']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset uses anonymization techniques to avoid incorporating bias from identifiable individuals.

**Data Licensing**: Public domain data from Wikipedia was used, adhering to licensing agreements.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Data collection and processing comply with relevant ethical guidelines for research.
