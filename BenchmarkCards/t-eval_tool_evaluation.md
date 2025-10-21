# T-Eval (Tool Evaluation)

## 📊 Benchmark Details

**Name**: T-Eval (Tool Evaluation)

**Overview**: T-Eval is a step-by-step tool utilization evaluation benchmark for large language models (LLMs). It decomposes tool utilization capability into multiple subprocesses such as instruction following, planning, reasoning, retrieval, understanding, and review, facilitating a fine-grained analysis of LLMs' abilities.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/open-compass/T-Eval)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the tool utilization capabilities of large language models step by step, providing insights into their strengths and weaknesses.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Tool Utilization Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Generated from a multi-agent data generation pipeline verified by human experts.

**Size**: 23,305 test cases

**Format**: JSON, string

**Annotation**: Annotated by human experts through a multi-agent framework.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the generated action sequences and responses of LLMs compared against expert-verified results.

**Interpretation**: Results reflect the LLM's capabilities in each sub-domain of tool utilization.

**Validation**: Extensive experimentation with various LLMs to validate effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
