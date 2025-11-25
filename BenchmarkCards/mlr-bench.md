# MLR-Bench

## 📊 Benchmark Details

**Name**: MLR-Bench

**Overview**: MLR-Bench is a comprehensive benchmark for evaluating AI agents on open-ended machine learning research. It includes 201 research tasks, an automated evaluation framework called MLR-Judge, and a modular agent called MLR-Agent to conduct research across multiple stages.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MLE-bench
- MLAgentBench
- PaperBench

**Resources**:
- [GitHub Repository](https://github.com/chchenhui/mlrbench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic framework for evaluating AI agents in conducting open-ended machine learning research, improving their reliability and transparency.

**Target Audience**:
- ML Researchers
- AI Developers

**Tasks**:
- Research Idea Generation
- Research Proposal Generation
- Experimentation
- Paper Writing

**Limitations**: N/A

## 💾 Data

**Source**: 201 real-world research tasks sourced from NeurIPS, ICLR, and ICML workshops.

**Size**: 201 tasks

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated evaluation using LLM-based judges
- Stepwise evaluation
- End-to-end evaluation

**Metrics**:
- Consistency
- Clarity
- Novelty
- Feasibility
- Significance

**Calculation**: Each research output is evaluated based on criteria such as clarity, consistency, and novelty.

**Interpretation**: Higher scores in evaluating AI-generated research indicate better performance in producing quality research outputs.

**Baseline Results**: N/A

**Validation**: Validated through human evaluations showing high agreement with expert reviewers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Trustworthiness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Transparency**: Lack of training data transparency
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
