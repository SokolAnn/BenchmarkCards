# JBBQ (Japanese Bias Benchmark for Analyzing Social Biases in Large Language Models)

## 📊 Benchmark Details

**Name**: JBBQ (Japanese Bias Benchmark for Analyzing Social Biases in Large Language Models)

**Overview**: The JBBQ dataset evaluates social biases in Japanese large language models (LLMs) using question-answering tasks, constructed from an existing English bias benchmark while adjusting for Japanese cultural contexts.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Japanese

**Similar Benchmarks**:
- BBQ
- CBBQ
- KoBBQ

**Resources**:
- [GitHub Repository](https://github.com/ynklab/JBBQ_data)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for assessing biases in Japanese large language models using a dataset that reflects Japan's unique social context.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The range of social categories in JBBQ is limited compared to the original BBQ, excluding nationality, race, religion, and socioeconomic status.

## 💾 Data

**Source**: Constructed from the BBQ dataset, translated, and modified for Japanese cultural contexts.

**Size**: 245 templates

**Format**: JSON

**Annotation**: Semi-automatically created, with translations and modifications made by native Japanese speakers.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Bias score

**Calculation**: Bias scores are calculated based on the model's predictions in ambiguous and disambiguated contexts.

**Interpretation**: Higher accuracy indicates better performance in correctly answering questions; bias scores reflect the tendency of models to produce biased answers.

**Validation**: Results were validated through experiments with various open Japanese LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt leaking

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset does not include personal identifiable information.

**Data Licensing**: Explicitly states that the dataset should not be used to generate biased language targeting specific groups.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
