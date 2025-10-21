# SCOP (Systematic Comprehension Operations for Language Models)

## 📊 Benchmark Details

**Name**: SCOP (Systematic Comprehension Operations for Language Models)

**Overview**: SCOP is proposed to explore the comprehension process of large language models (LLMs) from a cognitive view. It includes a systematic definition of five requisite comprehension skills, a strict data construction framework, and a detailed analysis of various LLMs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SQuAD v2.0
- HotpotQA
- MCTest
- NewsQA

**Resources**:
- [GitHub Repository](https://github.com/SCUNLP/SCOP)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of SCOP is to evaluate and improve the comprehension process of large language models by examining their alignment with expert comprehension skills.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Reading Comprehension
- Text Understanding
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Various existing datasets and new data crawled based on skill definitions.

**Size**: 4,682 samples

**Format**: N/A

**Annotation**: Data annotated based on systematic definitions of comprehension skills.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: The accuracy is defined as the number of times LLM’s predictions exactly match the golden results, divided by the total sample size.

**Interpretation**: Higher accuracy indicates better alignment of LLM comprehension process with expert-level comprehension.

**Baseline Results**: N/A

**Validation**: The methodology involves rigorous filtering of data to ensure valid evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All datasets are reviewed to ensure they comply with respective licenses and do not contain personally identifiable information.

**Data Licensing**: Data used in SCOP complies with the licensing terms of the original datasets.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
