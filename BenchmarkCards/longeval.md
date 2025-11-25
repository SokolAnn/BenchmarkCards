# LongEval

## 📊 Benchmark Details

**Name**: LongEval

**Overview**: LongEval is a benchmark designed to evaluate long-text generation capabilities of Large Language Models (LLMs) through direct and plan-based generation paradigms.

**Data Type**: long-form text generation

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HelloBench
- LongWriter

**Resources**:
- [GitHub Repository](https://github.com/Wusiwei0410/LongEval)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of LongEval is to comprehensively evaluate the long-text generation capabilities of LLMs and highlight their performance degradation as text length increases.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Long-Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: The data sources are arXiv papers, Wikipedia articles, and blogs collected from publicly available data.

**Size**: 166 samples

**Format**: N/A

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Content-following Score
- Redundancy Score
- Length Score
- Consistency Score
- Introduction Score
- Related Work Score
- Method Score
- Experiment Analysis Score

**Calculation**: Metrics are computed based on adherence to content plans and quality of generated text.

**Interpretation**: Higher scores reflect better following of the content plans and higher quality of generated long texts.

**Baseline Results**: LongEval benchmark scores for various models provided across different domains.

**Validation**: Validation conducted through manual evaluations of generated content by trained reviewers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data was derived from permitted sources ensuring no copyright infringement.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
