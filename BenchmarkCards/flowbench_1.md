# FlowBench

## 📊 Benchmark Details

**Name**: FlowBench

**Overview**: FlowBench is the first benchmark for workflow-guided planning, covering 51 scenarios from 6 domains, intended to evaluate the efficacy of LLM-based agents using various formats of workflow knowledge.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Robotics
- Healthcare
- Logistics
- E-tailing
- Customer Service

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLM-based agents in workflow-guided planning across various scenarios and formats of workflow knowledge.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Task Planning
- Dialogue Management

**Limitations**: FlowBench may not cover all potential formats and relies on human verification for quality assurance.

## 💾 Data

**Source**: Constructed through task collection, workflow organization, and session generation.

**Size**: 536 sessions

**Format**: N/A

**Annotation**: Expert annotations combined with GPT-4 for knowledge formatting.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Tool Invocation F1 Score
- Success Rate
- Task Progress

**Calculation**: Tool invocation is evaluated based on precision, recall, and F1 score. Session-level success rate is calculated by checking if all user goals are met during interaction.

**Interpretation**: A higher score indicates better planning and interaction capabilities of LLM agents.

**Baseline Results**: GPT-4o demonstrated varying performance with F1 Scores and success rates across evaluations.

**Validation**: Data quality was assured through multiple verification stages involving human annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Human annotators were instructed to filter out potential ethical concerns during data collection.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
