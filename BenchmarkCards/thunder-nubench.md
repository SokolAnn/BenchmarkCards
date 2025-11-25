# Thunder-NUBench

## 📊 Benchmark Details

**Name**: Thunder-NUBench

**Overview**: Thunder-NUBench is a benchmark designed to evaluate large language models' sentence-level understanding of negation, contrasting standard negation with structurally diverse alternatives such as local negation, contradiction, and paraphrase. It consists of manually curated sentence-negation pairs and a multiple-choice dataset for deep evaluation.

**Data Type**: sentence-negation pairs, multiple-choice questions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- NegNLI
- MoNLI
- SCoNe

**Resources**:
- [Resource](https://huggingface.co/datasets/thunder-research-group/SNU_Thunder-NUBench)

## 🎯 Purpose and Intended Users

**Goal**: To assess the ability of large language models to interpret sentence-level negation and understand its distinctions from related concepts like contradiction and paraphrase.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Negation Understanding

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from the HoVer dataset and Wikipedia Summary dataset

**Size**: 4,874 examples

**Format**: JSON

**Annotation**: Manually curated and reviewed by authors

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Normalized Accuracy

**Calculation**: Accuracy is calculated as the proportion of correct predictions over total predictions.

**Interpretation**: A higher accuracy indicates better performance in understanding negation over sentence structures, with normalized accuracy accounting for sentence length.

**Baseline Results**: N/A

**Validation**: Dataset was carefully validated through human review to ensure quality and consistency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-NC-SA 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
