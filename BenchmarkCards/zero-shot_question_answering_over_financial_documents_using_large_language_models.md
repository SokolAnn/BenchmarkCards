# Zero-Shot Question Answering over Financial Documents using Large Language Models

## 📊 Benchmark Details

**Name**: Zero-Shot Question Answering over Financial Documents using Large Language Models

**Overview**: This paper proposes a zero-shot prompting technique for financial question answering that mitigates arithmetic errors by guiding large language models (LLMs) to generate executable programs for complex questions requiring multi-hop numerical reasoning over financial reports.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- FinQA
- ConvFinQA
- TATQA

**Resources**:
- [GitHub Repository](https://github.com/czyssrs/FinQA)
- [GitHub Repository](https://github.com/wenhuchen/Program-of-Thoughts)

## 🎯 Purpose and Intended Users

**Goal**: To optimize zero-shot prompts for financial question answering that leverage large language models for numerical reasoning.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: The proposed methods are specifically tailored for the GPT-x series and may require adjustment for other LLMs.

## 💾 Data

**Source**: FinQA, ConvFinQA, TATQA datasets

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Program generation via zero-shot prompts
- Evaluation against baseline zero-shot techniques

**Metrics**:
- Accuracy

**Calculation**: The accuracy is determined based on the correctness of the program output compared to the expected results.

**Interpretation**: A higher accuracy indicates more effective program generation and reasoning extraction by the LLM.

**Baseline Results**: ZS-FinPYT significantly improved accuracy over ZS-STD and ZS-CoT methods by up to 47%.

**Validation**: Experimental validation using test splits of FinQA, ConvFinQA, and TATQA datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

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
