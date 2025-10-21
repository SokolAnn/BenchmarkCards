# OmniGIRL (A Multilingual and Multimodal Benchmark for GitHub Issue Resolution)

## 📊 Benchmark Details

**Name**: OmniGIRL (A Multilingual and Multimodal Benchmark for GitHub Issue Resolution)

**Overview**: OmniGIRL is a GitHub issue resolution benchmark that is multilingual, multimodal, and multi-domain, including 959 task instances collected from repositories across four programming languages (Python, JavaScript, TypeScript, and Java) and eight different domains.

**Data Type**: text and image information

**Domains**:
- Natural Language Processing
- Software Engineering

**Languages**:
- Python
- JavaScript
- TypeScript
- Java

**Similar Benchmarks**:
- SWE-bench
- SWE-bench Verified
- SWE-bench-java

**Resources**:
- [GitHub Repository](https://github.com/DeepSoftwareAnalytics/OmniGIRL)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating issue resolution abilities of LLMs across multiple programming languages, domains, and input modalities.

**Target Audience**:
- ML Researchers
- Software Engineers
- Model Developers

**Tasks**:
- GitHub Issue Resolution

**Limitations**: Limited performance of current LLMs on multi-language issues and those requiring image understanding.

## 💾 Data

**Source**: Collected from various GitHub repositories based on popularity and relevance across multiple domains.

**Size**: 959 task instances

**Format**: JSON

**Annotation**: Manually annotated with task instance information including issue descriptions, images, and website links.

## 🔬 Methodology

**Methods**:
- Oracle Retrieval
- Agentless-X
- AutoCodeRover-X

**Metrics**:
- Resolve Rate
- Apply Rate

**Calculation**: Metrics are calculated based on the percentage of task instances that are resolved successfully and patches that can be applied without errors.

**Interpretation**: Higher resolve and apply rates indicate better performance of the LLMs in issue resolution.

**Baseline Results**: GPT-4o with Agentless-X achieves the highest resolve rate of 8.6%.

**Validation**: Execution-based filtering to ensure task instances have verifiable solutions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Fairness

**Atlas Risks**:
- **Fairness**: Output bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
