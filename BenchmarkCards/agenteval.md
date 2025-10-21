# AgentEval

## 📊 Benchmark Details

**Name**: AgentEval

**Overview**: AgentEval is a novel framework designed to simplify the utility verification process of LLM-powered applications by automatically proposing criteria tailored to the application's purpose and assessing the utility against these criteria.

**Data Type**: task utility criteria

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MATH (Mathematics Dataset)
- ALFWorld

**Resources**:
- [GitHub Repository](https://github.com/microsoft/autogen/blob/main/notebook/agenteval_cq_math.ipynb)

## 🎯 Purpose and Intended Users

**Goal**: To assess the alignment between application behavior and end-user goals, providing insights for application developers to improve functionality.

**Target Audience**:
- Application Developers
- ML Researchers

**Tasks**:
- Task Utility Verification

**Limitations**: N/A

## 💾 Data

**Source**: Open-source datasets, specifically the MATH dataset and ALFWorld

**Size**: 12,500 problems for MATH dataset, 134 tasks for ALFWorld

**Format**: N/A

**Annotation**: Automatically generated criteria based on task description and examples of task execution.

## 🔬 Methodology

**Methods**:
- Critic Agent Evaluation
- Quantifier Agent Assessment

**Metrics**:
- Task Utility Score
- Criteria Performance Metrics

**Calculation**: Task utility is assessed based on suggested criteria by the CriticAgent and quantified by the QuantifierAgent.

**Interpretation**: A higher score indicates better alignment with user goals and utility in accomplishing tasks.

**Baseline Results**: N/A

**Validation**: Criteria effectiveness is validated through task-specific assessments across multiple dataset scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
