# LawBench

## 📊 Benchmark Details

**Name**: LawBench

**Overview**: LawBench is a comprehensive evaluation benchmark designed to assess the legal capabilities of large language models (LLMs) on legal-related tasks based on the Chinese civil law system, covering memorization, understanding, and application of legal knowledge through 20 diverse tasks.

**Data Type**: text

**Domains**:
- Legal

**Languages**:
- Chinese

**Similar Benchmarks**:
- LEGELBENCH
- lexglue

**Resources**:
- [GitHub Repository](https://github.com/open-compass/LawBench/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a structured evaluation of LLMs' capabilities in the legal domain, emphasizing their ability to memorize, understand, and apply legal knowledge in realistic scenarios.

**Target Audience**:
- ML Researchers
- Legal Practitioners
- Model Developers

**Tasks**:
- Legal Knowledge Memorization
- Legal Knowledge Understanding
- Legal Knowledge Applying

**Limitations**: N/A

## 💾 Data

**Source**: Publicly available legal texts and datasets, including CAIL2022 and CAIL2019, and self-constructed datasets.

**Size**: 20 tasks

**Format**: JSON

**Annotation**: Curated from existing legal datasets and tasks with manual validation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score
- ROUGE-L
- rc-F1

**Calculation**: Metrics are computed based on extracted answers compared to ground truth.

**Interpretation**: Scores indicate how well models perform in various legal tasks, with specific metrics applied based on task type.

**Baseline Results**: N/A

**Validation**:  Extensive evaluations conducted across 51 LLMs to ensure robustness of results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
