# MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models

## 📊 Benchmark Details

**Name**: MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models

**Overview**: MiniLongBench is created through a data compression method tailored for long-text data, substantially reducing the evaluation cost of existing benchmarks while maintaining a high correlation with LongBench results.

**Data Type**: question-answering pairs, summarizations, code generation

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- LongBench

**Resources**:
- [GitHub Repository](https://github.com/username/repository)

## 🎯 Purpose and Intended Users

**Goal**: To provide a low-cost evaluation benchmark for assessing long context understanding (LCU) capabilities of large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Single Document Question Answering
- Multi Document Question Answering
- Summarization
- Few-shot Learning
- Code Generation

**Limitations**: The MiniLongBench may not capture all evaluation capabilities of LongBench, as the Spearman correlation can’t reach 1.0.

## 💾 Data

**Source**: Created by pruning the LongBench dataset based on redundancy analysis.

**Size**: 237 test samples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Logistic regression for representation learning
- Statistical sampling for redundancy analysis

**Metrics**:
- Spearman correlation coefficient

**Calculation**: Metrics are calculated based on the performance rankings of models on the selected test samples.

**Interpretation**: Higher Spearman correlation indicates better alignment with performance outcomes of LongBench.

**Baseline Results**: MiniLongBench achieves an average Spearman correlation of 0.97 with the original LongBench.

**Validation**: Validated through empirical analysis of over 60 LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Efficiency

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
