# Drowzee: Metamorphic Testing for Fact-Conflicting Hallucination Detection in Large Language Models

## 📊 Benchmark Details

**Name**: Drowzee: Metamorphic Testing for Fact-Conflicting Hallucination Detection in Large Language Models

**Overview**: This work addresses the challenge of detecting fact-conflicting hallucinations (FCH) in large language models (LLMs) by introducing a novel testing framework utilizing logic programming and metamorphic testing.

**Data Type**: Factual knowledge triples

**Domains**:
- Culture
- Geography
- Health
- History
- Mathematics
- Natural Sciences
- People
- Society
- Technology

**Languages**:
- English

**Similar Benchmarks**:
- TruthfulQA
- HaluEval
- KoLA

**Resources**:
- [Resource](GitHub repository for Drowzee)

## 🎯 Purpose and Intended Users

**Goal**: To automatically generate and test hallucination cases in LLMs to ensure factual accuracy.

**Target Audience**:
- Researchers in AI and machine learning
- Developers of large language models
- Academic institutions

**Tasks**:
- Detecting fact-conflicting hallucinations in LLM outputs
- Validating reasoning processes of LLM responses
- Developing benchmarks for hallucination detection

**Limitations**: None

**Out of Scope Uses**:
- Testing non-LLM systems
- Applications outside of language processing

## 💾 Data

**Source**: Wikipedia and Wikidata

**Size**: Comprehensive total of 7,200 test cases

**Format**: Factual knowledge triples

**Annotation**: Automatically generated with ground truth answers

## 🔬 Methodology

**Methods**:
- Logic programming
- Metamorphic testing
- Semantic-aware testing oracles

**Metrics**:
- Hallucination rates
- Semantic similarity scores

**Calculation**: Hallucination rates calculated based on the responses of LLMs compared to ground truth.

**Interpretation**: Analyzing logical reasoning between LLM responses and factual knowledge.

**Validation**: Responses validated through semantic similarity assessment between LLM outputs and ground truth.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Data privacy rights alignment

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Ensuring privacy through the use of publicly available knowledge bases.

**Data Licensing**: Data used is from open-source datasets (e.g., Wikipedia, Wikidata).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
