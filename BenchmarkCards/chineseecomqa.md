# ChineseEcomQA

## 📊 Benchmark Details

**Name**: ChineseEcomQA

**Overview**: ChineseEcomQA is a scalable question-answering benchmark designed to rigorously assess large language models (LLMs) on fundamental e-commerce concepts. It focuses on key characteristics such as e-commerce generality and expertise, addressing the challenges of diverse tasks and the need for precise validation of domain capabilities.

**Data Type**: question-answering pairs

**Domains**:
- E-commerce
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- Shopping MMLU

**Resources**:
- [GitHub Repository](https://github.com/OpenStellarTeam/ChineseEcomQA)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of ChineseEcomQA is to provide a systematic evaluation benchmark for large language models in the e-commerce domain, focusing on fundamental concepts.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: E-commerce corpus.

**Size**: 1,800 question-answer pairs

**Format**: N/A

**Annotation**: Manual annotation and LLM verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: The proportion of 'Correct' answers based on the evaluation criteria defined for the benchmark.

**Interpretation**: An answer is considered correct if it fully includes the reference answer without introducing contradictory elements.

**Baseline Results**: N/A

**Validation**: Evaluation procedures involving LLMs and human verification to ensure quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
