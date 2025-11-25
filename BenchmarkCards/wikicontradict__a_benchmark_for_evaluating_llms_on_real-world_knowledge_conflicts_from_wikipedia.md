# WikiContradict: A Benchmark for Evaluating LLMs on Real-World Knowledge Conflicts from Wikipedia

## 📊 Benchmark Details

**Name**: WikiContradict: A Benchmark for Evaluating LLMs on Real-World Knowledge Conflicts from Wikipedia

**Overview**: WikiContradict is a benchmark consisting of 253 high-quality, human-annotated instances designed to assess LLM performance when augmented with retrieved passages containing real-world knowledge conflicts.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TruthfulQA
- FreshQA
- HaluEval
- HalluQA
- FELM

**Resources**:
- [Resource](https://ibm.biz/wikicontradict)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of LLMs on handling real-world knowledge conflicts.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: Limited to English language instances.

## 💾 Data

**Source**: Wikipedia articles containing inconsistency tags

**Size**: 253 instances

**Format**: JSON

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: Human evaluations yield metrics based on responses from LLMs to annotated instances.

**Interpretation**: An answer is considered correct if it accurately reflects the contradictory nature of the passages.

**Baseline Results**: N/A

**Validation**: Moderate to substantial inter-annotator agreement on human evaluations.

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

**Data Licensing**: MIT License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
