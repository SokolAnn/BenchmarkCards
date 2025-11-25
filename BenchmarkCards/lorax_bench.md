# LORAX BENCH

## 📊 Benchmark Details

**Name**: LORAX BENCH

**Overview**: LORAX BENCH is a benchmark that focuses on low-resource languages of Indonesia and covers 6 diverse tasks: reading comprehension, open-domain QA, language inference, causal reasoning, translation, and cultural QA, specifically for 20 Indonesian languages.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Indonesian
- Acehnese
- Ambonese Malay
- Balinese
- Banjar
- Batak Toba
- Betawi
- Buginese
- Gorontalo
- Iban
- Jambi Malay
- Javanese
- Lampung Nyo
- Madurese
- Makasar
- Minangkabau
- Musi
- Ngaju
- Sasak
- Sundanese

**Similar Benchmarks**:
- Florex
- XNLI
- IndoNLU
- IndoNLI
- COPAL-ID

**Resources**:
- [Resource](https://huggingface.co/datasets/google/LoraxBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation suite for low-resource Indonesian languages and encourage the development of models that better capture local nuances.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Reading Comprehension
- Open-Domain QA
- Natural Language Inference
- Causal Reasoning
- Cultural QA
- Machine Translation

**Limitations**: N/A

## 💾 Data

**Source**: Adapted existing Indonesian-language datasets through expert translation.

**Size**: 84,895 instances

**Format**: JSON

**Annotation**: Manual annotation by experts and native speakers.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Prompt strategies

**Metrics**:
- Accuracy

**Calculation**: Performance calculated based on the exact match of generated responses to gold-standard answers.

**Interpretation**: High scores indicate better model performance in understanding and processing the tasks in low-resource languages.

**Validation**: Human validation through review and redundancy checks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: Mediated through translator and annotator diversity across multiple Indonesian languages.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The benchmark will be released under an unrestricted license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
