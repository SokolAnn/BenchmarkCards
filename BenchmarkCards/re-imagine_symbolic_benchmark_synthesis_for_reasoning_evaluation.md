# RE-IMAGINE (Symbolic Benchmark Synthesis for Reasoning Evaluation)

## 📊 Benchmark Details

**Name**: RE-IMAGINE (Symbolic Benchmark Synthesis for Reasoning Evaluation)

**Overview**: RE-IMAGINE is a framework that characterizes a hierarchy of reasoning abilities in Large Language Models (LLMs) and proposes a scalable pipeline to generate numerous problem variations across different reasoning domains, providing a systematic method for evaluating genuine reasoning versus statistical recall.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- CLadder
- CRUXEval
- Loop

**Resources**:
- [Resource](https://arxiv.org/abs/2506.15455)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the evaluation of reasoning capabilities in LLMs by generating challenging problem variations that cannot be solved through memorization alone.

**Target Audience**:
- AI Researchers
- ML Engineers
- Benchmark Developers

**Tasks**:
- Reasoning Assessment
- Mathematical Problem Solving
- Code Understanding

**Limitations**: N/A

## 💾 Data

**Source**: Varies from widely-used benchmarks reformulated into symbolic problems.

**Size**: 10,000 examples across multiple benchmarks.

**Format**: N/A

**Annotation**: Generated through an automated pipeline that ensures logic-based problem articulation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Task performance across levels of reasoning complexity

**Calculation**: Accuracy metrics are computed by running LLMs on both original and mutated benchmark questions.

**Interpretation**: Higher accuracy indicates better reasoning ability of the LLMs, particularly when assessed against problem variations.

**Baseline Results**: N/A

**Validation**: Results validated against established benchmarks (GSM8K, CLadder, etc.)

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Transparency

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
