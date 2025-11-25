# TRAIT (Personality Testset for LLMs)

## 📊 Benchmark Details

**Name**: TRAIT (Personality Testset for LLMs)

**Overview**: TRAIT is a benchmark consisting of 8,000 multi-choice questions designed to assess the personality of Large Language Models (LLMs), built on the Big Five Inventory (BFI) and Short Dark Triad (SD-3) questionnaires, enhanced with the ATOMIC10× knowledge graph.

**Data Type**: multi-choice questions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)

**Resources**:
- [GitHub Repository](https://github.com/pull-ups/TRAIT)
- [Resource](https://huggingface.co/datasets/mirlab/TRAIT)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reliable and valid method for measuring the personality traits of Large Language Models (LLMs).

**Target Audience**:
- ML Researchers
- Psychologists
- AI Developers

**Tasks**:
- Personality Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from psychometrically validated questionnaires and augmented with a large-scale commonsense knowledge graph (ATOMIC10×).

**Size**: 8,000 questions

**Format**: Multi-choice

**Annotation**: Automated generation and manual curation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Content Validity
- Internal Validity
- Refusal Rate
- Reliability

**Calculation**: Validity and reliability are measured through established psychometric methods.

**Interpretation**: High scores indicate better personality alignment with expected behaviors.

**Baseline Results**: Compared to existing personality assessment tools, TRAIT achieved the highest scores in reliability and validity metrics.

**Validation**: TRAIT was validated by psychological professionals who confirmed the quality of the test.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Data poisoning

**Demographic Analysis**: The dataset utilizes English language models and acknowledges potential cultural biases inherent in the generated content.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Care was taken to ensure the training data was stripped of identifiable information and handled ethically during its construction.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
