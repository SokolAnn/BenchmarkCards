# UnsafeChain

## 📊 Benchmark Details

**Name**: UnsafeChain

**Overview**: UnsafeChain is a safety alignment dataset constructed from hard prompts with diverse sources, where unsafe completions are identified and explicitly corrected into safe responses. Its purpose is to enhance safety while preserving general reasoning ability.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SafeChain
- STAR-1

**Resources**:
- [GitHub Repository](https://github.com/mbzuai-nlp/UnsafeChain)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the safety of large reasoning models (LRMs) by exposing them to unsafe behaviors and guiding their correction.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Safety Alignment
- Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Collected from diverse datasets including WildJailbreak, StrongReject, GSM8K, MBPP, TruthfulQA, and HH-RLHF.

**Size**: 13,604 training examples, 2,069 test examples

**Format**: N/A

**Annotation**: Corrections made by GPT-4.1 for unsafe outputs.

## 🔬 Methodology

**Methods**:
- Supervised Fine-Tuning (SFT)

**Metrics**:
- Safe@1
- ConsSafe@5
- Safe@K

**Calculation**: Safety scores calculated by sampling multiple responses to evaluate their safety.

**Interpretation**: Higher scores indicate better performance in generating safe responses.

**Baseline Results**: UnsafeChain outperforms SafeChain and STAR-1 across multiple benchmarks.

**Validation**: Experimented across 11 benchmarks including WildJailbreak and StrongReject.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Constructed using publicly available prompts under permissible research licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
