# GG-BBQ (German Gender Bias Benchmark for Question Answering)

## 📊 Benchmark Details

**Name**: GG-BBQ (German Gender Bias Benchmark for Question Answering)

**Overview**: The GG-BBQ dataset evaluates gender bias in German Large Language Models (LLMs) using a systematically translated subset of the English BBQ dataset, specifically designed for measuring bias in Question Answering tasks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- German

**Similar Benchmarks**:
- BBQ
- CBBQ
- KoBBQ

**Resources**:
- [GitHub Repository](https://github.com/shalakasatheesh/GG-BBQ)

## 🎯 Purpose and Intended Users

**Goal**: To create resources for studying biases in LLMs used in German contexts.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: The dataset may not capture all biases relevant to the German-speaking cultural context and relies on a single language expert for translation, which may introduce biases.

## 💾 Data

**Source**: A translated subset of the Bias Benchmark for Question Answering (BBQ) dataset originally created for U.S. English contexts.

**Size**: 167 templates, 2 subsets totaling 5,000 samples

**Format**: JSON

**Annotation**: Manual review and correction by a language expert

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Bias Score

**Calculation**: Accuracy calculated for ambiguous and disambiguated contexts, with bias evaluated using the difference in biased predictions.

**Interpretation**: A model with zero bias will score 0 on bias metrics and an accuracy close to 1.

**Validation**: Evaluated using multiple models under a zero-shot setting.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Gender bias analyzed across models.

**Potential Harm**: ['Potential reinforcement of gender stereotypes']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
