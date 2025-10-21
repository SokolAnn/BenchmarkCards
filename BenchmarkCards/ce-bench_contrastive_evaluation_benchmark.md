# CE-Bench (Contrastive Evaluation Benchmark)

## 📊 Benchmark Details

**Name**: CE-Bench (Contrastive Evaluation Benchmark)

**Overview**: CE-Bench is a novel, lightweight contrastive evaluation benchmark for sparse autoencoders, designed to measure interpretability by analyzing neuron activation patterns across semantically contrastive contexts.

**Data Type**: contrastive story pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SAEBench

**Resources**:
- [GitHub Repository](https://github.com/jbloomAus/SAELens)
- [Resource](https://huggingface.co/datasets/CE-Bench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of CE-Bench is to provide a reliable and reproducible evaluation framework for sparse autoencoders without reliance on external language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Interpretability Evaluation

**Limitations**: The dataset may bias the evaluation toward models that better capture GPT-4's stylistic and semantic regularities, and its generalizability to varied contexts remains uncertain.

## 💾 Data

**Source**: Constructed using curated contrastive story pairs generated with GPT-4 and human validation.

**Size**: 5,000 pairs

**Format**: JSON

**Annotation**: Semi-automated with human validation.

## 🔬 Methodology

**Methods**:
- Correlation analysis with existing benchmarks
- Contrastive scoring
- Sparsity-aware scoring

**Metrics**:
- Spearman Correlation
- Pearson Correlation
- Correct Ranking Pair Ratio (CRPR)

**Calculation**: Metrics are calculated based on neuron activation comparisons between contrastive story pairs.

**Interpretation**: Higher scores indicate greater interpretability of the sparse autoencoders.

**Validation**: Results align with existing benchmarks, showing strong correlation under multiple alignment metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The evaluation may reflect certain demographic biases originating from the dataset population.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
