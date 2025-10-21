# Reasoning Core

## 📊 Benchmark Details

**Name**: Reasoning Core

**Overview**: Reasoning Core is a scalable environment for Reinforcement Learning with Verifiable Rewards (RLVR), designed to advance foundational symbolic reasoning in Large Language Models (LLMs) through procedurally generated problems across core formal domains.

**Data Type**: text

**Domains**:
- Artificial Intelligence
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Reasoning Gym
- Relational Reasoning Benchmark

**Resources**:
- [GitHub Repository](https://github.com/sileod/reasoning_core)
- [Resource](https://huggingface.co/datasets/reasoning-core/rc1)

## 🎯 Purpose and Intended Users

**Goal**: To provide an adaptive and scalable framework that enhances the reasoning capabilities of large language models through rigorous problem-solving in symbolic reasoning domains.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Symbolic Reasoning
- Problem Solving

**Limitations**: N/A

## 💾 Data

**Source**: Generated problems across various symbolic reasoning domains including first-order logic, PDDL planning, and context-free grammar parsing.

**Size**: Virtually infinite instances

**Format**: N/A

**Annotation**: Automatically verified through external solvers

## 🔬 Methodology

**Methods**:
- Automated metrics
- Verification via external tools

**Metrics**:
- Zero-shot evaluation performance

**Calculation**: Average rewards obtained by models on various tasks through zero-shot evaluations.

**Interpretation**: Higher rewards indicate better reasoning performance by the models across generated instances.

**Baseline Results**: Initial evaluations of models like GPT-5 across different difficulty levels showed varying capabilities.

**Validation**: Tests using zero-shot evaluations on frontier LLMs to ascertain task difficulty and model adaptability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
