# ChineseSafe: A Chinese Benchmark for Evaluating Safety in Large Language Models

## 📊 Benchmark Details

**Name**: ChineseSafe: A Chinese Benchmark for Evaluating Safety in Large Language Models

**Overview**: ChineseSafe is a comprehensive safety benchmark for evaluating the safety of large language models in Chinese contexts, focusing on 205,034 examples across 4 classes and 10 sub-classes of safety issues.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- SafetyBench
- CHiSafetyBench
- CHBench

**Resources**:
- [Resource](https://huggingface.co/spaces/SUSTech/ChineseSafe-Benchmark)
- [Resource](https://huggingface.co/datasets/SUSTech/ChineseSafe)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the safety of large language models in identifying unsafe content in Chinese scenarios.

**Target Audience**:
- Researchers
- Developers

**Tasks**:
- Safety Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Collected from open-sourced datasets and internet resources.

**Size**: 205,034 examples

**Format**: N/A

**Annotation**: Data processing includes cleaning and deduplication performed on the collected data.

## 🔬 Methodology

**Methods**:
- Generation-based evaluation
- Perplexity-based evaluation

**Metrics**:
- Accuracy
- Precision
- Recall

**Calculation**: Metrics are calculated based on model predictions for identifying unsafe content.

**Interpretation**: Higher scores indicate better performance in identifying unsafe content.

**Validation**: Extensive experiments on various mainstream LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
