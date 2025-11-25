# SEALQA

## 📊 Benchmark Details

**Name**: SEALQA

**Overview**: SEALQA is a benchmark for evaluating Search-Augmented Language Models on challenging factual questions where web search results may be conflicting, noisy, or irrelevant. It includes three variants: SEAL-0, SEAL-HARD, and LONG SEAL, each targeting different challenges in search-augmented reasoning.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU

**Resources**:
- [Resource](https://huggingface.co/datasets/vtllms/sealqa)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate reasoning under noisy, conflicting, and ambiguous search results.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: SEALQA is small and questions are constructed to have a single short answer, which may not fully capture the complexity of real-world information-seeking tasks.

## 💾 Data

**Source**: Carefully curated questions created by NLP researchers.

**Size**: 111 questions (SEAL-0), 254 questions (SEAL-HARD), 254 questions (LONG SEAL)

**Format**: N/A

**Annotation**: Questions are reviewed and approved through a multi-round vetting process involving graduate-level and expert reviewers.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Evaluation uses auto-rater to label responses as 'correct', 'incorrect', or 'not attempted'.

**Interpretation**: Performance is evaluated based on factual correctness and consistency throughout the response.

**Baseline Results**: Frontier LLMs perform poorly across SEALQA variants.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
