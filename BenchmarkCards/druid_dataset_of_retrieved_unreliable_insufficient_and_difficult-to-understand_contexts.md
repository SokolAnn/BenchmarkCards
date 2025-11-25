# DRUID (Dataset of Retrieved Unreliable, Insufficient and Difficult-to-understand contexts)

## 📊 Benchmark Details

**Name**: DRUID (Dataset of Retrieved Unreliable, Insufficient and Difficult-to-understand contexts)

**Overview**: DRUID introduces a dataset with real-world queries and contexts annotated for stance, focusing on the automated claim verification task.

**Data Type**: claim-evidence pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CounterFact
- ConflictQA

**Resources**:
- [GitHub Repository](https://github.com/copenlu/context-utilisation-for-RAG)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate studies of context usage and failures in real-world scenarios, particularly for retrieval-augmented generation tasks.

**Target Audience**:
- ML Researchers
- Model Developers
- Fact Checkers

**Tasks**:
- Claim Verification

**Limitations**: The dataset is focused on claim verification, which may limit its applicability to other RAG tasks.

## 💾 Data

**Source**: Real-world claims collected from diverse fact-checking websites and evidence retrieved using automated methods.

**Size**: 5,490 samples

**Format**: JSON

**Annotation**: Manually annotated for evidence relevance and stance by crowdsource workers.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- ACU score (Accumulated Context Usage)

**Calculation**: The ACU score measures the difference in model predictions with and without evidence, normalized for meaningful comparison.

**Interpretation**: A higher ACU score indicates better context usage by the model, reflecting its ability to leverage retrieved evidence effectively.

**Validation**: DRUID is compared against existing synthetic datasets (CounterFact, ConflictQA) to validate its effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: The dataset includes data from various international fact-checking sources, which may introduce biases.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset does not retain personal information about annotators and compensates them fairly for their work.

**Data Licensing**: Not Applicable

**Consent Procedures**: Annotators were informed about the use of their data and consented to their participation.

**Compliance With Regulations**: The dataset adheres to ethical standards in data collection and annotation.
