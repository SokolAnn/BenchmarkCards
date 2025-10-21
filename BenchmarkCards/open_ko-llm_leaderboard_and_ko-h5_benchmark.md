# Open Ko-LLM Leaderboard and Ko-H5 Benchmark

## 📊 Benchmark Details

**Name**: Open Ko-LLM Leaderboard and Ko-H5 Benchmark

**Overview**: This paper introduces the Open Ko-LLM Leaderboard and the Ko-H5 Benchmark as vital tools for evaluating Large Language Models (LLMs) in Korean, incorporating private test sets and emphasizing the need for broader linguistic diversity in LLM evaluation.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Korean

**Similar Benchmarks**:
- Open LLM Leaderboard

**Resources**:
- [Resource](https://huggingface.co/spaces/upstage/open-ko-llm-leaderboard)

## 🎯 Purpose and Intended Users

**Goal**: To establish a robust evaluation framework for Korean LLMs that enhances linguistic diversity and addresses data contamination issues through private test sets.

**Target Audience**:
- ML Researchers
- Model Developers
- Korean LLM Developers

**Tasks**:
- Text Classification
- Question Answering
- Commonsense Reasoning

**Limitations**: The benchmark is prone to performance saturation due to its static nature as it primarily derives tasks from existing English benchmarks.

## 💾 Data

**Source**: The benchmark includes datasets like Ko-ARC, Ko-HellaSwag, Ko-MMLU, Ko-TruthfulQA, and Ko-CommonGen v2, some derived from original English datasets and others created specifically for Korean.

**Size**: 14,000 examples (Ko-MMLU), 10,000 examples (Ko-HellaSwag), 1,000 examples (Ko-ARC), 800 examples (Ko-TruthfulQA, Ko-CommonGen v2)

**Format**: Various formats derived or adapted from corresponding English datasets.

**Annotation**: The datasets were curated through a combination of machine translation and rigorous human review processes.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are computed based on the performance of models on the benchmark tasks, comparing outputs against ground truth.

**Interpretation**: Scores indicate model performance in text understanding, commonsense reasoning, and truthfulness.

**Baseline Results**: Improvements in benchmark scores were demonstrated across various model sizes and types over time.

**Validation**: The benchmark is validated through extensive empirical analysis and comparison with existing evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Data privacy rights alignment

**Demographic Analysis**: The dataset includes demographic factors, particularly in the aspect of evaluating linguistic nuances valid for Korean language models.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All datasets utilize private test sets to mitigate data contamination and leakage risks.

**Data Licensing**: The licenses for datasets include CC-BY-SA and MIT, allowing for open redistribution.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
