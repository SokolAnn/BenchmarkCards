# RealFactBench

## 📊 Benchmark Details

**Name**: RealFactBench

**Overview**: RealFactBench is a comprehensive benchmark designed to assess the fact-checking capabilities of Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs) across diverse real-world tasks, including Knowledge Validation, Rumor Detection, and Event Verification.

**Data Type**: text and image claims

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TruthfulQA
- HaluEval
- FEVER

**Resources**:
- [GitHub Repository](https://github.com/kalendsyang/RealFactBench.git)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the fact-checking capabilities of LLMs and MLLMs in real-world scenarios.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Knowledge Validation
- Rumor Detection
- Event Verification

**Limitations**: N/A

## 💾 Data

**Source**: Claims collected from authoritative sources and public fact-checking datasets.

**Size**: 6,000 samples

**Format**: N/A

**Annotation**: Claims labeled with TRUE/FALSE by human annotators, with supporting evidence sourced from credible materials.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- F1 Score
- Matthews Correlation Coefficient (MCC)
- Unknown Rate (UnR)

**Calculation**: Factual Accuracy is assessed via Macro F1-Score; Prediction Reliability is evaluated using MCC; Uncertainty Handling is measured with the Unknown Rate.

**Interpretation**: Higher scores in F1 and MCC indicate better performance in fact-checking capabilities.

**Validation**: Extensive experiments on existing LLMs and MLLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
