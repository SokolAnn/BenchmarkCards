# VideoHallucer

## 📊 Benchmark Details

**Name**: VideoHallucer

**Overview**: VideoHallucer is the first comprehensive benchmark for hallucination detection in large video-language models (LVLMs), categorizing hallucinations into intrinsic and extrinsic types.

**Data Type**: Video Question-Answering

**Domains**:
- Multimodal Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- POPE
- HallusionBench
- MMHal-Bench

**Resources**:
- [Resource](https://VideoHallucer.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate hallucination issues in large video-language models.

**Target Audience**:
- Researchers in AI and machine learning
- Developers of video-language models

**Tasks**:
- Detecting hallucinations in LVLMs
- Evaluating model performance on video inputs

**Limitations**: The benchmark's scalability is currently limited.

**Out of Scope Uses**:
- General purpose video summarization
- Non-research-based commercial applications

## 💾 Data

**Source**: VideoHallucer dataset based on existing datasets like YouCook, COIN, and EDUVSUM.

**Size**: 1,800 question-answer pairs from 948 videos

**Format**: Dataset with paired basic and hallucinated question-answer formats

**Annotation**: Annotated by human evaluators, ensuring correctness and fluency.

## 🔬 Methodology

**Methods**:
- Adversarial binary VideoQA
- Question generation and annotation
- Comparison with existing benchmarks

**Metrics**:
- Accuracy
- Yes Percentage Difference
- False Positive Ratio

**Calculation**: Overall accuracy calculated by pairing basic and hallucinated questions.

**Interpretation**: Models' ability to recognize hallucinations does not compromise their fundamental task performance.

**Validation**: Comparison conducted against existing benchmarks to ensure reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Potential Harm**: Hallucinated questions could lead to misinterpretation in research contexts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset does not contain personal information to ensure privacy.

**Data Licensing**: The dataset is under CC BY-NC-SA (Attribution-NonCommercial-ShareAlike).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: All responsible for rights violations are acknowledged by the authors.
