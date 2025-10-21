# JAPAGEN (Japanese Training Dataset Generation)

## 📊 Benchmark Details

**Name**: JAPAGEN (Japanese Training Dataset Generation)

**Overview**: JAPAGEN utilizes large language models (LLMs) to synthesize supervised training data for various Japanese natural language processing tasks, including text classification and natural language inference, under few-shot and zero-shot learning scenarios.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Japanese

**Similar Benchmarks**:
- JGLUE

**Resources**:
- [GitHub Repository](https://github.com/retrieva/JapaGen)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the effectiveness of using LLMs as synthetic data generators in Japanese NLP tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification
- Natural Language Inference
- Semantic Textual Similarity

**Limitations**: N/A

## 💾 Data

**Source**: JGLUE datasets including MARC-ja, JSTS, JNLI, JCoLA, News, and COVID-19.

**Size**: 25,000 examples per class for synthesized data

**Format**: N/A

**Annotation**: Generated using large language models

## 🔬 Methodology

**Methods**:
- Data generation via LLMs
- Fine-tuning of models with synthesized data
- Prompting

**Metrics**:
- Accuracy
- Matthews Correlation Coefficient (MCC)
- Spearman’s Rank Correlation Coefficient

**Calculation**: Metrics are calculated based on the performance of models fine-tuned on synthetic data

**Interpretation**: Higher scores indicate better performance in classification tasks.

**Baseline Results**: N/A

**Validation**: Performance compared against established benchmarks

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
