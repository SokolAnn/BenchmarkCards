# HypoGen

## 📊 Benchmark Details

**Name**: HypoGen

**Overview**: HypoGen is a dataset of approximately 5,500 structured problem-hypothesis pairs extracted from top-tier computer science conference papers, aimed at framing scientific hypothesis generation as a conditional language modeling task.

**Data Type**: problem-hypothesis pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- KG-CoI

**Resources**:
- [Resource](https://huggingface.co/datasets/UniverseTBD/hypogen-dr1)

## 🎯 Purpose and Intended Users

**Goal**: To provide a structured dataset that facilitates the generation of scientific hypotheses and evaluates large language models in the context of scientific discovery.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Hypothesis Generation
- Natural Language Generation

**Limitations**: N/A

## 💾 Data

**Source**: Papers accepted at NeurIPS 2023 and ICLR 2024.

**Size**: 5,500 examples

**Format**: JSON

**Annotation**: Structured extraction using OpenAI's o1 model.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Perplexity
- IAScore
- Idea Distinctness Index

**Calculation**: Automated metrics based on generated hypotheses compared with expert-generated ideas.

**Interpretation**: Lower perplexity indicates better fluency and coherence, while higher IAScore suggests better alignment with expert proposals.

**Baseline Results**: N/A

**Validation**: Evaluation using a test set of 50 hypotheses extracted from recent literature.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
