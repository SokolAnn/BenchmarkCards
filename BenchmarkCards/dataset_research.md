# DATASET RESEARCH

## 📊 Benchmark Details

**Name**: DATASET RESEARCH

**Overview**: DATASET RESEARCH is the first comprehensive benchmark evaluating AI agents’ ability to discover and synthesize datasets from 208 real-world demands across knowledge-intensive and reasoning-intensive tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/GAIR-NLP/DatasetResearch)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to evaluate AI agents' capabilities in demand-driven dataset discovery and synthesis.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Multiple Choice
- Text Generation
- Summarization
- Text Translation
- Text Classification
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: HuggingFace and PapersWithCode

**Size**: 208 datasets

**Format**: N/A

**Annotation**: Automated metadata generation and human verification

## 🔬 Methodology

**Methods**:
- Metadata evaluation
- Few-shot evaluation
- Supervised fine-tuning

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- ROUGE

**Calculation**: Normalized scores are calculated based on the reference dataset performance.

**Interpretation**: Scores reflect the quality of discovered datasets against reference datasets.

**Baseline Results**: Top fine-tuning score of 22% on difficult DatasetResearch-pro subset.

**Validation**: Performance evaluated through real-world tasks and comparisons with baseline agents.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
