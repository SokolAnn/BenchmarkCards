# WikiFactDiff

## 📊 Benchmark Details

**Name**: WikiFactDiff

**Overview**: WikiFactDiff is a large dataset for factual knowledge updates of language models, depicting the evolution of knowledge between two dates via new, obsolete, and static facts.

**Data Type**: subject-relation-object triples

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CounterFact
- zsRE

**Resources**:
- [GitHub Repository](https://github.com/Orange-OpenSource/WikiFactDiff)
- [Resource](https://huggingface.co/datasets/OrangeInnov/WikiFactDiff)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for evaluating factual knowledge update algorithms in language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Knowledge Update

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from raw snapshots of the Wikidata knowledge base.

**Size**: 327,688 updates

**Format**: N/A

**Annotation**: Automatically generated updates based on changes in Wikidata.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Efficacy
- Generalization
- Specificity
- Fluency

**Calculation**: Metrics are calculated based on the updated model's ability to correctly predict facts from cloze tests.

**Interpretation**: Good performance is indicated by high efficacy and low bleedover.

**Baseline Results**: ROME outperforms other algorithms with high efficacy and minimal impact on specificity.

**Validation**: Evaluation of existing update algorithms on the WikiFactDiff dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
