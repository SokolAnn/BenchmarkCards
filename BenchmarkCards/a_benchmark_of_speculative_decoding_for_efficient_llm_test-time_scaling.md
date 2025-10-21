# A Benchmark of Speculative Decoding for Efficient LLM Test-Time Scaling

## 📊 Benchmark Details

**Name**: A Benchmark of Speculative Decoding for Efficient LLM Test-Time Scaling

**Overview**: This paper introduces the first comprehensive benchmark designed to evaluate speculative decoding methods for accelerating large language model (LLM) test-time scaling in order to mitigate computational overhead.

**Data Type**: mathematics problems, question-answering tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AIME
- MATH
- GPQA

**Resources**:
- [Resource](https://arxiv.org/abs/2509.04474)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation of speculative decoding methods for accelerating LLM test-time scaling.

**Target Audience**:
- ML Researchers
- Practitioners

**Tasks**:
- Test-Time Scaling
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: AIME 2024 and AIME 2025, MATH-500, GPQA.

**Size**: 120 samples

**Format**: N/A

**Annotation**: Official problems from mathematical competitions and expert-level questions.

## 🔬 Methodology

**Methods**:
- Model-based speculative decoding
- Training-based speculative decoding
- N-gram-based methods

**Metrics**:
- Mean Accepted Tokens (MAT)
- Speedup Ratio

**Calculation**: Metrics calculated during experiments comparing speculative decoding methods under Best-of-N sampling and multi-round thinking.

**Interpretation**: Higher speedup ratio indicates improved efficiency in reasoning tasks.

**Baseline Results**: Key Baselines include Model-based SpS, Training-based EAGLE-3, and various N-gram methods.

**Validation**: Evaluation methods utilized fair experimental protocols defined in the benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
