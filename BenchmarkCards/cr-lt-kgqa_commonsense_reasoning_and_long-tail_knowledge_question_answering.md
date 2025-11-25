# CR-LT-KGQA (Commonsense Reasoning and Long-Tail Knowledge Question Answering)

## 📊 Benchmark Details

**Name**: CR-LT-KGQA (Commonsense Reasoning and Long-Tail Knowledge Question Answering)

**Overview**: CR-LT-KGQA is a novel Knowledge Graph Question Answering dataset that requires commonsense reasoning and focuses on long-tail entities, posing significant challenges for hallucination-prone large language models.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/D3Mlab/cr-lt-kgqa)

## 🎯 Purpose and Intended Users

**Goal**: To provide a challenging KGQA dataset that requires commonsense reasoning and targets long-tail knowledge.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering
- Claim Verification

**Limitations**: N/A

## 💾 Data

**Source**: Wikidata

**Size**: 350 queries

**Format**: N/A

**Annotation**: Annotated by experts through a manual verification process.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score
- FActScore

**Calculation**: Metrics are calculated based on the performance of LLMs in answering queries and verifying claims.

**Interpretation**: Higher scores indicate better performance in terms of correctness and reasoning reliability.

**Baseline Results**: Evaluation on existing LLMs shows significant performance drops in long-tail settings.

**Validation**: Baseline evaluations were established using GPT-3.5 Turbo with both zero-shot and few-shot settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
