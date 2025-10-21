# XIFBench

## 📊 Benchmark Details

**Name**: XIFBench

**Overview**: XIFBench is a comprehensive constraint-based benchmark for assessing multilingual instruction-following abilities of Large Language Models (LLMs), featuring a novel taxonomy of five constraint categories and 465 parallel instructions across six languages.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- Russian
- Arabic
- Hindi
- Swahili

**Resources**:
- [Resource](https://arxiv.org/abs/2503.07539)

## 🎯 Purpose and Intended Users

**Goal**: To quantify and analyze multilingual instruction-following variations and their causes systematically.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Instruction Following

**Limitations**: N/A

## 💾 Data

**Source**: Seed instructions sourced from AlpacaEval, WizardLM, and LIMA; composed of 93 easy instructions and 465 hard instructions, validated for multilingual evaluation.

**Size**: 3,348 instances

**Format**: N/A

**Annotation**: Manual filtering and annotation with cultural accessibility labels by experts.

## 🔬 Methodology

**Methods**:
- LLM-based evaluation
- Manual evaluation

**Metrics**:
- Requirement Following Rate (RFR)
- Instruction Following Rate (IFR)

**Calculation**: RFR calculates the percentage of satisfaction across all evaluation requirements for each instruction; IFR quantifies the percentage of instructions where all requirements are met.

**Interpretation**: Higher rates indicate better adherence to the evaluated instructions across constraints and complexities.

**Baseline Results**: N/A

**Validation**: Evaluation verified by comparing outputs from multiple LLMs against a set of requirement criteria.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: Analysis of instruction-following performance across different languages and resource levels is included.

**Potential Harm**: The benchmark seeks to prevent potential biases in language model evaluation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data does not contain identifiable personal information; cultural accessibility annotations focus on general themes.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
