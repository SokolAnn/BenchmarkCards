# SATA-B ENCH (Select All That Apply Benchmark)

## 📊 Benchmark Details

**Name**: SATA-B ENCH (Select All That Apply Benchmark)

**Overview**: SATA-B ENCH is a benchmark suite specifically designed to evaluate and enhance the performance of Large Language Models (LLMs) on Select All That Apply (SATA) tasks across diverse domains, reflecting real-world scenarios requiring the identification of multiple correct answers.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Law
- Biomedicine
- Reading Comprehension
- Toxicity Identification
- News Classification

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- ARC

**Resources**:
- [GitHub Repository](https://github.com/sata-bench/sata-bench)
- [Resource](https://huggingface.co/datasets/sata-bench/sata-bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of LLMs in identifying multiple correct choices in SATA questions and to promote robust decision-making in realistic applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Curated benchmark dataset featuring 1,604 human-validated questions.

**Size**: 1,604 questions

**Format**: JSON

**Annotation**: Human validation and curation to ensure clarity, diversity, and correct labeling.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Choice Funnel decoding strategy

**Metrics**:
- Exact Match (EM)
- Jaccard Index (JI)
- Mean Average Precision (Precision)
- Mean Average Recall (Recall)
- Selection Probability Divergence (SPD)
- Count Bias Metrics

**Calculation**: Metrics calculated based on model predictions compared to ground truth answers.

**Interpretation**: Higher Exact Match and Precision scores indicate better model performance in identifying all correct answers.

**Baseline Results**: Top-performing models achieve a maximum exact match of 41.8%.

**Validation**: Rigorous human validation across multiple cycles of review.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy, Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Selection bias', 'Count bias']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
