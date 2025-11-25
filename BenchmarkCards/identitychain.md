# IdentityChain

## 📊 Benchmark Details

**Name**: IdentityChain

**Overview**: IdentityChain is a framework designed to evaluate the self-consistency and conventional accuracy of Code Large Language Models (LLMs), particularly in natural language to programming language (NL-to-PL) and programming language to natural language (PL-to-NL) generation tasks.

**Data Type**: program and natural language specifications

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- MBPP

**Resources**:
- [GitHub Repository](https://github.com/marcusm117/IdentityChain)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and provide insights into the self-consistency of Code LLMs, identifying weaknesses in their performance.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Code Generation
- Code Summarization

**Limitations**: N/A

## 💾 Data

**Source**: HumanEvalPlus-Mini-v0.1 and MBPP datasets.

**Size**: 164 tasks for HumanEvalPlus, 974 tasks for MBPP

**Format**: Python problems

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Test Output Match (TOM) score

**Calculation**: The accuracy is computed as a percentage based on correctly generated outputs compared to expected outputs.

**Interpretation**: Higher scores indicate better self-consistency and model performance.

**Baseline Results**: N/A

**Validation**: Model performance is validated using a set of benchmark tasks and manual examination of outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
