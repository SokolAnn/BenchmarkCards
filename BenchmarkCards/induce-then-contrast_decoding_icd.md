# Induce-then-Contrast Decoding (ICD)

## 📊 Benchmark Details

**Name**: Induce-then-Contrast Decoding (ICD)

**Overview**: A decoding strategy proposed to alleviate hallucinations in large language models by first inducing hallucinations in a weaker model and then penalizing these hallucinations during generation.

**Data Type**: N/A

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TruthfulQA
- FACTSCORE

**Resources**:
- [GitHub Repository](https://github.com/hillzhang1999/ICD)

## 🎯 Purpose and Intended Users

**Goal**: To improve the factual accuracy of language models in text generation.

**Target Audience**:
- Research community
- AI practitioners

**Tasks**:
- Hallucination reduction
- Text generation

**Limitations**: Additional computational costs due to contrastive decoding.

**Out of Scope Uses**:
- Direct factual data enhancement without hallucination methods

## 💾 Data

**Source**: HaluEval dataset

**Size**: 10,000 samples for fine-tuning

**Format**: Pairs of prompts and responses

**Annotation**: Hallucinated and factual samples differentiated

## 🔬 Methodology

**Methods**:
- Induce-then-Contrast Decoding (ICD)
- Fine-tuning
- Prompt-based induction

**Metrics**:
- TruthfulQA scores (MC1, MC2, MC3)
- FACTSCORE factual precision

**Calculation**: Evaluation based on performance improvements over baseline models.

**Interpretation**: Observing improvements in truthfulness and factuality post-implementation of ICD.

**Validation**: Consistency in improvements across different LLM sizes and families.

## ⚠️ Targeted Risks

**Risk Categories**:
- Hallucination in outputs
- Misuse of generated factual data

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Transparency**: Lack of training data transparency
- **Misuse**: Spreading disinformation

**Demographic Analysis**: N/A

**Potential Harm**: Factual inaccuracies may lead to misinformation if models are not trusted.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Utilized human annotators for evaluating hallucinations.

**Compliance With Regulations**: Not Applicable
