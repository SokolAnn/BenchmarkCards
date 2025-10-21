# TheAgentCompany

## 📊 Benchmark Details

**Name**: TheAgentCompany

**Overview**: TheAgentCompany is an extensible benchmark for evaluating AI agents that interact with the world in ways similar to digital workers by browsing the web, writing code, running programs, and communicating with coworkers. It includes a simulated environment with 175 realistic and professional tasks performed in a software company.

**Data Type**: task completion

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SWE-Bench
- Mind2Web
- WebArena

**Resources**:
- [Resource](https://the-agent-company.com)
- [GitHub Repository](https://github.com/TheAgentCompany/TheAgentCompany)
- [GitHub Repository](https://github.com/TheAgentCompany/experiments)

## 🎯 Purpose and Intended Users

**Goal**: To measure the progress of LLM agents' performance on real-world professional tasks and provide insights into AI automation potential.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Task Automation
- Software Development
- Project Management
- Data Science
- Administrative Tasks
- Human Resources

**Limitations**: Tasks are generally on the more straightforward side and do not cover complex creative tasks. Current evaluation only includes two agent scaffolds without comparison to human performance.

## 💾 Data

**Source**: Tasks generated based on a simulated software company modeled after real-world job categories.

**Size**: 175 tasks

**Format**: N/A

**Annotation**: Tasks are crafted by domain experts with detailed descriptions and structured checkpoints for evaluation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Checkpoint-based evaluation

**Metrics**:
- Success Rate
- Task Completion Score

**Calculation**: Scores are calculated based on agent performance across predefined checkpoints, awarding partial credit for substantial task milestones.

**Interpretation**: Higher scores indicate better performance and more successful task execution.

**Validation**: Validation of task completion is based on an evaluation framework that includes deterministic checks and LLM reviewers for complex tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All tasks and evaluations are designed to respect user privacy and anonymize sensitive data.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
