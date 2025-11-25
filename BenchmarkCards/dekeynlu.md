# DeKeyNLU

## 📊 Benchmark Details

**Name**: DeKeyNLU

**Overview**: DeKeyNLU is a dataset specifically designed to enhance Natural Language Understanding (NLU) capabilities for Natural Language to SQL (NL2SQL) systems, containing 1,500 meticulously annotated question-answer pairs focusing on task decomposition and keyword extraction.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BIRD
- Spider

**Resources**:
- [Resource](https://huggingface.co/datasets/GPS-Lab/DeKeyNLU)
- [GitHub Repository](https://github.com/AlexJJJChen/DeKeyNLU)

## 🎯 Purpose and Intended Users

**Goal**: To refine task decomposition and enhance keyword extraction precision for Natural Language to SQL generation systems.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Text-to-SQL

**Limitations**: The dataset size of 1,500 samples may affect the robustness and generalizability of models trained on it.

## 💾 Data

**Source**: Derived from the BIRD dataset, which contains validated natural language questions paired with SQL commands, and manually annotated for task decomposition and keyword extraction.

**Size**: 1,500 examples

**Format**: JSON

**Annotation**: Initial task decomposition and keyword extraction were performed by GPT-4o, followed by manual refinement from expert annotators through a three-phase cyclic process.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- BLEU
- ROUGE

**Calculation**: Metrics are calculated based on the comparison of generated SQL statements against human-annotated ground truth.

**Interpretation**: Higher scores in BLEU and F1 indicate better task decomposition and keyword extraction performance.

**Validation**: Validation involved cross-validation by annotators to ensure data quality and reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The DeKeyNLU dataset does not contain any personally identifiable information.

**Data Licensing**: CC BY-NC 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
