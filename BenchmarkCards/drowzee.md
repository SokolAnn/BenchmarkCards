# DROWZEE

## 📊 Benchmark Details

**Name**: DROWZEE

**Overview**: DROWZEE is an end-to-end metamorphic testing framework designed to detect fact-conflicting hallucinations in large language models (LLMs) using temporal logic and a comprehensive factual knowledge base.

**Data Type**: Various factual knowledge derived from knowledge databases like Wikipedia.

**Domains**:
- Culture and the Arts
- Geography and Places
- Health and Fitness
- History and Events
- Mathematics and Logic
- Natural and Physical Sciences
- Society and Social Sciences
- Technology and Applied Sciences

**Languages**:
- English

**Similar Benchmarks**:
- TruthfulQA
- HaluEval
- KoLA

**Resources**:
- [Resource](Source code and dataset are publicly available)

## 🎯 Purpose and Intended Users

**Goal**: To systematically detect fact-conflicting hallucinations in LLMs and enhance their reliability in producing accurate information.

**Target Audience**:
- Researchers in AI and NLP
- Developers of LLM applications
- Data scientists

**Tasks**:
- Detecting hallucinations in LLM outputs
- Validating logical reasoning in LLMs
- Evaluating the performance of LLMs across various domains

**Limitations**: The system relies on the quality and coverage of the knowledge databases, which can impact its effectiveness.

**Out of Scope Uses**:
- General LLM application outside of factual accuracy assessment
- Use without proper knowledge bases

## 💾 Data

**Source**: Wikipedia and Wikidata

**Size**: 54,483 entities and 1,647,206 facts

**Format**: Structured knowledge as three-element predicates

**Annotation**: Generated knowledge is transformed into Q&A pairs for testing.

## 🔬 Methodology

**Methods**:
- Temporal logic-based reasoning
- Metamorphic testing
- Semantic-aware oracles

**Metrics**:
- Hallucination rates
- Accuracy of responses
- Response validation against ground truth

**Calculation**: Utilizes Jaccard Similarity for edge and node comparisons of LLM responses against ground truth.

**Interpretation**: Analyzes the logical and semantic structures of the LLM outputs to determine the occurrence of hallucinations.

**Baseline Results**: Hallucination rates ranged from 24.7% to 59.8% across tested models.

**Validation**: Utilizes semantic structure similarity comparisons and metamorphic oracles for validation of LLM outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy
- Fairness
- Explainability
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy, Data contamination
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Explainability**: Unexplainable output
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The framework ensures the handling of data complies with privacy standards as it uses publicly available datasets.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
