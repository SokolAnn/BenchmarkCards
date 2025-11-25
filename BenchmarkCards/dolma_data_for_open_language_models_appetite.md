# Dolma (Data for Open Language Models' Appetite)

## 📊 Benchmark Details

**Name**: Dolma (Data for Open Language Models' Appetite)

**Overview**: Dolma is a three-trillion-token English corpus built from a diverse mixture of web content, scientific papers, code, public-domain books, social media, and encyclopedic materials, aimed at facilitating scientific research on language model pretraining through improved data transparency and reproducibility.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/allenai/dolma)
- [GitHub Repository](https://github.com/allenai/dolma)

## 🎯 Purpose and Intended Users

**Goal**: To promote transparency, reproducibility, and further research in language modeling by providing a comprehensive and well-documented dataset.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Language Modeling

**Limitations**: N/A

## 💾 Data

**Source**: Dolma corpus collected from a diverse set of sources including web pages, scientific papers, code from GitHub, public domain books, social media content, and encyclopedic materials.

**Size**: 11TB

**Format**: Plain text files

**Annotation**: Automated filtering, language identification, quality filtering, and deduplication.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Training evaluation on downstream tasks

**Metrics**:
- Perplexity
- Accuracy

**Calculation**: Metrics calculated using perplexity evaluations on various downstream tasks.

**Interpretation**: Lower perplexity indicates better model performance on language tasks; higher accuracy indicates better performance on specific benchmarks used for evaluation.

**Validation**: The Dolma corpus was validated against known benchmarks in language modeling tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: Analysis of the demographic factors is recommended for assessing the diversity of the provided content.

**Potential Harm**: ['Potential for perpetuating bias in language models due to the sourcing of data from the web and other repositories.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Efforts were made to remove personally identifiable information (PII) through filtering and regex identification.

**Data Licensing**: Released under ODC-By license, with terms for usage outlined on the Hugging Face page.

**Consent Procedures**: No direct informed consent was collected from data contributors; however, a mechanism for data removal is available.

**Compliance With Regulations**: The dataset aims for compliance with GDPR principles and provides avenues for individuals to request data removal.
