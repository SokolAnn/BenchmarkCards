# BEACON (BEnchm Ark for COmprehensive R NA Task and Language Models)

## 📊 Benchmark Details

**Name**: BEACON (BEnchm Ark for COmprehensive R NA Task and Language Models)

**Overview**: BEACON is the first comprehensive RNA benchmark that encompasses 13 diverse tasks spanning structural analysis, functional studies, and engineering applications, aiming to provide standardized evaluation for RNA models.

**Data Type**: RNA sequences

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/terry-r123/RNABenchmark)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized benchmark for evaluating RNA models across various tasks and their corresponding performance in RNA understanding.

**Target Audience**:
- ML Researchers
- Biologists
- Computational Biologists

**Tasks**:
- Structural Analysis
- Functional Studies
- Engineering Applications

**Limitations**: Although BEACON includes 13 diverse RNA-related tasks, it may not cover all aspects of RNA biology, necessitating further expansions in the future.

## 💾 Data

**Source**: Curated collection of RNA-related tasks derived from previous studies and research papers, including databases like bpRNA-1m, RNAcontact, and others.

**Size**: 967,000 sequences

**Format**: N/A

**Annotation**: Data is compiled from multiple RNA-related research studies and databases.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Top-L Precision
- R^2
- Accuracy (ACC)
- Mean Columnwise Root Mean Squared Error (MCRMSE)

**Calculation**: Metrics are calculated based on the predictions versus ground truth from the datasets used in the benchmark.

**Interpretation**: Higher scores indicate better model performance across the evaluated RNA tasks.

**Baseline Results**: ResNet and LSTM are strong naive supervised models. Pretrained RNA language models showed significant potential, with BEACON-B baseline achieving competitive results on various tasks.

**Validation**: Tasks validated through consistent training and testing processes across multiple RNA sequences.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
