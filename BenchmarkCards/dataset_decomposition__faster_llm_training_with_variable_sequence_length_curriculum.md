# Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum

## 📊 Benchmark Details

**Name**: Dataset Decomposition: Faster LLM Training with Variable Sequence Length Curriculum

**Overview**: This paper introduces dataset decomposition (DD), a novel method to efficiently decompose datasets of variable-length documents into buckets containing fixed-length sequences. It allows for variable sequence length training and length-based curriculum, leading to accelerated training and improved model accuracy.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- The Pile
- RefinedWeb
- RedPajama

**Resources**:
- [GitHub Repository](https://github.com/apple/ml-dataset-decomposition)

## 🎯 Purpose and Intended Users

**Goal**: To propose a method that enhances the training of large language models by improving dataset preparation and training efficiency.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Language Modeling
- Long Context Performance Evaluation

**Limitations**: The training speed gains compared to the baseline are significant only when the target sequence length is long enough.

## 💾 Data

**Source**: OpenLM training sets based on various web-sourced documents.

**Size**: 1.1 trillion tokens

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Variable Sequence Length Training
- Length-based Curriculum Sampling

**Metrics**:
- Regular evaluation metrics (accuracy)
- Multi-Document Question Answering accuracy

**Calculation**: Metrics calculated by evaluating model performance on established benchmarks and comparing results against baseline models.

**Interpretation**: Models trained using dataset decomposition show improved performance in both regular evaluations and long-context tasks compared to baseline models.

**Baseline Results**: Results indicate significant accuracy improvements with a combined LLM training acceleration of up to 6×.

**Validation**: Benchmarks validated through extensive experiments on long-context tasks and comparison against existing methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
