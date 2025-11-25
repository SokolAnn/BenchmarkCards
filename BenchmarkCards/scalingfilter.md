# ScalingFilter

## 📊 Benchmark Details

**Name**: ScalingFilter

**Overview**: ScalingFilter is a novel approach that evaluates text quality based on the perplexity difference between two language models trained on the same data, eliminating the influence of reference datasets.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To propose a quality filtering method that assesses text quality without the biases introduced by reference datasets, thereby enhancing diversity and performance of language models.

**Target Audience**:
- ML Researchers
- Model Developers
- Data Curators

**Tasks**:
- Text Classification
- Question Answering

**Limitations**: ScalingFilter relies on perplexity difference which may miss nuanced aspects of text quality like factual accuracy or bias. It requires significant computational resources for large datasets.

## 💾 Data

**Source**: Five CommonCrawl dumps processed through the CCNet pipeline, yielding 500 GB of text data for quality filtering experiments.

**Size**: 500 GB

**Format**: Raw text files

**Annotation**: Calculated quality factors based on perplexity differences using trained language models.

## 🔬 Methodology

**Methods**:
- Model-based evaluation

**Metrics**:
- Zero-shot accuracy

**Calculation**: Metrics calculated by training a 1.3B model on filtered data and evaluating performance on several downstream tasks.

**Interpretation**: Higher zero-shot performance and semantic diversity indicate better data quality and diversity.

**Baseline Results**: Compared with existing quality filtering methods and achieved improvements in accuracy and semantic diversity.

**Validation**: Results compared against baseline, random selection, and existing methods for performance verification.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential for biased model outputs due to inherent biases in filtered data.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
