# DivLogicEval (Diverse Logical Reasoning Evaluation)

## 📊 Benchmark Details

**Name**: DivLogicEval (Diverse Logical Reasoning Evaluation)

**Overview**: DivLogicEval is a benchmarking framework specifically designed to evaluate logical reasoning capabilities in Large Language Models (LLMs). It highlights the importance of isolating logical reasoning from other reasoning types and addresses limitations of existing benchmarks in terms of language diversity and bias.

**Data Type**: multiple-choice question answering (MCQA)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ReClor
- LogiQA

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust evaluation framework for assessing logical reasoning skills in LLMs with a focus on language diversity and bias mitigation.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Logical Reasoning
- Question Answering

**Limitations**: The methodology may lead to some grammatical mistakes due to synthesizing and integrating data from existing benchmarks.

## 💾 Data

**Source**: Synthetic dataset constructed from a predefined set of symbolic logic propositions and diverse natural sentences sampled from existing NLI datasets.

**Size**: 12,589 instances

**Format**: N/A

**Annotation**: Automatically generated and transformed via a framework involving logic expressions and diverse natural language sentences.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Circular
- PartialCircular

**Calculation**: The PartialCircular metric assigns a score based on the number of correct predictions across multiple mutants and penalizes uncertainty in predicted distributions.

**Interpretation**: Higher scores indicate higher confidence in correct predictions while considering the uncertainty of the model's output distribution.

**Baseline Results**: Accuracy and other metrics were compared with existing benchmarks like ReClor and LogiQA.

**Validation**: DivLogicEval was validated against standard metrics to establish its reliability and effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
