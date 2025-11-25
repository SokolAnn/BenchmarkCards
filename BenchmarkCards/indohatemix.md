# IndoHateMix

## 📊 Benchmark Details

**Name**: IndoHateMix

**Overview**: IndoHateMix is a diverse, high-quality dataset capturing Hindi–English code-mixing and transliteration in the Indian context, providing a realistic benchmark to evaluate model robustness in complex multilingual scenarios where existing NLP methods often struggle.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Hindi
- English

**Similar Benchmarks**:
- HateXplain
- ImplicitHate

**Resources**:
- [Resource](https://huggingface.co/meta-llama/Llama-3.1-8B)
- [Resource](https://huggingface.co/mistralai/Mistral-7B-v0.3)
- [Resource](https://huggingface.co/internlm/internlm2_5-7b)
- [Resource](https://huggingface.co/Qwen/Qwen2.5-7B)

## 🎯 Purpose and Intended Users

**Goal**: To provide a realistic benchmark for hate speech detection in code-mixed Hindi-English contexts.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Hate Speech Detection

**Limitations**: N/A

## 💾 Data

**Source**: Curated from the Koo microblogging platform, targeted at accounts likely to generate hate speech.

**Size**: 11,725 samples

**Format**: N/A

**Annotation**: Manual annotation by three expert annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on standard performance analysis comparing model outputs against annotated dataset labels.

**Interpretation**: Higher accuracy, precision, recall, and F1 scores reflect better performance in detecting hate speech.

**Baseline Results**: LLMs such as LLaMA3.1-8B achieved accuracies of 83% on IndoHateMix.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
