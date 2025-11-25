# Indic-QA Benchmark

## 📊 Benchmark Details

**Name**: Indic-QA Benchmark

**Overview**: Indic-QA Benchmark is a large dataset for context-grounded question answering in 11 major Indian languages, covering both extractive and abstractive tasks. This benchmark aims to evaluate the question-answering capabilities of multilingual large language models (LLMs) in low-resource languages.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Hindi
- Bengali
- Gujarati
- Kannada
- Malayalam
- Marathi
- Odia
- Punjabi
- Tamil
- Telugu
- Assamese

**Similar Benchmarks**:
- SQuAD
- XQuAD
- MLQA

**Resources**:
- [GitHub Repository](https://github.com/ayushayush591/IndicQA-Benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating LLMs' question-answering capabilities in Indic languages, particularly for low-resource contexts.

**Target Audience**:
- ML Researchers
- Domain Experts
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: The benchmark may not capture true performance across completely unseen domains, and potential cascading translation errors are acknowledged.

## 💾 Data

**Source**: The dataset compiles existing and translated datasets along with synthetic data generated using the Gemini model, focusing on cultural nuances from various Indian contexts.

**Size**: 55,000 instances

**Format**: JSON

**Annotation**: Manual verification for quality assurance and translation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- ROUGE-L

**Calculation**: F1 Score is calculated as the harmonic mean of precision and recall based on the predicted answer comparing the sets of words in the predicted and actual answers. ROUGE-L measures the recall of the generated response related to the gold response.

**Interpretation**: Higher F1 scores indicate better overall quality and correctness of generated answers. ROUGE-L evaluates how closely the generated text matches a reference answer.

**Baseline Results**: N/A

**Validation**: The benchmark was validated through extensive evaluation on multiple language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
