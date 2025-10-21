# L2CEval (Evaluating Language-to-Code Generation Capabilities of Large Language Models)

## 📊 Benchmark Details

**Name**: L2CEval (Evaluating Language-to-Code Generation Capabilities of Large Language Models)

**Overview**: L2CEval provides a systematic evaluation of the language-to-code generation capabilities of LLMs on 7 tasks across the domain spectrum of semantic parsing, math reasoning, and Python programming, analyzing factors that affect performance and releasing model outputs.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://l2c-eval.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To provide insight into applying LLMs to language-to-code generation tasks and to facilitate future research in this domain.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Semantic Parsing
- Math Reasoning
- Python Programming

**Limitations**: N/A

## 💾 Data

**Source**: Evaluated across a variety of datasets including Spider, WikiTQ, GSM8k, MBPP, HumanEval, and DS-1000.

**Size**: 1,000 examples (for Spider), 2,828 examples (for WikiTQ), and numerous examples for other tasks

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Execution accuracy

**Calculation**: Execution accuracy calculated by checking if the model's output matches the expected result upon execution.

**Interpretation**: Models are evaluated on their ability to generate executable code that meets user intent.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
