# CCrepairBench

## 📊 Benchmark Details

**Name**: CCrepairBench

**Overview**: A new, large-scale dataset for C++ compilation errors, constructed through a sophisticated generate-and-verify pipeline, designed for automated compilation repair.

**Data Type**: code snippets

**Domains**:
- Computer Science

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2509.15690)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive framework for automated C++ compilation repair.

**Target Audience**:
- Research Community
- Software Engineers
- ML Researchers

**Tasks**:
- Code Repair

**Limitations**: N/A

## 💾 Data

**Source**: Constructed through web scraping and a LLM-driven data generation and verification pipeline.

**Size**: Large-scale, specific number not mentioned.

**Format**: N/A

**Annotation**: Automatically validated by comparing compiled outputs against expected errors.

## 🔬 Methodology

**Methods**:
- Reinforcement Learning
- Automated Metrics

**Metrics**:
- Compilation Success Rate (CSR)
- Genuine Fix Rate (GFR)

**Calculation**: Total reward R is gated by the classification from an LLM-as-a-Judge.

**Interpretation**: High CSR and GFR indicate a successful repair.

**Validation**: The model's performance was validated through comparative performance analysis.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
