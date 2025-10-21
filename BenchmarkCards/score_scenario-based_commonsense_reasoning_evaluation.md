# SCoRE (Scenario-based Commonsense Reasoning Evaluation)

## 📊 Benchmark Details

**Name**: SCoRE (Scenario-based Commonsense Reasoning Evaluation)

**Overview**: SCoRE is a benchmark designed to evaluate complex logical reasoning in commonsense scenarios through multi-step inference chains, synthesizing 100,000 bilingual (Chinese–English) questions of varying difficulty levels and explicit reasoning chains.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese
- English

**Similar Benchmarks**:
- CommonsenseQA
- ProtoQA
- bAbI

**Resources**:
- [GitHub Repository](https://github.com/pokerwf/KnowLogic)

## 🎯 Purpose and Intended Users

**Goal**: To assess the long-chain commonsense reasoning abilities of large language models (LLMs) and diagnose their reasoning capabilities.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Complex Logical Reasoning
- Multi-step Inference

**Limitations**: N/A

## 💾 Data

**Source**: The data is generated from a knowledge-based approach combining manual construction of a reliable knowledge base and automatic question generation.

**Size**: 100,000 questions

**Format**: N/A

**Annotation**: Manually constructed knowledge base integrated with automated question generation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the proportion of correct answers among the total presented questions.

**Interpretation**: Higher accuracy indicates better commonsense reasoning performance.

**Baseline Results**: The highest-performing model achieved 69.78% accuracy on SCoRE.

**Validation**: Evaluated against 13 state-of-the-art reasoning LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
