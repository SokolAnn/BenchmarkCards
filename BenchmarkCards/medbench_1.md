# MedBench

## 📊 Benchmark Details

**Name**: MedBench

**Overview**: MedBench is a comprehensive, standardized, and reliable benchmarking system for evaluating Chinese Medical Large Language Models (LLMs). It includes the largest evaluation dataset with 300,901 questions covering 43 clinical specialties and implements a cloud-based evaluation infrastructure with dynamic mechanisms to prevent shortcut learning and answer leakage.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- Chinese

**Similar Benchmarks**:
- CMeEE
- CMeIE
- CHIP-CDEE
- CMB

**Resources**:
- [Resource](https://medbench.opencompass.org.cn)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of MedBench is to provide a standardized evaluation framework for assessing the efficacy of Medical Large Language Models in the Chinese context.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Medical Language Understanding
- Medical Language Generation
- Medical Knowledge Question Answering
- Complex Medical Reasoning
- Healthcare Safety and Ethics

**Limitations**: N/A

## 💾 Data

**Source**: The dataset comprises 8 public datasets and 12 self-constructed datasets featuring 300,901 Chinese-language medical questions across various medical contexts.

**Size**: 300,901 questions

**Format**: N/A

**Annotation**: The data was collected, screened, and verified by medical professionals to ensure accuracy and reliability.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- BLEU Score
- ROUGE-L
- Micro-F1

**Calculation**: Metrics are computed based on the performance of models on various tasks, averaging scores across different dimensions.

**Interpretation**: High scores correspond to better performance in correctly answering medical questions.

**Baseline Results**: N/A

**Validation**: MedBench's automation and cloud-based infrastructure are regularly updated to enhance reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**
- **Accuracy**
- **Robustness**: Evasion attack, Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The construction process includes rewriting medical records to ensure no identifiable personal information is disclosed.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
