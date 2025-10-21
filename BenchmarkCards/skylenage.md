# SKYLENAGE

## 📊 Benchmark Details

**Name**: SKYLENAGE

**Overview**: SKYLENAGE provides a hard, reasoning-centered and broadly covering math benchmark with calibrated difficulty and rich metadata, serving as a reference benchmark for future evaluations of mathematical reasoning.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- MATH
- AIME
- GPQA
- MMLU-Pro

**Resources**:
- [Resource](https://arxiv.org/abs/2510.01241)

## 🎯 Purpose and Intended Users

**Goal**: To introduce benchmarks that restore headroom and enable fine-grained analysis of mathematical reasoning in language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Reasoning
- Contest-Style Problem Solving

**Limitations**: Some subjects are less represented in the 150-item track.

## 💾 Data

**Source**: Human authored and rule-based generation

**Size**: 100 reasoning problems, 150 contest-style problems

**Format**: N/A

**Annotation**: Dual label annotation with checks for uniqueness and consistency.

## 🔬 Methodology

**Methods**:
- Chain-of-Thought prompting
- Auto-grading
- Standardized answer extraction

**Metrics**:
- Accuracy

**Calculation**: Final answers are normalized via regex templates for grading.

**Interpretation**: Accuracy indicates robustness to structural difficulty in reasoning.

**Validation**: Analyzed using comparative performance across 15 contemporary LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Hallucination
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
