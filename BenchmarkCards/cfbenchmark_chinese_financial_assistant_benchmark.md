# CFBenchmark (Chinese Financial Assistant Benchmark)

## 📊 Benchmark Details

**Name**: CFBenchmark (Chinese Financial Assistant Benchmark)

**Overview**: CFBenchmark is a Chinese financial assistant benchmark designed to evaluate the performance of large language models (LLMs) in basic financial text processing abilities across three aspects: recognition, classification, and generation, covering eight specific tasks.

**Data Type**: financial texts

**Domains**:
- Finance

**Languages**:
- Chinese

**Similar Benchmarks**:
- FLUE
- FLARE
- FinCUGE
- FinEval

**Resources**:
- [GitHub Repository](https://github.com/TongjiFinLab/CFBenchmark1)

## 🎯 Purpose and Intended Users

**Goal**: The primary goal is to assess the capabilities of large language models in processing Chinese financial texts and to provide insights into their performance in financial tasks.

**Target Audience**:
- ML Researchers
- Finance Professionals

**Tasks**:
- Financial Entity Recognition
- Financial Text Classification
- Financial Content Generation

**Limitations**: N/A

## 💾 Data

**Source**: Sourced from Chinese financial research reports and news articles spanning from 2018 to 2023.

**Size**: 3,917 financial texts

**Format**: N/A

**Annotation**: Annotated by three professional researchers from financial institutions.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Few-shot evaluation

**Metrics**:
- F1 Score
- Cosine Similarity

**Calculation**: F1 Score for recognition and classification tasks; Cosine Similarity for generation tasks.

**Interpretation**: Scores reflect the models' abilities to recognize, classify, and generate relevant financial content based on input texts.

**Baseline Results**: N/A

**Validation**: Evaluated against 22 renowned LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack, Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
