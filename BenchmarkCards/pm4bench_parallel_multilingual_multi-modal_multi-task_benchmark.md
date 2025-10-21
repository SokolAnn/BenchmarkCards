# PM4Bench (Parallel Multilingual Multi-Modal Multi-task Benchmark)

## 📊 Benchmark Details

**Name**: PM4Bench (Parallel Multilingual Multi-Modal Multi-task Benchmark)

**Overview**: PM4Bench features a parallel corpus design across 10 languages for fair and accurate cross-lingual comparisons in evaluating Large Vision Language Models (LVLMs). It incorporates safety evaluations and includes tasks that require models to simultaneously interpret visual and textual information.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Chinese
- Korean
- Thai
- Vietnamese
- Russian
- Hungarian
- Serbian
- Czech
- Arabic

**Similar Benchmarks**:
- M3Exam
- MMJB

**Resources**:
- [GitHub Repository](https://github.com/opendatalab/PM4Bench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of LVLMs in multilingual and multi-modal scenarios, identifying performance disparities and guiding further optimization.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Multi-Discipline Understanding and Reasoning
- Multi-Image Question Answering
- Multi-Modal JailBreaking Challenge
- Multi-Size OCR Challenge

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from various datasets like MMMU-pro and SafeBench, translated and curated to create parallel corpora.

**Size**: 10 languages, 1730 samples per language for MDUR, varied sizes for other tasks

**Format**: N/A

**Annotation**: Machine translation followed by human verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- LLM-based evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Scores calculated based on correct percentage for MDUR, average scores for MIQA based on multiple criteria, safety rate for MMJB, and recognition error rates for MSOCR.

**Interpretation**: Higher scores indicate better performance in multilingual understanding and safety.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Risk of harmful outputs due to safety vulnerabilities.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personally identifiable information is included in the datasets.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
