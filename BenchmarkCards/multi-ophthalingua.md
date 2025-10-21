# Multi-OphthaLingua

## 📊 Benchmark Details

**Name**: Multi-OphthaLingua

**Overview**: This study introduces the first multilingual ophthalmological question-answering benchmark with manually curated questions parallel across languages, allowing for direct cross-lingual comparisons.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English
- Spanish
- Filipino
- Portuguese
- Mandarin
- French
- Hindi

**Resources**:
- [Resource](https://huggingface.co/datasets/AAAIBenchmark/Multi-Opthalingua/tree/main)

## 🎯 Purpose and Intended Users

**Goal**: To assess and debias LLM ophthalmological question-answering in multilingual contexts, facilitating equitable LLM application across different languages.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- AI Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The data was curated by board-certified ophthalmologists from diverse language backgrounds.

**Size**: 1184 questions

**Format**: N/A

**Annotation**: Manually curated and reviewed by native-speaker ophthalmologists.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated by measuring the proportion of correct answers in the question-answering tasks.

**Interpretation**: Higher accuracy indicates better performance of LLMs in understanding and responding to the ophthalmology-related questions.

**Baseline Results**: GPT-4 and GPT-3.5 accuracy results vary significantly, with GPT-4 achieving 63.4% in English and 51.8% in Filipino.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
