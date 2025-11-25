# MML ONG BENCH

## 📊 Benchmark Details

**Name**: MML ONG BENCH

**Overview**: MML ONG BENCH is the first benchmark covering a diverse set of long-context vision-language tasks, designed to evaluate long-context vision-language models (LCVLMs) effectively and thoroughly. It includes 13,331 examples across five different categories of downstream tasks and standardizes input lengths from 8K to 128K tokens.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MMLongBench-Doc
- MM-NIAH

**Resources**:
- [GitHub Repository](https://github.com/EdinburghNLP/MMLongBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating long-context vision-language models (LCVLMs) across various multimodal tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Visual Retrieval-Augmented Generation
- Many-Shot In-Context Learning
- Long-Document Visual Question Answering
- Summarization

**Limitations**: The largest models tested were limited to 72B parameters due to computational resource constraints.

## 💾 Data

**Source**: Built upon existing open-sourced datasets, particularly focusing on long-context tasks featuring diverse multimodal examples.

**Size**: 13,331 examples

**Format**: JSON

**Annotation**: Automatically generated and manually checked for accuracy.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Substring Exact Match (SubEM)

**Calculation**: Metrics are calculated based on model outputs compared to ground truth annotations, using techniques specified for each dataset type.

**Interpretation**: Performance interpretation correlates with the benchmark's ability to assess complex multimodal reasoning tasks.

**Baseline Results**: The evaluation involved 46 models, highlighting various performance metrics across different tasks and context lengths.

**Validation**: The benchmark was validated against a wide range of existing models in the field, ensuring a comprehensive comparison.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Data poisoning
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: All data based on previously open-sourced datasets with publicly available licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
