# HALOGEN

## 📊 Benchmark Details

**Name**: HALOGEN

**Overview**: HALOGEN is a comprehensive hallucination benchmark consisting of 10,923 prompts for generative models spanning nine domains. It includes automatic high-precision verifiers for each use case that decompose LLM generations into atomic units and verify each unit against a high-quality knowledge source.

**Data Type**: Text

**Domains**:
- Programming
- Scientific Attribution
- Summarization
- Text Simplification
- Biographies
- Historical Events
- Rationalization (Binary)
- Rationalization (Numerical)
- False Presuppositions

**Languages**:
- English

**Similar Benchmarks**:
- TruthfulQA
- FactScore
- SciFact

**Resources**:
- [Resource](https://halogen-hallucinations.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To measure and identify model hallucinations in generative large language models.

**Target Audience**:
- AI Researchers
- Natural Language Processing Practitioners
- Data Scientists

**Tasks**:
- Evaluate the propensity of LLMs to hallucinate
- Investigate potential sources of hallucination

**Limitations**: The reliability of benchmark scores is limited by the accuracy of automated verification techniques.

**Out of Scope Uses**:
- Creative writing
- Opinion-based responses

## 💾 Data

**Source**: Generated prompts and responses from language models.

**Size**: 10,923 prompts

**Format**: Text

**Annotation**: Prompts are annotated according to identified hallucinations and factual inaccuracies.

## 🔬 Methodology

**Methods**:
- Decomposition of text into atomic units
- Verification against external knowledge sources

**Metrics**:
- Hallucination Score
- Response Ratio
- Utility Score

**Calculation**: Metrics are calculated based on the proportion of hallucinations found in the model output based on verification results.

**Interpretation**: Lower hallucination scores indicate more accurate model performance.

**Validation**: Validation was conducted using automatic verifiers against known data sources.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Transparency
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Data contamination, Poor model accuracy
- **Fairness**: Data bias, Output bias
- **Transparency**: Lack of training data transparency
- **Privacy**: Personal information in data

**Potential Harm**: Potential misinformation and reinforcement of biases due to model hallucinations.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data primarily consists of publicly available prompts and model outputs.

**Data Licensing**: All datasets used are permissively licensed including MIT and Apache licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
