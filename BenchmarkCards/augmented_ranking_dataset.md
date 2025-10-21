# Augmented Ranking Dataset

## 📊 Benchmark Details

**Name**: Augmented Ranking Dataset

**Overview**: The paper presents a method for augmenting preference datasets for preference optimization in large language models and introduces a multi-response-based training method.

**Data Type**: ranking data

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/Intel/orca_dpo_pairs)

## 🎯 Purpose and Intended Users

**Goal**: To produce a large-scale preference dataset for training large language models and improve their response quality based on human preferences.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Preference Optimization

**Limitations**: N/A

## 💾 Data

**Source**: Seed dataset consisting of human-labeled preference pairs and generated data from language models.

**Size**: 50,000 preference pairs

**Format**: JSON

**Annotation**: Automatically generated and labeled by language models.

## 🔬 Methodology

**Methods**:
- Data augmentation
- Multi-response training

**Metrics**:
- Win rate in instruction-following tasks

**Calculation**: The performance is calculated based on win rates against baseline models in instruction tasks.

**Interpretation**: Higher win rates indicate better performance in following human instructions.

**Validation**: Results validated through the AlpacaEval and MT-bench benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
