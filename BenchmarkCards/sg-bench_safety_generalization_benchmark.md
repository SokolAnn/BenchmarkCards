# SG-Bench (Safety Generalization Benchmark)

## 📊 Benchmark Details

**Name**: SG-Bench (Safety Generalization Benchmark)

**Overview**: SG-Bench is a multi-dimensional evaluation benchmark designed to assess the safety generalization of large language models (LLMs) across diverse tasks and prompt types. It integrates generative and discriminative evaluation tasks and investigates the impacts of prompt engineering and jailbreak attacks on model safety.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AdvBench
- SafetyPrompts
- SafetyBench
- EasyJailbreak
- Jailbroken

**Resources**:
- [GitHub Repository](https://github.com/MurrayTom/SG-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the generalization of safety-aligned LLMs across diverse tasks and prompt types, ensuring their reliability and safety in practical applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Safety Evaluation
- Prompt Engineering Analysis

**Limitations**: N/A

## 💾 Data

**Source**: SG-Bench was constructed using malicious queries collected from various datasets (AdvBench, HarmfulQA, Beaver-eval), which were filtered and categorized into different safety issues.

**Size**: 1,442 original malicious queries, 8,652 generated queries from jailbreak attacks, and 2,884 safety judgment queries

**Format**: N/A

**Annotation**: The data was annotated using Llama-Guard-7B for harmfulness evaluation, and through manual filtering and classification methods.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Failure Rate (FR)

**Calculation**: The Failure Rate is calculated based on the proportion of harmful responses determined by the judgment model compared to total responses.

**Interpretation**: Lower Failure Rate indicates better safety performance of the model.

**Baseline Results**: Average failure rates were calculated for proprietary and open-source LLMs, with Claude3 showing the best performance at 2.99% average failure rate.

**Validation**: Extensive experiments were conducted to validate the benchmark with various models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Privacy**: Exposing personal information

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential harm from unsafe content generation', 'Possible misuse of the model in generating harmful content']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Research emphasizes the importance of ethical guidelines and restricts access to authorized researchers to mitigate risks associated with harmful content.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
