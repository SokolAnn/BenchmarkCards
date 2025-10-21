# Harnessing Dataset Cartography for Improved Compositional Generalization in Transformers

## 📊 Benchmark Details

**Name**: Harnessing Dataset Cartography for Improved Compositional Generalization in Transformers

**Overview**: This paper introduces a method utilizing dataset cartography to enhance compositional generalization in Transformer models, significantly improving performance on CFQ and COGS datasets.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CFQ
- COGS

**Resources**:
- [GitHub Repository](https://github.com/cyberiada/cartography-for-compositionality)

## 🎯 Purpose and Intended Users

**Goal**: To improve compositional generalization abilities in Transformer models using dataset cartography.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Generation
- Semantic Parsing

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic datasets, specifically CFQ and COGS.

**Size**: 95,743 training samples for CFQ; 24,155 training samples for COGS.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- BLEU Score
- Inverse Perplexity

**Calculation**: Metrics are calculated based on sequence generation accuracy and confidence measures.

**Interpretation**: Higher accuracy indicates better model performance; BLEU score measures the overlap of generated sequences with the ground truth.

**Baseline Results**: 100% training dataset performance used for comparison.

**Validation**: Results validated through multiple training runs and comparisons against full dataset training.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
