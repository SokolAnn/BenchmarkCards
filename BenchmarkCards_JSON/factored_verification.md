# Factored Verification

## 📊 Benchmark Details

**Name**: Factored Verification

**Overview**: A method for detecting and reducing hallucinations in summaries of academic papers.

**Data Type**: summarization

**Domains**:
- academic papers

**Similar Benchmarks**:
- HaluEval

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and mitigate hallucination in language model-generated summaries.

**Target Audience**:
- Researchers
- AI developers

**Tasks**:
- Detecting hallucinations in summaries
- Reducing hallucination rates in language models

**Limitations**: None

## 💾 Data

**Source**: HaluEval benchmark

**Size**: 4000 items

**Format**: text

**Annotation**: Claims are annotated based on their support by source material.

## 🔬 Methodology

**Methods**:
- Claim decomposition
- Probability assignment for each claim
- Model-generated critiques

**Metrics**:
- Accuracy of hallucination detection

**Calculation**: The probability that a summary is correct is calculated as the product of the probabilities of each individual claim.

**Interpretation**: A summary is classified as hallucinated if the overall probability exceeds a defined threshold.

**Validation**: Validated on the HaluEval benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
