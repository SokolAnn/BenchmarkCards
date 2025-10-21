# ToxSyn-PT

## 📊 Benchmark Details

**Name**: ToxSyn-PT

**Overview**: ToxSyn-PT is the first large-scale Portuguese corpus that enables fine-grained hate-speech classification across nine legally protected minority groups. The dataset contains 53,274 synthetic sentences annotated for toxicity, discourse type, and target group, created through a novel four-stage generation pipeline.

**Data Type**: synthetic sentences

**Domains**:
- Natural Language Processing

**Languages**:
- Portuguese

**Similar Benchmarks**:
- HateBR
- OFFCOMBR-3
- OLID-BR
- TuPy-E

**Resources**:
- [Resource](https://huggingface.co/datasets/ToxSyn-PT)

## 🎯 Purpose and Intended Users

**Goal**: To advance research on synthetic data and hate-speech detection in low-resource settings.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Binary Classification
- Multi-label Classification

**Limitations**: Each sentence is annotated with a single toxicity label and one target group, precluding intersectional or multi-target cases; overlapping abuses remain unmodeled.

## 💾 Data

**Source**: Generated through a four-stage pipeline: seed dataset, expansion using LLM, paraphrase augmentation, and implicit-hate enrichment.

**Size**: 53,274 sentences

**Format**: N/A

**Annotation**: LLM-generated with controlled annotations for toxicity and demographic targets.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Macro-Recall
- ROC AUC

**Calculation**: Metrics are calculated based on the model's performance on the dataset across multiple tasks.

**Interpretation**: Higher scores indicate stronger model performance in detecting hate speech.

**Baseline Results**: Models fine-tuned on ToxSyn-PT achieved macro-recall of 0.64 and ROC AUC of 0.73.

**Validation**: Model evaluation conducted against existing benchmarks and synthesized versions of benchmark datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: The dataset includes nine legally protected minority groups.

**Potential Harm**: ['Toxicity towards defined minority groups']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Synthetic dataset does not include personal information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
