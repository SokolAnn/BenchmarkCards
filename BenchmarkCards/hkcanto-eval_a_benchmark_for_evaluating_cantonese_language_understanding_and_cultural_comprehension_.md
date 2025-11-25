# HKCanto-Eval (A Benchmark for Evaluating Cantonese Language Understanding and Cultural Comprehension in LLMs)

## 📊 Benchmark Details

**Name**: HKCanto-Eval (A Benchmark for Evaluating Cantonese Language Understanding and Cultural Comprehension in LLMs)

**Overview**: The HKCanto-Eval benchmark addresses the gap in evaluating the performance of large language models (LLMs) on Cantonese language understanding tasks, integrating cultural and linguistic nuances intrinsic to Hong Kong, and providing a framework for assessing language models in realistic scenarios.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Cantonese
- English
- Written Chinese

**Similar Benchmarks**:
- MMLU
- BIG-Bench
- CMMLU
- C-Eval
- TMLU
- TMMLU+

**Resources**:
- [GitHub Repository](https://github.com/hon9kon9ize/hkeval2025)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the Cantonese capabilities and Hong Kong knowledge of large language models, focusing on language proficiency, cultural knowledge, and reasoning skills.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Language Proficiency Assessment
- Cultural Knowledge Assessment
- Reasoning and Problem-Solving Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Datasets include translated MMLU dataset, Academic and Professional dataset, Hong Kong Cultural Questions dataset, Linguistic Knowledge dataset, and NLP Tasks dataset.

**Size**: 14,042 questions from MMLU, 1,196 questions from Academic and Professional dataset, and 277 questions from Cultural Questions dataset.

**Format**: JSON, CSV

**Annotation**: Manually annotated by experts and sourced from various educational and cultural resources.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- BLEU Score

**Calculation**: Accuracy calculated based on the number of correct answers from model outputs compared to the ground truth.

**Interpretation**: Higher scores indicate better performance in understanding and generating Cantonese language and cultural nuances.

**Baseline Results**: Proprietary models generally outperform open-weight models, but significant limitations remain in handling Cantonese-specific knowledge.

**Validation**: Validation procedures include comparative evaluations against human performance in cultural and linguistic assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy
- **Robustness**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
