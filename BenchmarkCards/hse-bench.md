# HSE-Bench

## 📊 Benchmark Details

**Name**: HSE-Bench

**Overview**: HSE-Bench is the first benchmark dataset designed to evaluate the HSE compliance assessment capabilities of large language models (LLMs), comprising over 1,000 manually curated questions drawn from regulations, court cases, safety exams, and fieldwork videos using an IRAC reasoning framework.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LEGALBENCH
- MEDCALC-BENCH
- BEACON

**Resources**:
- [Resource](https://huggingface.co/datasets/Joysouo/hse-bench)
- [GitHub Repository](https://github.com/mengqiwang1/hse-bench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic framework for benchmarking, performance evaluation, and advancing the application of LLMs in HSE compliance assessment.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The dataset instances are created from regulations, court cases, safety exams, and fieldwork videos gathered from multiple authoritative sources.

**Size**: 1,020 questions

**Format**: JSON

**Annotation**: Manually curated and reviewed by experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- AUC-ROC

**Calculation**: Accuracy is the proportion of correct answers among total questions; AUC-ROC measures the model’s ability to rank the correct answer higher than incorrect ones.

**Interpretation**: Higher scores indicate better model performance in HSE compliance assessment.

**Baseline Results**: N/A

**Validation**: Benchmark results were validated through evaluation on 12 state-of-the-art LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
