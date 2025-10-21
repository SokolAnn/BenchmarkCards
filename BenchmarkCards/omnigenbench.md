# OmniGenBench

## 📊 Benchmark Details

**Name**: OmniGenBench

**Overview**: OmniGenBench is a framework dedicated to genomic foundation model (GFM) benchmarking. It standardizes benchmark suites and automates benchmarking for a wide range of open-source GFMs, integrating millions of genomic sequences across hundreds of genomic tasks from large-scale benchmarks.

**Data Type**: genomic sequences

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- N/A

**Similar Benchmarks**:
- RNA Genomic Benchmark (RGB)
- Plant Genomic Benchmark (PGB)
- Genomic Understanding Evaluation (GUE)
- Genomic Benchmarks (GB)

**Resources**:
- [GitHub Repository](https://github.com/yangheng95/OmniGenomeBench)

## 🎯 Purpose and Intended Users

**Goal**: To address the challenges of GFM benchmarking and application by providing a comprehensive software platform for genomic analysis.

**Target Audience**:
- ML Researchers
- Genomic Scientists
- Bioinformaticians

**Tasks**:
- Genome classification
- RNA secondary structure prediction
- Gene expression prediction
- mRNA degradation prediction

**Limitations**: N/A

## 💾 Data

**Source**: Various genomic datasets accessed and integrated from public databases and existing benchmarks.

**Size**: 42 million genomic sequences from 75 datasets

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated benchmarking
- Human evaluation
- Performance recording

**Metrics**:
- F1 Score
- AUC
- RMSE

**Calculation**: Metrics are calculated based on evaluation protocols specified in benchmark suites.

**Interpretation**: Higher scores indicate better model performance on genomic tasks.

**Baseline Results**: OmniGenome was evaluated against various open-source GFMs across multiple benchmarks.

**Validation**: Standardized benchmark protocols ensure reproducibility and reliability in evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
