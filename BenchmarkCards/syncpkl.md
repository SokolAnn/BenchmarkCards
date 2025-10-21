# SynCPKL

## 📊 Benchmark Details

**Name**: SynCPKL

**Overview**: SynCPKL is a new dataset specifically designed for training commonsense persona knowledge linkers. It leverages the SynCPKL Pipeline to generate high-quality synthetic datasets for this task, addressing the lack of suitable training data.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ComFact
- PeaCok

**Resources**:
- [GitHub Repository](https://github.com/irislin1006/CPKL)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to support the training of robust commonsense persona knowledge linkers for open-domain dialogue systems.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Commonsense Persona Knowledge Linking

**Limitations**: N/A

## 💾 Data

**Source**: Generated using the SynCPKL Pipeline leveraging LLMs and the PeaCoK knowledge graph.

**Size**: 39,802 examples

**Format**: N/A

**Annotation**: Synthetic labeling by LLMs (GPT-3.5-Turbo) with a quality control process to ensure relevance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: F1 Score calculated based on the relevance of commonsense persona facts linked to dialogues.

**Interpretation**: Higher F1 scores indicate better performance in linking persona facts with dialogues.

**Validation**: The performance was evaluated using a private test set from the CPKL challenge.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
