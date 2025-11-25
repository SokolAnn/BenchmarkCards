# SG-Bench

## 📊 Benchmark Details

**Name**: SG-Bench

**Overview**: SG-Bench is a multi-dimensional safety evaluation benchmark designed to assess the generalization of large language model (LLM) safety across various tasks and prompt types. It integrates both generative and discriminative evaluation tasks and includes extended data to examine the impact of prompt engineering and jailbreak techniques on safety performance.

**Data Type**: malicious queries

**Domains**:
- Safety evaluation
- Machine Learning
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SafetyPrompts
- SafetyBench
- EasyJailbreak

**Resources**:
- [GitHub Repository](https://github.com/MurrayTom/SG-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of LLM safety generalization across diverse tasks and prompt types, facilitating safer AI model development.

**Target Audience**:
- AI researchers
- Model developers
- Safety engineers

**Tasks**:
- Evaluate safety performance
- Examine safety alignment techniques
- Analyze prompt engineering impacts

**Limitations**: N/A

**Out of Scope Uses**:
- Non-malicious content evaluation
- General LLM performance assessment

## 💾 Data

**Source**: Collected from multiple public datasets including AdvBench, HarmfulQA, and Beaver-eval

**Size**: 1442 malicious queries

**Format**: Text

**Annotation**: Malicious queries categorized into safety issues like toxic content, misinformation, privacy leaks, etc.

## 🔬 Methodology

**Methods**:
- Jailbreak attack techniques
- Multiple-choice questions
- Safety judgments

**Metrics**:
- Failure Rate

**Calculation**: The proportion of harmful responses to the total number of test samples, averaged across multiple tests.

**Interpretation**: Lower failure rates indicate better safety performance in LLMs.

**Baseline Results**: Claude-3 shows the best safety performance with an average failure rate of 2.99% compared to Qwen1.5-7B-chat with 30.79% average failure rate.

**Validation**: Evaluated using LlamaGuard-7B as a classifier for harmful responses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Malicious Use
- Privacy leak & infringement
- Misinformation
- Stereotyping & Bias
- Toxic content

**Atlas Risks**:
- **Robustness**: Prompt injection attack, Extraction attack, Data poisoning
- **Fairness**: Data bias, Output bias, Decision bias
- **Privacy**: Personal information in data, Reidentification
- **Explainability**: Inaccessible training data, Unexplainable output
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: Identified risks involve exposure to harmful information generation and lack of discrimination in responses.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected includes potentially harmful queries and was handled according to ethical guidelines to minimize risks.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Access to potentially harmful queries is limited to authorized researchers adhering to ethical standards.
