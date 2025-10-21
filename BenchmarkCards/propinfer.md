# PropInfer

## 📊 Benchmark Details

**Name**: PropInfer

**Overview**: PropInfer is a benchmark task for evaluating property inference in large language models (LLMs) under question-answering and chat-completion paradigms, focusing on the confidentiality of fine-tuning datasets.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare
- Finance
- Legal

**Languages**:
- English

**Similar Benchmarks**:
- ChatDoctor

**Resources**:
- [Resource](https://huggingface.co/datasets/Pengrun/PropInfer_dataset)

## 🎯 Purpose and Intended Users

**Goal**: To investigate property inference attacks on LLMs and provide a standardized framework for future research and evaluation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Data Scientists

**Tasks**:
- Property Inference

**Limitations**: Specialized attacks may not apply to all LLMs and task configurations.

## 💾 Data

**Source**: ChatDoctor dataset

**Size**: 29,791 conversations for gender labeling, 50,000 for medical diagnosis

**Format**: JSON

**Annotation**: Labeling using ChatGPT-4o and manual inspection

## 🔬 Methodology

**Methods**:
- Black-box generation attack
- Shadow-model attack with word frequency

**Metrics**:
- Mean Absolute Error (MAE)

**Calculation**: MAE calculated as the absolute error between predicted and actual property ratios.

**Interpretation**: Lower MAE indicates better performance in inferring property ratios.

**Validation**: Empirical evaluations across multiple pretrained LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy
- Fairness

**Atlas Risks**:
- **Privacy**: Exposing personal information
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: Yes, includes demographic breakdowns.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
