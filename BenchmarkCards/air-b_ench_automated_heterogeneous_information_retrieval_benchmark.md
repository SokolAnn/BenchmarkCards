# AIR-B ENCH (Automated Heterogeneous Information Retrieval Benchmark)

## 📊 Benchmark Details

**Name**: AIR-B ENCH (Automated Heterogeneous Information Retrieval Benchmark)

**Overview**: AIR-B ENCH is a new information retrieval benchmark characterized by its automated, heterogeneous, and dynamic features, providing diverse and high-quality testing data generated without human intervention.

**Data Type**: retrieval datasets

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- Arabic
- Bengali
- German
- Spanish
- Persian
- French
- Hindi
- Indonesian
- Japanese
- Korean
- Russian

**Similar Benchmarks**:
- MTEB
- BEIR
- Mr.TyDi
- MIRACL

**Resources**:
- [GitHub Repository](https://github.com/AIR-Bench/AIR-Bench)
- [Resource](https://huggingface.co/spaces/AIR-Bench/leaderboard)

## 🎯 Purpose and Intended Users

**Goal**: Advance the evaluation techniques for information retrieval models by providing a versatile and comprehensive benchmark.

**Target Audience**:
- IR Researchers
- ML Researchers
- Industry Practitioners

**Tasks**:
- Question Answering
- Long Document Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Real-world corpora

**Size**: 69 datasets

**Format**: N/A

**Annotation**: Automatically generated using large language models

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- nDCG@10
- Recall@10

**Calculation**: Standard evaluation metrics for retrieval tasks.

**Interpretation**: Higher scores indicate better retrieval performance.

**Baseline Results**: Results against existing benchmarks like MTEB and BEIR.

**Validation**: Comparative evaluation against human-labeled data sets

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Bias in generated outputs due to language model limitations']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: All generated testing data in AIR-B ENCH is licensed under CC BY-NC-SA-4.0.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
