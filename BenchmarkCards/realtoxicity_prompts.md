# REALTOXICITY PROMPTS

## 📊 Benchmark Details

**Name**: REALTOXICITY PROMPTS

**Overview**: REALTOXICITY PROMPTS is a dataset of 100K naturally occurring, sentence-level prompts derived from a large corpus of English web text, paired with toxicity scores from a widely-used toxicity classifier. It provides a testbed for evaluating toxic generations by language models and highlights the need for better data curation processes.

**Data Type**: sentence-level prompts with toxicity scores

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://toxicdegeneration.allenai.org/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the toxic degeneration in pretrained language models and assess various methods for detoxifying their outputs.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Text Generation
- Toxicity Detection

**Limitations**: N/A

## 💾 Data

**Source**: Derived from the OPENWEBTEXT CORPUS, a large corpus of English web text scraped from outbound URLs from Reddit.

**Size**: 100,000 prompts

**Format**: N/A

**Annotation**: Scored for toxicity using the PERSPECTIVE API

## 🔬 Methodology

**Methods**:
- Toxicity Detection using PERSPECTIVE API
- Empirical Evaluation of Language Model Generations

**Metrics**:
- Expected Maximum Toxicity
- Empirical Probability of Toxic Generation

**Calculation**: Toxicity is calculated based on the scores provided by the PERSPECTIVE API, with a threshold of 0.5 marking prompts as toxic.

**Interpretation**: Higher expected maximum toxicity indicates a greater risk of generating toxic outputs from language models.

**Validation**: Systematic evaluations performed by prompting various pretrained language models with the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Bias

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Propagation of toxic language in language model outputs']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
