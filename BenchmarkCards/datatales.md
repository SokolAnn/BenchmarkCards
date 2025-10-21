# DATATALES

## 📊 Benchmark Details

**Name**: DATATALES

**Overview**: DATATALES is designed to assess the proficiency of language models in data narration, providing 4.9k financial reports paired with corresponding market data to evaluate models’ ability to create clear narratives and analyze complex datasets in finance.

**Data Type**: text

**Domains**:
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- RotoWire
- WikiBio
- ToTTo

**Resources**:
- [GitHub Repository](https://github.com/yajingyang/DataTales/)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to evaluate language models' capabilities in generating insightful narrations from complex financial data, emphasizing precision and analytical depth.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Data-to-Text Generation

**Limitations**: The method and dataset are primarily designed for languages with limited morphology, such as English. The dataset currently focuses on market data and textual narratives without visual components.

## 💾 Data

**Source**: Financial reports from diverse outlets paired with comprehensive financial ticker data.

**Size**: 4,900 examples

**Format**: CSV

**Annotation**: The dataset was annotated through sentence categorization using in-context learning with ChatGPT.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Factual Accuracy
- Insightfulness
- Language Style

**Calculation**: Evaluated based on numerical predictions accuracy, human assessment of impact and significance of insights, and BLEU scores comparing generated text to human-written reports.

**Interpretation**: Good performance is indicated by high factual accuracy, insightful analysis leading to high impact and significance scores, and fluent language style as measured by BLEU scores.

**Baseline Results**: Baseline performance of models like GPT-3.5-Turbo, GPT-4, and LLaMa2 models was established in zero-shot and fine-tuned settings.

**Validation**: Results were validated through comprehensive human evaluations and automated assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Transparency

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personal data is included; all data sources respect copyright laws for non-commercial use.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The dataset complies with relevant copyright regulations and ethical standards for data use.
