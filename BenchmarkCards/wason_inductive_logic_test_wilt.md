# Wason Inductive Logic Test (WILT)

## 📊 Benchmark Details

**Name**: Wason Inductive Logic Test (WILT)

**Overview**: WILT is a multi-turn inductive logic benchmark designed to assess LLMs’ ability to gather evidence and reason across multiple turns, requiring models to propose test cases and infer hidden rules.

**Data Type**: test cases with boolean outcomes

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MATH
- GSM8K
- CommonsenseQA
- StrategyQA
- BIG-BENCH
- SciBench

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To measure LLMs' multi-turn reasoning capabilities and gather evidence over multiple interactions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Inductive Logic Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Test cases generated based on the Wason 2-4-6 task principles.

**Size**: 50 tests in full split, 10 tests in lite split

**Format**: JSON

**Annotation**: Manually constructed hidden rules and test cases.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Correct responses out of total tests attempted to diagnose reasoning capabilities.

**Interpretation**: Higher accuracy indicates better multi-turn reasoning.

**Baseline Results**: Top-performing models achieved only 28% accuracy.

**Validation**: Models evaluated on both lite and full test splits.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
