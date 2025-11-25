# Neuron State-Based Cross-Lingual Alignment (NeuronXA)

## 📊 Benchmark Details

**Name**: Neuron State-Based Cross-Lingual Alignment (NeuronXA)

**Overview**: NeuronXA assesses the cross-lingual alignment capabilities of large language models by quantifying neuron activation likelihood in response to parallel corpora across multiple languages.

**Data Type**: parallel sentence pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- French
- German
- Italian
- Spanish
- Russian
- Arabic
- Hindi
- Japanese

**Similar Benchmarks**:
- MEXA
- m-MMLU
- Belebele

**Resources**:
- [Resource](https://arxiv.org/abs/2507.14900)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust evaluation framework for assessing the multilingual capabilities of large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Cross-Lingual Transfer
- Multilingual Similarity Evaluation

**Limitations**: The evaluation method requires access to model intrinsic representations, limiting its application for closed-source models.

## 💾 Data

**Source**: FLORES-200 and Tatoeba parallel sentence datasets.

**Size**: 100 parallel sentence pairs

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Neuron State-Based Alignment Evaluation

**Metrics**:
- Pearson correlation

**Calculation**: Alignment scores are calculated based on neuron activation states using significant cosine similarity metrics.

**Interpretation**: Higher alignment scores correlate strongly with better performance on multilingual tasks.

**Baseline Results**: Pearson correlation of NeuronXA with downstream tasks performance reached 0.9556.

**Validation**: Evaluated across various multilingual benchmarks and tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
