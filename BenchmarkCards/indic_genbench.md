# INDIC GENBENCH

## 📊 Benchmark Details

**Name**: INDIC GENBENCH

**Overview**: INDIC GENBENCH is a high-quality, human-curated benchmark to evaluate text generation capabilities of multilingual models on Indic languages, consisting of diverse generation tasks such as cross-lingual summarization, machine translation, and cross-lingual question answering across 29 Indic languages.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Hindi
- Bengali
- Gujarati
- Kannada
- Malayalam
- Marathi
- Tamil
- Telugu
- Urdu
- Assamese
- Bhojpuri
- Nepali
- Odia
- Punjabi
- Pashto
- Sanskrit
- Awadhi
- Haryanvi
- Tibetan
- Bodo
- Garhwali
- Konkani
- Chhattisgarhi
- Rajasthani
- Maithili
- Manipuri
- Malvi
- Marwari
- Santali

**Similar Benchmarks**:
- CrossSum
- XQuAD
- XorQA
- FLORES

**Resources**:
- [GitHub Repository](https://github.com/google-research-datasets/indic-gen-bench)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research on multilingual LLM evaluation by providing a comprehensive benchmark for evaluating generative language capabilities across diverse Indic languages.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Cross-Lingual Summarization
- Machine Translation
- Multilingual Question Answering
- Cross-Lingual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Human curation and existing datasets such as CrossSum, FLORES, XQuAD, and XOR-TYDI.

**Size**: over 200,000 examples across multiple tasks and languages

**Format**: N/A

**Annotation**: Manual annotation by professional human translators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- ChrF

**Calculation**: Metrics are calculated as per the definitions for each task, with specific focus on low-resource languages.

**Interpretation**: Results indicate the model's ability to generate or translate content appropriately across various tasks in Indic languages.

**Baseline Results**: Performance on INDIC GENBENCH evaluated against multiple state-of-the-art LLMs including GPT-3.5, GPT-4, PaLM-2, mT5, Gemma, BLOOM, and LLaMA.

**Validation**: Evaluation is conducted through comprehensive testing across various model settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
