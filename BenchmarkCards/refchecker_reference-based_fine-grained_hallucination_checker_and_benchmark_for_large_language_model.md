# REFCHECKER (Reference-based Fine-grained Hallucination Checker and Benchmark for Large Language Models)

## 📊 Benchmark Details

**Name**: REFCHECKER (Reference-based Fine-grained Hallucination Checker and Benchmark for Large Language Models)

**Overview**: REFCHECKER introduces claim-triplets to detect fine-grained hallucinations in responses from large language models, creating a comprehensive benchmark with 11k annotated claim-triplets across multiple tasks.

**Data Type**: claim-triplets

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SelfCheckGPT
- FActScore
- FacTool

**Resources**:
- [GitHub Repository](https://github.com/amazon-science/RefChecker)

## 🎯 Purpose and Intended Users

**Goal**: To provide a unified framework for detecting hallucination in LLM responses using claim-triplet analysis.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Hallucination Detection
- Question Answering
- Summarization
- Information Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Natural Questions, MS MARCO, databricks-dolly-15k

**Size**: 11,000 claim-triplets

**Format**: N/A

**Annotation**: Manually annotated by experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the correct identification of hallucination types (Entailment, Contradiction, Neutral).

**Interpretation**: Higher scores indicate better accuracy in detecting hallucinations.

**Baseline Results**: REFCHECKER outperforms prior methods by 6.8 to 26.1 points.

**Validation**: Validated through human evaluation with 95% Inter-Annotator Agreement.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Publicly accessible datasets under various licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
