# ACCESS (Abstra CtCausal Event Di Scovery and ReaSoning)

## 📊 Benchmark Details

**Name**: ACCESS (Abstra CtCausal Event Di Scovery and ReaSoning)

**Overview**: ACCESS is designed for discovery and reasoning over abstract causal events, focusing on causality of everyday life events at an abstraction level. The benchmark includes 725 event abstractions and 1,494 causal relations.

**Data Type**: causal pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CRAB
- GLUCOSE

**Resources**:
- [GitHub Repository](https://github.com/isVy08/ACCESS)

## 🎯 Purpose and Intended Users

**Goal**: To explore event causality at the abstraction level as a more efficient representation of knowledge.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Causal Discovery
- Event Abstraction

**Limitations**: ACCESS is built upon GLUCOSE with a scope limited to everyday children's stories, which may introduce biases.

## 💾 Data

**Source**: GLUCOSE (Mostafazadeh et al., 2020)

**Size**: 1,494 causal pairs

**Format**: N/A

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Statistical structure learning algorithms
- Human annotation
- Clustering algorithms

**Metrics**:
- Precision
- Recall
- F1 Score
- Accuracy

**Calculation**: Metrics are calculated based on the performance of models against the causal pairs and event abstractions extracted.

**Interpretation**: Higher scores indicate better performance in identifying causal relations and reasoning.

**Baseline Results**: N/A

**Validation**: Validated through expert annotation and comparison with existing benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All necessary measures have been taken to ensure privacy and informed consent during data collection.

**Data Licensing**: Not Applicable

**Consent Procedures**: Each annotator was required to adhere to ethical standards and take breaks as needed during the annotation process.

**Compliance With Regulations**: Not Applicable
