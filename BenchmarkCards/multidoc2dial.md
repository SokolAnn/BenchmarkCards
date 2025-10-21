# MultiDoc2Dial

## 📊 Benchmark Details

**Name**: MultiDoc2Dial

**Overview**: MultiDoc2Dial is a new dataset and task on modeling goal-oriented dialogues grounded in multiple documents, addressing scenarios where conversations are based on several sub-goals related to different documents.

**Data Type**: dialogue turns grounded in multiple documents

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Doc2Dial

**Resources**:
- [Resource](https://doc2dial.github.io/multidoc2dial/)

## 🎯 Purpose and Intended Users

**Goal**: To model goal-oriented dialogues that involve multiple topics grounded in various documents, reflecting real-life conversation scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Grounding Span Generation
- Agent Response Generation

**Limitations**: N/A

## 💾 Data

**Source**: Crowdsourced dialogues and existing data from Doc2Dial dataset

**Size**: 4,796 dialogues with an average of 14 turns

**Format**: N/A

**Annotation**: Annotated with role, dialogue act, human-generated utterance, and grounding span with document information.

## 🔬 Methodology

**Methods**:
- Retriever-Reader Architecture
- End-to-End Generation Task

**Metrics**:
- F1 Score
- Exact Match (EM)
- BLEU Score

**Calculation**: Full sentence-level metrics calculated based on generation output and retrieved documents.

**Interpretation**: Higher scores indicate better performance in grounding and response generation tasks.

**Validation**: Trained and tested on specific train-validation-test split for varying complexity of dialogues.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**
- **Societal Impact**

**Demographic Analysis**: N/A

**Potential Harm**: Potential bias in simulated user queries due to crowdsourced data collection.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
