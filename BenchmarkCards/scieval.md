# SciEval

## 📊 Benchmark Details

**Name**: SciEval

**Overview**: SciEval is a comprehensive and multi-disciplinary evaluation benchmark designed to systematically evaluate the scientific research ability of Large Language Models (LLMs). It consists of about 18,000 challenging scientific questions across biology, chemistry, and physics, including both objective and subjective questions, while employing dynamic data generation to mitigate data leakage.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- AGIEval
- C-Eval
- MultiMedQA
- ChemLLMBench
- MATH

**Resources**:
- [GitHub Repository](https://github.com/OpenDFM/SciEval)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust benchmark for assessing scientific capabilities of Large Language Models (LLMs).

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Socratic Q&A, PubMedQA, MedQA, and custom scripts for generating physics data.

**Size**: 18,000 questions

**Format**: N/A

**Annotation**: The questions are preprocessed using rule-based methods, GPT-4 is utilized for generating and simplifying responses.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- BLEU Score
- Mean Squared Error (MSE)

**Calculation**: Accuracy is calculated for objective questions while MSE is used for numerical answers and BLEU score for string answers.

**Interpretation**: The performance of the models is compared based on the accuracy achieved on static and dynamic data subsets.

**Baseline Results**: Performance of several LLMs was tested; specific accuracy levels, such as GPT-4 achieving 84.49% on Static Data, are noted.

**Validation**: The benchmark is validated through comprehensive experiments on advanced LLMs, comparing their abilities on SciEval.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
