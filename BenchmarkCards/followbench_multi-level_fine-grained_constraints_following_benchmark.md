# FollowBench (Multi-level Fine-grained Constraints Following Benchmark)

## 📊 Benchmark Details

**Name**: FollowBench (Multi-level Fine-grained Constraints Following Benchmark)

**Overview**: FollowBench is a benchmark designed to comprehensively assess the instruction-following capabilities of Large Language Models (LLMs) by incorporating five different types of fine-grained constraints. It employs a novel multi-level mechanism that adds constraints incrementally to evaluate models on various difficulties.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- MMLU
- BIG-Bench

**Resources**:
- [GitHub Repository](https://github.com/YJiangcm/FollowBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a precise and comprehensive evaluation of instruction-following capabilities in LLMs.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Generation
- Open-ended Question Answering
- Content Constraints Evaluation
- Situation Constraints Evaluation
- Style Constraints Evaluation
- Format Constraints Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Curated dataset with instructions based on various NLP tasks.

**Size**: 820 instructions

**Format**: Text

**Annotation**: Manual and automated verification by experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Model-based evaluation

**Metrics**:
- Hard Satisfaction Rate (HSR)
- Soft Satisfaction Rate (SSR)
- Consistent Satisfaction Levels (CSL)

**Calculation**: Metrics are calculated based on the proportion of constraints satisfied in the instructions evaluated.

**Interpretation**: Higher scores indicate better adherence to constraints by LLMs.

**Validation**: Dual-layer human verification on instructions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Potential Harm**: ['Potential for biased outputs based on the instructions provided.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
