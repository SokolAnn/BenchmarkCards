# CloudAPIBench

## 📊 Benchmark Details

**Name**: CloudAPIBench

**Overview**: CloudAPIBench is a benchmark specifically designed to evaluate Code LLMs’ abilities to invoke cloud APIs, addressing API hallucinations in various software engineering contexts.

**Data Type**: synthetic tasks for API invocations

**Domains**:
- Natural Language Processing
- Computer Science

**Languages**:
- Python

**Resources**:
- [GitHub Repository](https://github.com/youtype/mypy_boto3_builder/)

## 🎯 Purpose and Intended Users

**Goal**: To systematically study real-world API hallucinations and evaluate Code LLMs' capabilities in invoking cloud APIs effectively.

**Target Audience**:
- ML Researchers
- Software Engineers
- Developers

**Tasks**:
- API Invocation
- Code Completion

**Limitations**: CloudAPIBench is a Python only benchmark containing synthetic prompts that may not represent all real-world cloud API invocations across different programming languages and contexts.

## 💾 Data

**Source**: Generated from API specifications and documentation from AWS and Azure.

**Size**: 622 tasks

**Format**: Synthetic code prompts

**Annotation**: Includes frequency annotations of APIs based on occurrences in The Stack v2.

## 🔬 Methodology

**Methods**:
- Evaluation on synthetic tasks
- Validation against API syntax through dummy function stubs

**Metrics**:
- Valid API Invocation
- Frequency of API Usage

**Calculation**: The valid API invocation metric is computed based on whether an API is invoked according to its syntax as determined by its required arguments.

**Interpretation**: Higher valid API invocation rates indicate better performance of Code LLMs in accurately invoking APIs.

**Baseline Results**: Performance results detailed across multiple models including GPT-4o, StarCoder2, etc.

**Validation**: Performance validated through API invocation success rates across task categories.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
