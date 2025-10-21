# 3LM

## 📊 Benchmark Details

**Name**: 3LM

**Overview**: 3LM is a suite of three benchmarks designed specifically for Arabic, focusing on STEM domains including mathematics, physics, chemistry, biology, and code generation.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic

**Resources**:
- [GitHub Repository](https://github.com/tiiuae/3LM-benchmark)
- [Resource](https://huggingface.co/datasets/tiiuae/evalplus-arabic)
- [Resource](https://huggingface.co/datasets/tiiuae/SyntheticQA)
- [Resource](https://huggingface.co/datasets/tiiuae/NativeQA)

## 🎯 Purpose and Intended Users

**Goal**: To advance Arabic LLM research in STEM and programming domains.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: The benchmark primarily targets middle and high school-level content.

## 💾 Data

**Source**: 3LM benchmark consists of native and synthetic questions from Arabic educational materials and machine-translated code benchmarks.

**Size**: 3,130 question-answer pairs

**Format**: JSON

**Annotation**: Manual and automatic generation processes, with human verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Calculated using model predictions against the correct answers from the benchmark.

**Interpretation**: Accuracy on benchmark tasks indicates model proficiency in STEM and code generation for the Arabic language.

**Validation**: Benched against over 40 state-of-the-art Arabic and multilingual LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Evasion attack

**Demographic Analysis**: The dataset includes diverse Arabic educational materials.

**Potential Harm**: Potential biases in synthetic question generation reflecting model limitations.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: All datasets are publicly available under open-source licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
