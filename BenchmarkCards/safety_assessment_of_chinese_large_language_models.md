# Safety Assessment of Chinese Large Language Models

## 📊 Benchmark Details

**Name**: Safety Assessment of Chinese Large Language Models

**Overview**: This benchmark assesses the safety of large language models (LLMs) through a comprehensive safety performance evaluation based on eight typical safety scenarios and six types of instruction attacks.

**Data Type**: N/A

**Languages**:
- Chinese

**Similar Benchmarks**:
- N/A

**Resources**:
- [Resource](http://coai.cs.tsinghua.edu.cn/leaderboard/)
- [GitHub Repository](https://github.com/thu-coai/Safety-Prompts)

## 🎯 Purpose and Intended Users

**Goal**: To enhance safety in the deployment of large language models by providing a comprehensive assessment benchmark.

**Target Audience**:
- AI researchers
- Developers of language models

**Tasks**:
- Assessing the safety performance of large language models

**Limitations**: N/A

**Out of Scope Uses**:
- N/A

## 💾 Data

**Source**: N/A

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Manual prompt creation
- Automated safety evaluation using LLMs

**Metrics**:
- Safety scenario scores
- Instruction attack scores

**Calculation**: Proportion of safe responses to total responses in each safety scenario.

**Interpretation**: Scores reflect the safety performance of the evaluated models in handling various safety scenarios.

**Baseline Results**: N/A

**Validation**: Safety assessments conducted across 15 LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety issues in language models

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias, Output bias, Decision bias
- **Misuse**: Spreading disinformation, Improper usage, Dangerous use
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Dissemination of misleading information', 'Encouragement of harmful actions', 'Support for unethical behavior']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
